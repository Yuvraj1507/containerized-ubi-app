"""Initial database migration"""

from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Apply the initial migration"""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.String(length=50), nullable=False, unique=True),
        sa.Column('email', sa.String(length=100), nullable=False, unique=True),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.current_timestamp())
    )


def downgrade():
    """Rollback the migration"""
    op.drop_table('users')
