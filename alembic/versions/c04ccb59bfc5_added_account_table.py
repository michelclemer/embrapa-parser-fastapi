"""Added account table

Revision ID: c04ccb59bfc5
Revises: 
Create Date: 2024-05-26 00:56:56.383203

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c04ccb59bfc5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('production',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('id_product', sa.Integer(), nullable=False),
        sa.Column('control_label', sa.String(), nullable=False),
        sa.Column('production_name', sa.String(), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('quantity_liters', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('type_export',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('type_name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_type_export_type_name'), 'type_export', ['type_name'], unique=True)

    op.create_table('type_import',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('type_name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_type_import_type_name'), 'type_import', ['type_name'], unique=True)

    op.create_table('type_process',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('type_name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_type_process_type_name'), 'type_process', ['type_name'], unique=False)

    op.create_table('process_product',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('id_product', sa.Integer(), nullable=False),
        sa.Column('control_label', sa.String(), nullable=False),
        sa.Column('cultivar_name', sa.String(), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('quantity_kg', sa.Integer(), nullable=False),
        sa.Column('type_process_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['type_process_id'], ['type_process.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('comercialization',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('control_label', sa.String(), nullable=False),
        sa.Column('id_product', sa.Integer(), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('quantity_liters', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('import',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('id_product', sa.Integer(), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('country_origin', sa.String(), nullable=False),
        sa.Column('quantity_kg', sa.Integer(), nullable=False),
        sa.Column('price_uss', sa.Float(), nullable=False),
        sa.Column('type_import_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['type_import_id'], ['type_import.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('export',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('id_product', sa.Integer(), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('quantity_kg', sa.Integer(), nullable=False),
        sa.Column('price_uss', sa.Float(), nullable=False),
        sa.Column('type_export_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['type_export_id'], ['type_export.id']),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('export')
    op.drop_table('import')
    op.drop_table('comercialization')
    op.drop_table('process_product')
    op.drop_table('type_process')
    op.drop_table('type_import')
    op.drop_table('type_export')
    op.drop_table('production')