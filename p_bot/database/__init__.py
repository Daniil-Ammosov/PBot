import datetime as dt

from aiogram.types import User

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from .models import UserTG
from ..logger import get_logger


__author__ = "Daniil Ammosov"


class Database:
    name = "database"

    def __init__(self,
                 login: str = None,
                 password: str = None,
                 host: str = None,
                 database: str = None):

        self.logger = get_logger(self.name)

        self.engine = sa.create_engine(f"mysql+pymysql://{login}:{password}@{host}/{database}?charset=utf8")
        self.Session = sessionmaker(bind=self.engine)
        self.session_ = None

    @property
    def session(self):
        if self.session_ is None:
            self.session_ = self.Session()

        return self.session_

    def close(self):
        self.engine.dispose()

    def delete_user(self, user: User):
        try:
            self.session.query(
                    UserTG
            ).filter_by(
                    telegram_id=user.id
            ).delete()

            self.session.commit()
            return True

        except SQLAlchemyError as e:
            self.logger.exception(f"Пользователь {user.full_name} ID:{user.id} не удалён. Catch error: {str(e)}")
            self.session.rollback()
            return False

        finally:
            self.session.close()

    def add_new_user(self, user: User, quantity_days: int) -> bool:
        new_user = UserTG(
                telegram_id=user.id,
                login=user.username,
                license_end_date=dt.datetime.now() + dt.timedelta(days=quantity_days))

        try:
            self.session.add(new_user)
            self.session.commit()
            return True

        except SQLAlchemyError as e:
            self.logger.exception(f"Пользователь {user.full_name} ID:{user.id} не добавлен. Catch error: {str(e)}")
            self.session.rollback()
            return False

        finally:
            self.session.close()

    def update_user_license(self, user: User, quantity_days: int) -> bool:
        try:
            self.session.query(
                    UserTG
            ).filter_by(
                    telegram_id=user.id
            ).update(
                    {
                        UserTG.purchase_date: dt.datetime.now(),
                        UserTG.license_end_date: dt.datetime.now() + dt.timedelta(days=quantity_days)
                    }
            )
            return True

        except SQLAlchemyError as e:
            self.logger.exception(f"Для пользователя {user.full_name} ID:{user.id} лицензия не продлена. Catch error: {str(e)}")
            self.session.rollback()
            return False

        finally:
            self.session.close()
