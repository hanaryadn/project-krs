"""empty message

Revision ID: f1dacd342deb
Revises: c28bfec6b5e0
Create Date: 2018-07-15 12:10:27.998827

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f1dacd342deb'
down_revision = 'c28bfec6b5e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=20), nullable=False))
    op.drop_column('user', 'user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user', mysql.VARCHAR(length=20), nullable=False))
    op.drop_column('user', 'username')
    # ### end Alembic commands ###