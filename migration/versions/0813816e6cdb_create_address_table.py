"""create address table

Revision ID: 0813816e6cdb
Revises: ec409c537ac5
Create Date: 2022-12-26 23:16:18.201740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0813816e6cdb'
down_revision = 'ec409c537ac5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'address',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=True),
        sa.Column('description', sa.String, nullable=True)
    )

def downgrade():
    op.drop_table('address')
