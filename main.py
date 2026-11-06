from core.notifiers import ConsoleNotifier, TelegramNotifier  # Tambahkan TelegramNotifier di sini
from core.processor import PaymentProcessor
from core.registry import buat_metode, daftar_plugin
from core.utils import rupiah
from plugins import muat_semua_plugin
from core.protocols import Notifier  # Opsional untuk uji isinstance

def main() -> None:
    muat_semua_plugin()
    print("Plugin terdaftar:", daftar_plugin())
    print("-" * 60)
 
    pemroses = PaymentProcessor(ConsoleNotifier())
 
    skenario = [
        ("transfer", {"saldo": 1_000_000, "bank": "BCA"}, 250_000),
        ("ewallet", {"saldo": 100_000}, 150_000),
        ("ewallet", {"saldo": 5_000_000}, 2_500_000),
        ("qris", {}, 50_000),
    ]
 
    for kode, parameter, jumlah in skenario:
        try:
            metode = buat_metode(kode, **parameter)
        except KeyError as err:
            print("[PERINGATAN]", err)
            continue
        pemroses.checkout(metode, jumlah, pelanggan="mahasiswa@utr.ac.id")
 
    print("-" * 60)
    print("Riwayat transaksi berhasil:")
    for trx_id, nama, jumlah in pemroses.riwayat:
        print(f"  {trx_id} | {nama} | {rupiah(jumlah)}")

    # --- TAMBAHAN KHUSUS PENGUJIAN TUGAS 2 ---
    print("-" * 60)
    print("Uji Coba Tugas 2 (TelegramNotifier):")
    tg_notifier = TelegramNotifier()
    
    # 1. Buktikan memenuhi Protocol via isinstance (structural subtyping)
    print("TelegramNotifier memenuhi Notifier?", isinstance(tg_notifier, Notifier))
    
    # 2. Uji pasang ke PaymentProcessor
    pemroses.notifier = tg_notifier
    pemroses.checkout(buat_metode("transfer", saldo=500_000, bank="Mandiri"), 100_000, pelanggan="mahasiswa@utr.ac.id")
    # ----------------------------------------
 
if __name__ == "__main__":
    main()