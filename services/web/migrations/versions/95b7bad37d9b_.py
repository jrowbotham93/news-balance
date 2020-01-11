"""empty message

Revision ID: 95b7bad37d9b
Revises: 
Create Date: 2020-01-11 10:41:42.714544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95b7bad37d9b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Article', sa.Column('abstract', sa.String(length=1000), nullable=False))
    op.drop_constraint('Article_description_key', 'Article', type_='unique')
    op.create_unique_constraint(None, 'Article', ['abstract'])
    op.drop_column('Article', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Article', sa.Column('description', sa.VARCHAR(length=10000), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'Article', type_='unique')
    op.create_unique_constraint('Article_description_key', 'Article', ['description'])
    op.drop_column('Article', 'abstract')
    # ### end Alembic commands ###