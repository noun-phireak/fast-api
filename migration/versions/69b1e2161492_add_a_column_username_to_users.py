"""Add a column username to Users

Revision ID: 69b1e2161492
Revises: 0813816e6cdb
Create Date: 2022-12-28 20:32:08.581042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69b1e2161492'
down_revision = '0813816e6cdb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('username', sa.String))


def downgrade():
    op.drop_column('users', 'username')
