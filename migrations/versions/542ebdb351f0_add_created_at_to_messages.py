"""add created_at to messages

Revision ID: 542ebdb351f0
Revises: 313aa6e840e1
Create Date: 2023-06-04 18:02:10.144375

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "542ebdb351f0"
down_revision = "313aa6e840e1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "output_messages", sa.Column("created_at", sa.Integer(), nullable=True)
    )
    op.add_column(
        "prompt_messages", sa.Column("created_at", sa.Integer(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("prompt_messages", "created_at")
    op.drop_column("output_messages", "created_at")
    # ### end Alembic commands ###
