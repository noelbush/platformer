"""initial models

Revision ID: 1dfc5670a58f
Revises: None
Create Date: 2013-01-23 22:22:16.482028

"""

# revision identifiers, used by Alembic.
revision = '1dfc5670a58f'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('secret',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('secret', sa.Unicode(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('secret')
    )
    op.create_table('memo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.Unicode(), nullable=False),
    sa.Column('value', sa.Unicode(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('peer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.Unicode(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('health', sa.Float(), nullable=False),
    sa.Column('last_checked', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    op.create_table('reliability_metadata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source', sa.Unicode(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('memo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['memo_id'], ['memo.id'], ),
    sa.PrimaryKeyConstraint('id', 'score'),
    sa.UniqueConstraint('source')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reliability_metadata')
    op.drop_table('peer')
    op.drop_table('memo')
    op.drop_table('secret')
    ### end Alembic commands ###
