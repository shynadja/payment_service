"""initial migration

Revision ID: 312bd01b4d59
Revises: 
Create Date: 2024-12-17 17:24:06.199144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '312bd01b4d59'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('company_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('company_id')
    )
    op.create_table('payments',
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('payment_id', sa.String(), nullable=False),
    sa.Column('amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('type', sa.String(length=30), nullable=False),
    sa.Column('payment_status', sa.String(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.company_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('payment_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payments')
    op.drop_table('companies')
    # ### end Alembic commands ###
