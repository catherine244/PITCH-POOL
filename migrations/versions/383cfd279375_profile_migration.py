"""Profile Migration

Revision ID: 383cfd279375
Revises: 2ad9362032a0
Create Date: 2018-09-09 01:45:04.395404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '383cfd279375'
down_revision = '2ad9362032a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###