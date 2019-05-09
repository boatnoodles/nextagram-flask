from app import login_manager
from config import AWS_DOMAIN
from flask_login import UserMixin
from models.base_model import BaseModel
from playhouse.hybrid import hybrid_property
import peewee as pw


@login_manager.user_loader
def get_user(id):
    user = User.get_by_id(id)
    return user


class User(BaseModel, UserMixin):
    username = pw.CharField(null=False, unique=True)
    email = pw.CharField(null=False, unique=True)
    password = pw.TextField(null=False)
    privacy = pw.BooleanField(null=True, default=False)
    profile_picture = pw.CharField(null=True, default=None)
    # TODO SET DEFAULT PICTURE

    @hybrid_property
    def profile_picture_url(self):
        """Call via instance
        e.g., user = User.get_by_id(current_user.id)
        e.g., user.profile_picture_url"""
        return f"{AWS_DOMAIN}/{self.profile_picture}"
