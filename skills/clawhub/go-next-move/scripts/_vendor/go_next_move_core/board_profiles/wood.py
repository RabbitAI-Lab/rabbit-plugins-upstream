from __future__ import annotations

from . import common


PROFILE_NAME = "wood"


def classify_intersections(warped, xfit, yfit, board_size: int) -> list[list[str]]:
    return common.classify_intersections(warped, xfit, yfit, board_size, classify_cell)


def classify_cell(features: common.IntersectionFeatures) -> str:
    white_shape_ok = features.center_low_sat > 0.70 and features.edge_contrast > -2.0
    edge_white_shape_ok = (
        features.center_low_sat > 0.80
        and features.edge_contrast > 12.0
        and features.white_core > 0.50
        and features.bright_low_sat > 0.50
        and features.bright_fraction > 0.50
        and features.mean_s < 92
    )
    # Robust bright-stone path for warm/bright boards (e.g. bamboo),
    # where white stones keep a slight warm tint (saturation ~60-85) and
    # so fail the low-saturation shape checks above. A white stone is
    # very bright across most of the patch and its center is brighter
    # than its shadowed rim (edge_contrast > 0), while empty wood is much
    # darker (mean_v ~150) with a dark grid line through the center
    # (edge_contrast < 0).
    white_bright_ok = (
        features.bright_fraction > 0.50
        and features.mean_v > 185.0
        and features.mean_s < 95.0
        and features.white_core > 0.50
        and features.edge_contrast > 0.5
    )
    white_uniform_ok = (
        features.bright_fraction > 0.96
        and features.bright_low_sat > 0.96
        and features.white_core > 0.96
        and features.center_low_sat > 0.96
        and features.mean_s < 45.0
        and features.edge_contrast > -4.0
    )
    black_ok = features.dark_fraction > 0.30 or (
        features.mean_v < 108 and features.very_dark_fraction > 0.10
    )
    white_ok = (
        white_bright_ok
        or white_uniform_ok
        or (
            white_shape_ok
            and (
                (features.bright_low_sat > 0.48 and features.mean_s < 55)
                or (
                    features.white_core > 0.36
                    and features.mean_s < 78
                    and features.bright_fraction > 0.60
                )
                or edge_white_shape_ok
            )
        )
    )

    if black_ok:
        return "B"
    if white_ok:
        return "W"
    return "."


def assess_recognition(black_stones: int, white_stones: int) -> tuple[list[str], bool]:
    warnings = common.suspicious_white_count_warning(black_stones, white_stones)
    return warnings, not warnings
