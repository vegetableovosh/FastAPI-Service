"""empty message

Revision ID: 41c1658d6431
Revises: 9fcf17b48261, c6c41fed3441
Create Date: 2024-09-30 21:05:08.053519

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41c1658d6431'
down_revision: Union[str, None] = ('9fcf17b48261', 'c6c41fed3441')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
