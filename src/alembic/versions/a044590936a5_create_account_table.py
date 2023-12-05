"""create user table

Revision ID: a044590936a5
Revises: 
Create Date: 2023-12-05 13:10:19.909793

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a044590936a5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(30), nullable=False),
        sa.Column('password', sa.String(30), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('user')
