# Tests for pcv.analyze.distribution
import cv2
from plantcv.plantcv import outputs
from plantcv.plantcv.analyze import distribution as analyze_distribution


def test_distribution(test_data):
    """Test for PlantCV."""
    # Clear previous outputs
    outputs.clear()
    # Read in test data
    mask = cv2.imread(test_data.small_bin_img, -1)

    _ = analyze_distribution(labeled_mask=mask, n_labels=1)
    assert int(outputs.observations['default_1']['X_distribution_mean']['value']) == 200
