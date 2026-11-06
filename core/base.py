from abc import ABC, abstractmethod
from core.utils import rupiah

class PembayaranGagal(Exception):
    """Dilempar saat pembayaran ditolak atau tidak valid."""

class PaymentMethod(ABC):
    """Kontrak (abstract base class) untuk semua metode pembayaran."""

    def __init__(self, nama: str):
        self.nama = nama

    @abstractmethod
    def validasi(self, jumlah: float) -> bool:
        """Periksa apakah pembayaran dapat diproses."""

    @abstractmethod
    def bayar(self, jumlah: float) -> str:
        """Proses pembayaran, lalu kembalikan ID transaksi."""

    @abstractmethod
    def biaya_admin(self, jumlah: float) -> float:
        """Hitung biaya admin berdasarkan jumlah transaksi."""

    def proses(self, jumlah: float) -> str:
        """Template method: urutan langkah dijaga oleh kelas induk."""
        admin = self.biaya_admin(jumlah)
        total = jumlah + admin

        if total <= 0:
            raise PembayaranGagal("Jumlah pembayaran harus lebih dari 0")
        
        # Validasi menggunakan total (jumlah + biaya admin)
        if not self.validasi(total):
            raise PembayaranGagal(
                f"{self.nama} menolak pembayaran total {rupiah(total)} (termasuk admin {rupiah(admin)})"
            )
        return self.bayar(total)