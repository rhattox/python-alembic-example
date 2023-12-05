"""Add a creation date column

Revision ID: d7cad586b520
Revises: a044590936a5
Create Date: 2023-12-05 13:18:41.464105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7cad586b520'
down_revision: Union[str, None] = 'a044590936a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('user', sa.Column('creation_date', sa.DateTime))


def downgrade() -> None:
    op.drop_column('user', 'creation_date')
