from src.connectivity import Connectivity


def test_modify_connectivity_description():
    assert Connectivity.modify("Standalone") == "Free-Standing"
    assert Connectivity.modify("Semi-Connected") == "Single Connected"
    assert Connectivity.modify("End-Connected") == "Dual-Connected"
