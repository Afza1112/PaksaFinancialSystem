"""
API v1 router.
"""
from fastapi import APIRouter

api_router = APIRouter()

# Accounts Payable
try:
    from app.api.endpoints.accounts_payable import vendor, invoice, payment, credit_memo, form_1099
    api_router.include_router(vendor.router, prefix="/accounts-payable/vendors", tags=["accounts-payable", "vendors"])
    api_router.include_router(invoice.router, prefix="/accounts-payable/invoices", tags=["accounts-payable", "invoices"])
    api_router.include_router(payment.router, prefix="/accounts-payable/payments", tags=["accounts-payable", "payments"])
    api_router.include_router(credit_memo.router, prefix="/accounts-payable/credit-memos", tags=["accounts-payable", "credit-memos"])
    api_router.include_router(form_1099.router, prefix="/accounts-payable/1099", tags=["accounts-payable", "1099-reporting"])
except ImportError as e:
    print(f"Warning: Could not import accounts payable modules: {e}")

# Inventory
try:
    from app.api.endpoints.inventory import (
        item as inventory_item, adjustment as inventory_adjustment, category as inventory_category,
        purchase_order as inventory_purchase_order, reports as inventory_reports,
        barcode as inventory_barcode, cycle_count as inventory_cycle_count,
        forecast as inventory_forecast, location as inventory_location,
        transaction as inventory_transaction
    )
    api_router.include_router(inventory_item.router, prefix="/inventory/items", tags=["inventory", "items"])
    api_router.include_router(inventory_adjustment.router, prefix="/inventory/adjustments", tags=["inventory", "adjustments"])
    api_router.include_router(inventory_category.router, prefix="/inventory/categories", tags=["inventory", "categories"])
    api_router.include_router(inventory_purchase_order.router, prefix="/inventory/purchase-orders", tags=["inventory", "purchase-orders"])
    api_router.include_router(inventory_reports.router, prefix="/inventory/reports", tags=["inventory", "reports"])
    api_router.include_router(inventory_barcode.router, prefix="/inventory/barcode", tags=["inventory", "barcode"])
    api_router.include_router(inventory_cycle_count.router, prefix="/inventory/cycle-counts", tags=["inventory", "cycle-counts"])
    api_router.include_router(inventory_forecast.router, prefix="/inventory/forecast", tags=["inventory", "forecast"])
    api_router.include_router(inventory_location.router, prefix="/inventory/locations", tags=["inventory", "locations"])
    api_router.include_router(inventory_transaction.router, prefix="/inventory/transactions", tags=["inventory", "transactions"])
except ImportError as e:
    print(f"Warning: Could not import inventory modules: {e}")

# Operations
try:
    from app.api.endpoints.operations import router as operations_router
    api_router.include_router(operations_router, prefix="/operations", tags=["operations"])
except ImportError as e:
    print(f"Warning: Could not import operations module: {e}")

# Data Migration
try:
    from app.api.endpoints.data_migration import router as data_migration_router
    api_router.include_router(data_migration_router, prefix="/data-migration", tags=["data-migration"])
except ImportError as e:
    print(f"Warning: Could not import data migration module: {e}")

# User Administration
try:
    from app.api.endpoints.user_admin import router as user_admin_router
    api_router.include_router(user_admin_router, prefix="/user-admin", tags=["user-admin"])
except ImportError as e:
    print(f"Warning: Could not import user admin module: {e}")

# Localization
try:
    from app.api.endpoints.localization import router as localization_router
    api_router.include_router(localization_router, prefix="/localization", tags=["localization"])
except ImportError as e:
    print(f"Warning: Could not import localization module: {e}")

# Analytics
try:
    from app.api.endpoints import analytics
    api_router.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
except ImportError as e:
    print(f"Warning: Could not import analytics module: {e}")

# Add additional routers below as needed, using the same style.