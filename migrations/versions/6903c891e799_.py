"""empty message

Revision ID: 6903c891e799
Revises: b363e2f3dc11
Create Date: 2018-06-01 23:56:10.750012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6903c891e799'
down_revision = 'b363e2f3dc11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'create_time')
    # ### end Alembic commands ###