from src.utils.pricing import calculate_premium
def test_premium():
    calculate_premium(30, 1, False)

def normalize_gender(value: str) -> int:
    """Map 'Male'/'Female' (case-insensitive) to 1/0; raise ValueError otherwise."""
    mapping = {"male": 1, "female": 0}
    try:
        return mapping[value.strip().lower()]
    except KeyError:
        raise ValueError(f"Unknown gender: {value!r}") from None