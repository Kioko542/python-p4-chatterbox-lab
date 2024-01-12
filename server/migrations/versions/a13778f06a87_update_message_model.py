"""update Message model

Revision ID: a13778f06a87
Revises: ecdfbfbde726
Create Date: 2024-01-12 17:27:16.671624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a13778f06a87'
down_revision = 'ecdfbfbde726'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('body', sa.String(), nullable=False))
    op.add_column('messages', sa.Column('username', sa.String(), nullable=False))
    op.add_column('messages', sa.Column('created_at', sa.String(), nullable=False))
    op.add_column('messages', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'updated_at')
    op.drop_column('messages', 'created_at')
    op.drop_column('messages', 'username')
    op.drop_column('messages', 'body')
    # ### end Alembic commands ###
