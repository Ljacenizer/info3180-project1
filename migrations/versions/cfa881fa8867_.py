"""empty message

Revision ID: cfa881fa8867
Revises: 076da3f5ff64
Create Date: 2023-03-12 04:27:28.029284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfa881fa8867'
down_revision = '076da3f5ff64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=5000), nullable=True),
    sa.Column('roomnum', sa.Integer(), nullable=True),
    sa.Column('bathnum', sa.Integer(), nullable=True),
    sa.Column('price', sa.String(length=15), nullable=True),
    sa.Column('propertytype', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
