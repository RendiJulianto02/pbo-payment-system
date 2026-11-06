import pytest
from core.base import PaymentMethod
from core.registry import buat_metode


def test_payment_method_is_abstract():
    """Memastikan kelas abstrak PaymentMethod tidak dapat diinstansiasi langsung."""
    with pytest.raises(TypeError):
        PaymentMethod("uji")


def test_unknown_plugin_raises_key_error():
    """Memastikan pemanggilan plugin tak dikenal memunculkan KeyError."""
    with pytest.raises(KeyError):
        buat_metode("plugin_palsu", saldo=100_000)