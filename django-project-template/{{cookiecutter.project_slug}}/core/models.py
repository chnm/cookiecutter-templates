import logging

from django.db import models
from django.utils.text import camel_case_to_spaces

logger = logging.getLogger(__name__)

class BaseMeta(models.base.ModelBase):
    def __new__(cls, name, bases, attrs, **kwargs):

        meta = attrs.get('Meta')

        if meta:
            logger.debug(f"{name} has meta")

            if (
                not hasattr(meta, 'db_table')
                and not getattr(meta, 'abstract', False)
            ):
                logger.debug(f"{name} is concrete and has no db_table meta")
                meta.db_table = name.lower()
            else:
                logger.debug(f"{name} is abstract or has db_table meta")
        else:
            logger.debug(f"{name} has no meta")
            class Meta:
                db_table = name.lower()
            attrs['Meta'] = Meta

        return super().__new__(cls, name, bases, attrs, **kwargs)

class BaseModel(models.Model, metaclass=BaseMeta):
    class Meta:
        abstract = True
