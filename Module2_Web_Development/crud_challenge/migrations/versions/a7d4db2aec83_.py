"""empty message

Revision ID: a7d4db2aec83
Revises: 
Create Date: 2024-11-14 12:32:26.473632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7d4db2aec83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('cpf', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
