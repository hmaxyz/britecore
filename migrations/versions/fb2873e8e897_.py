"""empty message

Revision ID: fb2873e8e897
Revises: 
Create Date: 2019-03-29 02:20:32.747468

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fb2873e8e897'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feature_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('client', mysql.ENUM('Client A', 'Client B', 'Client C'), nullable=False),
    sa.Column('client_priority', sa.SmallInteger(), nullable=False),
    sa.Column('target_date', sa.Date(), nullable=False),
    sa.Column('product_area', mysql.ENUM('Policies', 'Billing', 'Claims', 'Reports'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feature_request')
    # ### end Alembic commands ###
