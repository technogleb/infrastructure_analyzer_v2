from sqlalchemy import create_engine

from ianapp.config import SQLALCHEMY_DATABASE_URI
from ianapp.infrastructure.models import Base1
from ianapp.realty.models import Base2

# Это твой комментарий? Если да, то он здесь лишний, и так понятно, что такое echo, стоит зайти в документацию


# The echo flag is a shortcut to setting up SQLAlchemy logging, which is accomplished via Python’s standard logging
# module. With it enabled, we’ll see all the generated SQL produced. If you are working through this tutorial and
# want less output generated, set it to False. This tutorial will format the SQL behind a popup window so it doesn’t
# get in our way; just click the “SQL” links to see what’s being generated.
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)

Base1.metadata.create_all(engine)
Base2.metadata.create_all(engine)

# почему create_db находится в самом верху структуры проекта, я бы поместил его внутрь ianapp
