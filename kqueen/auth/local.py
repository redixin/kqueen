from .base import BaseAuth
from kqueen.models import User

import bcrypt
import logging

logger = logging.getLogger('kqueen_api')


class LocalAuth(BaseAuth):
    verbose_name = 'Local'
    parameter_schema = {
        'username': {
            'type': 'email',
            'label': 'User Email',
            'description': 'Provide valid email of the user you want to invite to the organization',
            'validators': {
                'required': True
            },
            'active': False,
            'notify': True
        }
    }

    def verify(self, user, password):
        """Implementation of :func:`~kqueen.auth.base.__init__`

        This function tries to find local user and verify password.
        """

        if isinstance(user, User):
            user_password = user.password.encode('utf-8')
            given_password = password

            if bcrypt.checkpw(given_password, user_password):
                return user, None

        msg = "Local authentication failed"
        logger.info(msg)
        return None, msg
