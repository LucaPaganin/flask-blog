"""empty message

Revision ID: 87873d423995
Revises: a37d238614fa
Create Date: 2022-04-25 19:48:26.697946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87873d423995'
down_revision = 'a37d238614fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###
