from core.base import PaymentMethod
from core.registry import register_plugin
from core.utils import buat_id
import datetime


@register_plugin("va")
class VirtualAccount(PaymentMethod):
    def __init__(self, bank: str = "BCA", expired_minutes: int = 15):
        super().__init__(f"Virtual Account {bank}")
        self.expired_minutes = expired_minutes
        self.status = "menunggu"  # Status awal transaksi

    def validasi(self, jumlah: float) -> bool:
        # Validasi transaksi VA (misal: jumlah harus di atas 0)
        return jumlah > 0

    def bayar(self, jumlah: float) -> str:
        self.status = "dibayar"
        return buat_id("VA")

    def biaya_admin(self, jumlah: float) -> float:
        # Menyesuaikan dengan Tugas 3 (jika ada biaya admin)
        return 4_000.0