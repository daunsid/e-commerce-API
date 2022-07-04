"""add table to database

Revision ID: 41cfe136fb91
Revises: 
Create Date: 2022-07-02 11:41:48.548167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41cfe136fb91'
down_revision = None
branch_labels = None
depends_on = None

"""
name = Column(String)
    slug = Column(String, unique=True)
    url = Column(URLType)
    description = Column(TEXT)
    price = Column(DECIMAL)
    available = Column(Boolean)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, onupdate = datetime.now)
"""


def upgrade() -> None:

    op.create_table('product',
        sa.Column('id', sa.Integer, primary_key=True,unique=True),
        sa.Column('name', sa.String(100)),
        sa.Column('slug', sa.String(100)),
        sa.Column('url', sa.String(200)),
        sa.Column('description',sa.TEXT),
        sa.Column('price',sa.DECIMAL(scale=2)),
        sa.Column('available',sa.Boolean),
        sa.Column('created_date',sa.DateTime),
        sa.Column('updated', sa.DateTime)
    )
    pass


def downgrade() -> None:
    op.drop_table("product")
    pass
