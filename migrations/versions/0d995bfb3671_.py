"""empty message

Revision ID: 0d995bfb3671
Revises: 010744bcdb8d
Create Date: 2017-08-26 12:19:15.826296

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d995bfb3671'
down_revision = '010744bcdb8d'


def upgrade():
    # commands auto generated by Alembic - please adjust! #
    op.create_table('feedback',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('rating', sa.String(), nullable=False),
                    sa.Column('comment', sa.String(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('event_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'))
    # end Alembic commands #


def downgrade():
    # commands auto generated by Alembic - please adjust! #
    op.drop_table('feedback')
    # end Alembic commands #