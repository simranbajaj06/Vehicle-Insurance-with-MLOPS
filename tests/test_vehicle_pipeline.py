"""Tests intentionally call fixture functions so graph links can be extracted."""

import pytest

from graph_test_fixtures.vehicle_pipeline import (
    normalize_vehicle_type,
    prepare_prediction_input,
    validate_record,
)


def test_validate_record_accepts_required_fields():
    record = {"policy_id": "POL-101", "vehicle_type": "SUV"}
    assert validate_record(record) == record


def test_validate_record_rejects_missing_policy_id():
    with pytest.raises(ValueError, match="policy_id"):
        validate_record({"vehicle_type": "SUV"})


def test_normalize_vehicle_type_trims_and_lowercases():
    assert normalize_vehicle_type("  SUV  ") == "suv"


def test_normalize_vehicle_type_rejects_empty_value():
    with pytest.raises(ValueError, match="cannot be empty"):
        normalize_vehicle_type("   ")


def test_prepare_prediction_input_normalizes_vehicle_type():
    result = prepare_prediction_input(
        {"policy_id": " POL-101 ", "vehicle_type": "  SUV "}
    )
    assert result == {"policy_id": "POL-101", "vehicle_type": "suv"}


def test_prepare_prediction_input_rejects_invalid_record():
    with pytest.raises(ValueError, match="policy_id"):
        prepare_prediction_input({"vehicle_type": "SUV"})