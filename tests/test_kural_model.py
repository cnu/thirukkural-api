import pytest
from app.models.kural import KuralModel

@pytest.fixture
def kural_model():
    return KuralModel()

def test_get_kurals_by_numbers_with_list(kural_model):
    """Test getting kurals by providing a list of numbers instead of a string"""
    # Test with a list of integers
    kurals = kural_model.get_kurals_by_numbers([1, 2, 3])
    
    # Verify the results
    assert len(kurals) == 3
    assert kurals[0]['Number'] == 1
    assert kurals[1]['Number'] == 2
    assert kurals[2]['Number'] == 3
