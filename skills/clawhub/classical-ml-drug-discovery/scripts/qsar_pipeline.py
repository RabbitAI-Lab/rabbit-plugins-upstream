#!/usr/bin/env python3
"""Leakage-aware classical molecular ML for local drug-discovery workflows.

Commands:
  audit   Parse, standardize, deduplicate, and audit a labeled CSV.
  train   Compare RF, SVM/SVR, Gradient Boosting, and optional XGBoost.
  predict Score a CSV with a trusted model bundle and add domain flags.

This tool is decision support. Predictions are not evidence of efficacy or safety.
It performs no network requests and reads only user-specified paths.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import re
import sys
import warnings
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import joblib
    import numpy as np
    import pandas as pd
    import sklearn
    from sklearn.base import clone
    from sklearn.calibration import CalibratedClassifierCV
    from sklearn.ensemble import (
        GradientBoostingClassifier,
        GradientBoostingRegressor,
        RandomForestClassifier,
        RandomForestRegressor,
    )
    from sklearn.metrics import (
        accuracy_score,
        average_precision_score,
        balanced_accuracy_score,
        brier_score_loss,
        f1_score,
        matthews_corrcoef,
        mean_absolute_error,
        mean_squared_error,
        r2_score,
        roc_auc_score,
    )
    from sklearn.model_selection import (
        GridSearchCV,
        GroupKFold,
        GroupShuffleSplit,
        KFold,
        StratifiedGroupKFold,
        StratifiedKFold,
        TimeSeriesSplit,
        train_test_split,
    )
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler, label_binarize
    from sklearn.svm import SVC, SVR
    from sklearn.cluster import KMeans
    from sklearn.decomposition import PCA
    from sklearn.inspection import permutation_importance
except ImportError as exc:  # pragma: no cover - environment-dependent
    raise SystemExit(
        "Missing required Python dependency. Install requirements-optional.txt "
        f"in an isolated environment. Original error: {exc}"
    ) from exc

RDKIT_IMPORT_ERROR: Exception | None = None
try:
    from rdkit import Chem, DataStructs, rdBase
    from rdkit.Chem import QED, Crippen, Descriptors, Lipinski, rdFingerprintGenerator
    from rdkit.Chem.MolStandardize import rdMolStandardize
    from rdkit.Chem.Scaffolds import MurckoScaffold
except ImportError as exc:  # defer failure so --help remains useful
    RDKIT_IMPORT_ERROR = exc

TOOL_VERSION = "1.3.0"
DEFAULT_FP_RADIUS = 2
DEFAULT_FP_BITS = 2048

DESCRIPTOR_NAMES = [
    "MolWt",
    "MolLogP",
    "TPSA",
    "HBD",
    "HBA",
    "RotatableBonds",
    "RingCount",
    "AromaticRingCount",
    "FractionCSP3",
    "HeavyAtomCount",
    "FormalCharge",
    "QED",
]


@dataclass
class ModelSpec:
    name: str
    estimator: Any
    param_grid: dict[str, list[Any]]


def require_rdkit() -> None:
    if RDKIT_IMPORT_ERROR is not None:
        raise SystemExit(
            "RDKit is required for molecular parsing and featurization. Install it with "
            "`python3 -m pip install rdkit` in an isolated environment. "
            f"Original error: {RDKIT_IMPORT_ERROR}"
        )


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def json_default(value: Any) -> Any:
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        return float(value)
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, Path):
        return str(value)
    return str(value)


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            data,
            indent=2,
            sort_keys=True,
            default=json_default,
            allow_nan=False,
        )
        + "\n",
        encoding="utf-8",
    )


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_label(value: Any) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value).strip()


def canonicalize_smiles(
    smiles: Any,
    *,
    uncharge: bool = True,
    tautomer_canonicalize: bool = False,
) -> tuple[str | None, Any | None, str | None]:
    """Return canonical parent SMILES, RDKit molecule, and error text."""
    require_rdkit()
    text = "" if pd.isna(smiles) else str(smiles).strip()
    if not text:
        return None, None, "empty_smiles"
    try:
        mol = Chem.MolFromSmiles(text, sanitize=True)
        if mol is None:
            return None, None, "parse_failed"
        mol = rdMolStandardize.Cleanup(mol)
        mol = rdMolStandardize.LargestFragmentChooser().choose(mol)
        if uncharge:
            mol = rdMolStandardize.Uncharger().uncharge(mol)
        if tautomer_canonicalize:
            mol = rdMolStandardize.TautomerEnumerator().Canonicalize(mol)
        Chem.SanitizeMol(mol)
        canonical = Chem.MolToSmiles(mol, canonical=True, isomericSmiles=True)
        if not canonical:
            return None, None, "canonicalization_failed"
        return canonical, mol, None
    except Exception as exc:  # noqa: BLE001 - RDKit raises several wrapped exception types
        return None, None, f"standardization_failed:{type(exc).__name__}"


def scaffold_for_mol(mol: Any) -> str:
    """Generate a chirality-aware Murcko scaffold, with an acyclic topology fallback."""
    require_rdkit()
    scaffold = MurckoScaffold.GetScaffoldForMol(mol)
    if scaffold is not None and scaffold.GetNumAtoms() > 0:
        return Chem.MolToSmiles(scaffold, canonical=True, isomericSmiles=True)
    generic = MurckoScaffold.MakeScaffoldGeneric(mol)
    generic_smiles = Chem.MolToSmiles(generic, canonical=True, isomericSmiles=False)
    return f"ACYCLIC:{generic_smiles}"


def ensure_no_output_overwrite(
    sources: Sequence[Path], destinations: Sequence[Path]
) -> None:
    """Refuse configurations that would overwrite an input or trusted model artifact."""
    source_set = {path.expanduser().resolve() for path in sources}
    for destination in destinations:
        resolved = destination.expanduser().resolve()
        if resolved in source_set:
            raise SystemExit(f"Refusing to overwrite an input artifact: {resolved}")


def read_csv_checked(path: Path, required_columns: Sequence[str]) -> pd.DataFrame:
    if not path.is_file():
        raise SystemExit(f"Input file does not exist: {path}")
    try:
        frame = pd.read_csv(path)
    except Exception as exc:
        raise SystemExit(f"Could not read CSV {path}: {exc}") from exc
    missing = [column for column in required_columns if column not in frame.columns]
    if missing:
        raise SystemExit(
            f"Missing required column(s) {missing}. Available columns: {list(frame.columns)}"
        )
    if frame.empty:
        raise SystemExit(f"Input CSV has no rows: {path}")
    return frame


def curate_labeled_dataframe(
    frame: pd.DataFrame,
    *,
    smiles_column: str,
    target_column: str,
    task: str,
    uncharge: bool,
    tautomer_canonicalize: bool,
    conflict_policy: str,
    time_column: str | None = None,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Standardize structures, aggregate duplicates, and return an audit.

    When ``time_column`` is supplied, every modeled row must have a parseable timestamp and a
    duplicate parent receives its latest source timestamp. Assigning the whole parent to that
    latest time prevents an aggregate containing a future measurement from entering an earlier
    temporal training block.
    """
    records: list[dict[str, Any]] = []
    invalid_examples: list[dict[str, Any]] = []
    missing_target = 0

    for input_row, row in frame.iterrows():
        target = row[target_column]
        if pd.isna(target) or safe_label(target) == "":
            missing_target += 1
            continue
        canonical, mol, error = canonicalize_smiles(
            row[smiles_column],
            uncharge=uncharge,
            tautomer_canonicalize=tautomer_canonicalize,
        )
        if error is not None:
            if len(invalid_examples) < 25:
                invalid_examples.append(
                    {
                        "input_row": int(input_row),
                        "smiles": safe_label(row[smiles_column]),
                        "error": error,
                    }
                )
            continue
        value: Any
        if task == "regression":
            try:
                value = float(target)
                if not math.isfinite(value):
                    raise ValueError("non-finite")
            except (TypeError, ValueError):
                missing_target += 1
                continue
        else:
            value = safe_label(target)
        record = {
            "_input_row": int(input_row),
            "input_smiles": safe_label(row[smiles_column]),
            "canonical_smiles": canonical,
            "scaffold": scaffold_for_mol(mol),
            "target": value,
        }
        if time_column is not None:
            record["_time_value"] = row[time_column]
        records.append(record)

    parsed = pd.DataFrame(records)
    if parsed.empty:
        raise SystemExit(
            "No valid labeled molecules remained after parsing and target checks."
        )
    if time_column is not None:
        parsed_time = pd.to_datetime(parsed["_time_value"], errors="coerce", utc=True)
        if parsed_time.isna().any():
            bad = int(parsed_time.isna().sum())
            raise SystemExit(
                f"Time column contains {bad} missing or unparseable value(s) among modeled rows."
            )
        parsed["_time_value"] = parsed_time

    duplicate_rows = int(len(parsed) - parsed["canonical_smiles"].nunique())
    conflict_groups = 0
    dropped_conflict_groups = 0
    aggregated: list[dict[str, Any]] = []

    for canonical, group in parsed.groupby("canonical_smiles", sort=False):
        base = group.iloc[0].to_dict()
        base["source_row_count"] = len(group)
        base["source_rows"] = ";".join(
            str(int(x)) for x in group["_input_row"].tolist()
        )
        if time_column is not None:
            # Keep all measurements for a parent on one side of a temporal boundary. The latest
            # source timestamp is conservative: aggregates that use a later label cannot enter an
            # earlier training block.
            base["_time_value"] = group["_time_value"].max()
        if task == "regression":
            values = group["target"].astype(float).to_numpy()
            spread = float(np.max(values) - np.min(values)) if len(values) else 0.0
            if spread > 0:
                conflict_groups += 1
            if conflict_policy == "drop" and spread > 0:
                dropped_conflict_groups += 1
                continue
            base["target"] = float(np.median(values))
            base["replicate_min"] = float(np.min(values))
            base["replicate_max"] = float(np.max(values))
            base["replicate_spread"] = spread
        else:
            counts = group["target"].astype(str).value_counts()
            if len(counts) > 1:
                conflict_groups += 1
                if conflict_policy == "drop":
                    dropped_conflict_groups += 1
                    continue
                if len(counts) > 1 and counts.iloc[0] == counts.iloc[1]:
                    dropped_conflict_groups += 1
                    continue
            base["target"] = str(counts.index[0])
            base["label_count"] = int(counts.iloc[0])
        aggregated.append(base)

    curated = pd.DataFrame(aggregated).reset_index(drop=True)
    if curated.empty:
        raise SystemExit("No molecules remained after duplicate/conflict handling.")

    class_counts: dict[str, int] | None = None
    response_summary: dict[str, float] | None = None
    if task == "classification":
        class_counts = {
            str(label): int(count)
            for label, count in curated["target"].value_counts().sort_index().items()
        }
        if len(class_counts) < 2:
            raise SystemExit(
                f"Classification requires at least two classes; found {class_counts}."
            )
    else:
        values = curated["target"].astype(float)
        response_summary = {
            "min": float(values.min()),
            "max": float(values.max()),
            "mean": float(values.mean()),
            "median": float(values.median()),
            "std": float(values.std(ddof=1)) if len(values) > 1 else 0.0,
        }

    audit = {
        "tool_version": TOOL_VERSION,
        "created_at": utc_now(),
        "input_rows": len(frame),
        "missing_or_non_numeric_target_rows": int(missing_target),
        "invalid_structure_rows": int(len(frame) - missing_target - len(parsed)),
        "invalid_structure_examples": invalid_examples,
        "parsed_labeled_rows": len(parsed),
        "unique_standardized_parents_before_conflict_policy": int(
            parsed["canonical_smiles"].nunique()
        ),
        "duplicate_rows_collapsed": duplicate_rows,
        "conflicting_parent_groups": int(conflict_groups),
        "conflicting_parent_groups_dropped": int(dropped_conflict_groups),
        "final_modeling_rows": len(curated),
        "unique_scaffolds": int(curated["scaffold"].nunique()),
        "task": task,
        "class_counts": class_counts,
        "response_summary": response_summary,
        "standardization": {
            "cleanup": True,
            "largest_fragment": True,
            "uncharge": bool(uncharge),
            "tautomer_canonicalize": bool(tautomer_canonicalize),
            "isomeric_canonical_smiles": True,
        },
        "conflict_policy": conflict_policy,
        "temporal_parent_assignment": (
            "latest_source_timestamp" if time_column is not None else None
        ),
    }
    return curated, audit


def write_audit_outputs(
    output_dir: Path, curated: pd.DataFrame, audit: dict[str, Any]
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    curated.to_csv(output_dir / "curated_data.csv", index=False)
    write_json(output_dir / "data_audit.json", audit)


def molecules_from_canonical(smiles_values: Iterable[str]) -> list[Any]:
    require_rdkit()
    molecules = [Chem.MolFromSmiles(str(smiles)) for smiles in smiles_values]
    if any(mol is None for mol in molecules):
        raise RuntimeError(
            "A canonical SMILES unexpectedly failed to parse during featurization."
        )
    return molecules


def descriptor_vector(mol: Any) -> list[float]:
    return [
        float(Descriptors.MolWt(mol)),
        float(Crippen.MolLogP(mol)),
        float(Descriptors.TPSA(mol)),
        float(Lipinski.NumHDonors(mol)),
        float(Lipinski.NumHAcceptors(mol)),
        float(Lipinski.NumRotatableBonds(mol)),
        float(Lipinski.RingCount(mol)),
        float(Lipinski.NumAromaticRings(mol)),
        float(Lipinski.FractionCSP3(mol)),
        float(Descriptors.HeavyAtomCount(mol)),
        float(Chem.GetFormalCharge(mol)),
        float(QED.qed(mol)),
    ]


def featurize_molecules(
    molecules: Sequence[Any], *, fp_radius: int, fp_bits: int
) -> tuple[np.ndarray, list[Any], list[str]]:
    require_rdkit()
    generator = rdFingerprintGenerator.GetMorganGenerator(
        radius=fp_radius, fpSize=fp_bits
    )
    features = np.zeros(
        (len(molecules), fp_bits + len(DESCRIPTOR_NAMES)), dtype=np.float32
    )
    fingerprints: list[Any] = []
    for row_index, mol in enumerate(molecules):
        fp = generator.GetFingerprint(mol)
        fingerprints.append(fp)
        arr = np.zeros((fp_bits,), dtype=np.float32)
        DataStructs.ConvertToNumpyArray(fp, arr)
        features[row_index, :fp_bits] = arr
        features[row_index, fp_bits:] = np.asarray(
            descriptor_vector(mol), dtype=np.float32
        )
    names = [f"MorganBit_{i}" for i in range(fp_bits)] + DESCRIPTOR_NAMES
    return features, fingerprints, names


def encode_class_labels(
    labels: Sequence[Any], positive_label: str | None
) -> tuple[np.ndarray, list[str]]:
    normalized = np.asarray([safe_label(value) for value in labels], dtype=object)
    classes = sorted(set(normalized.tolist()))
    if len(classes) < 2:
        raise SystemExit("Classification requires at least two classes after curation.")
    if positive_label is not None:
        positive = safe_label(positive_label)
        if positive not in classes:
            raise SystemExit(
                f"Requested positive label {positive!r} not found. Classes: {classes}"
            )
        if len(classes) != 2:
            raise SystemExit(
                "--positive-label is supported only for binary classification."
            )
        negative = next(label for label in classes if label != positive)
        classes = [negative, positive]
    mapping = {label: index for index, label in enumerate(classes)}
    encoded = np.asarray([mapping[label] for label in normalized], dtype=int)
    return encoded, classes


def decode_class_labels(values: Sequence[int], classes: Sequence[str]) -> list[str]:
    return [str(classes[int(value)]) for value in values]


def choose_scaffold_split(
    y: np.ndarray,
    groups: np.ndarray,
    *,
    test_size: float,
    seed: int,
    classification: bool,
) -> tuple[np.ndarray, np.ndarray]:
    """Choose a deterministic group split close to requested size and prevalence."""
    best: tuple[float, np.ndarray, np.ndarray] | None = None
    unique_groups = len(set(groups.tolist()))
    if unique_groups < 2:
        raise SystemExit(
            "Scaffold split requires at least two distinct scaffold groups."
        )
    attempts = min(200, max(20, unique_groups * 4))
    for offset in range(attempts):
        splitter = GroupShuffleSplit(
            n_splits=1, test_size=test_size, random_state=seed + offset
        )
        train_idx, test_idx = next(splitter.split(np.zeros(len(y)), y, groups))
        if len(train_idx) == 0 or len(test_idx) == 0:
            continue
        if classification:
            if len(np.unique(y[train_idx])) < len(np.unique(y)):
                continue
            if len(np.unique(y[test_idx])) < len(np.unique(y)):
                continue
            total_dist = np.bincount(y, minlength=int(np.max(y)) + 1) / len(y)
            test_dist = np.bincount(y[test_idx], minlength=len(total_dist)) / len(
                test_idx
            )
            prevalence_penalty = float(np.abs(total_dist - test_dist).sum())
        else:
            prevalence_penalty = abs(
                float(np.mean(y[train_idx]) - np.mean(y[test_idx]))
            ) / (float(np.std(y)) + 1e-12)
        size_penalty = abs(len(test_idx) / len(y) - test_size)
        score = size_penalty + prevalence_penalty
        if best is None or score < best[0]:
            best = (score, train_idx, test_idx)
    if best is None:
        raise SystemExit(
            "Could not construct a scaffold split containing all classes. Consider a larger "
            "dataset, a cluster/series design, or a different predefined external test."
        )
    return best[1], best[2]


def make_outer_split(
    curated: pd.DataFrame,
    y: np.ndarray,
    *,
    split: str,
    test_size: float,
    seed: int,
    time_values: pd.Series | None,
) -> tuple[np.ndarray, np.ndarray, pd.DataFrame]:
    positions = np.arange(len(curated))
    classification = not np.issubdtype(y.dtype, np.floating)
    working = curated.copy().reset_index(drop=True)

    if split == "random":
        stratify = y if classification else None
        train_idx, test_idx = train_test_split(
            positions,
            test_size=test_size,
            random_state=seed,
            stratify=stratify,
        )
    elif split == "scaffold":
        groups = working["scaffold"].astype(str).to_numpy()
        train_idx, test_idx = choose_scaffold_split(
            y,
            groups,
            test_size=test_size,
            seed=seed,
            classification=classification,
        )
    elif split == "time":
        if time_values is None:
            raise SystemExit("Time split requires --time-column.")
        parsed_time = pd.to_datetime(time_values, errors="coerce", utc=True)
        if parsed_time.isna().any():
            bad = int(parsed_time.isna().sum())
            raise SystemExit(
                f"Time column contains {bad} missing or unparseable value(s)."
            )
        order = np.argsort(parsed_time.to_numpy())
        cutoff = max(1, min(len(order) - 1, round(len(order) * (1 - test_size))))
        train_idx = order[:cutoff]
        test_idx = order[cutoff:]
        if classification and (
            len(np.unique(y[train_idx])) < len(np.unique(y))
            or len(np.unique(y[test_idx])) < len(np.unique(y))
        ):
            raise SystemExit(
                "Temporal split does not contain every class in train and test. Do not silently "
                "change the cutoff after consulting model results; revise the endpoint/design."
            )
    else:  # pragma: no cover - guarded by argparse
        raise ValueError(f"Unknown split: {split}")

    assignments = working[
        ["_input_row", "canonical_smiles", "scaffold", "target", "source_row_count"]
    ].copy()
    if split == "time" and time_values is not None:
        assignments["latest_source_timestamp"] = pd.to_datetime(
            time_values, errors="coerce", utc=True
        ).astype(str)
    assignments["split"] = "train"
    assignments.loc[test_idx, "split"] = "test"
    return np.asarray(train_idx), np.asarray(test_idx), assignments


def effective_cv_folds(y: np.ndarray, requested: int, classification: bool) -> int:
    folds = min(requested, len(y))
    if classification:
        counts = np.bincount(y)
        folds = min(folds, int(counts.min()))
    if folds < 2:
        raise SystemExit(
            "At least two examples per validation unit/class are required for CV."
        )
    return folds


def make_inner_cv(
    *,
    split: str,
    y_train: np.ndarray,
    groups_train: np.ndarray | None,
    requested_folds: int,
    seed: int,
    classification: bool,
) -> tuple[Any, np.ndarray | None]:
    """Construct inner CV that preserves the outer split's leakage assumptions.

    Grouped and temporal classification can yield folds with a missing class even when the full
    training set is balanced. Such folds make fitting or probability metrics invalid. We therefore
    reduce the fold count when possible and require every retained train/validation fold to contain
    every class rather than allowing GridSearchCV to turn failures into silent NaN scores.
    """
    folds = effective_cv_folds(y_train, requested_folds, classification)
    all_classes = set(np.unique(y_train).tolist())

    if split == "scaffold":
        if groups_train is None:
            raise RuntimeError("Missing scaffold groups for grouped validation.")
        group_count = len(set(groups_train.tolist()))
        folds = min(folds, group_count)
        if folds < 2:
            raise SystemExit(
                "At least two training scaffold groups are required for CV."
            )
        if not classification:
            return GroupKFold(n_splits=folds), groups_train
        for candidate_folds in range(folds, 1, -1):
            splitter = StratifiedGroupKFold(
                n_splits=candidate_folds, shuffle=True, random_state=seed
            )
            split_list = list(
                splitter.split(np.zeros(len(y_train)), y_train, groups_train)
            )
            if all(
                set(np.unique(y_train[train_fold]).tolist()) == all_classes
                and set(np.unique(y_train[valid_fold]).tolist()) == all_classes
                for train_fold, valid_fold in split_list
            ):
                return split_list, None
        raise SystemExit(
            "Could not construct grouped inner CV with every class in every training and "
            "validation fold. Add scaffold-diverse examples or use a predefined design."
        )

    if split == "time":
        folds = min(folds, len(y_train) - 1)
        if folds < 2:
            raise SystemExit(
                "Temporal inner CV requires at least three chronological records."
            )
        if not classification:
            return TimeSeriesSplit(n_splits=folds), None
        for candidate_folds in range(folds, 1, -1):
            raw_splits = list(TimeSeriesSplit(n_splits=candidate_folds).split(y_train))
            valid_splits = [
                (train_fold, valid_fold)
                for train_fold, valid_fold in raw_splits
                if set(np.unique(y_train[train_fold]).tolist()) == all_classes
                and set(np.unique(y_train[valid_fold]).tolist()) == all_classes
            ]
            if len(valid_splits) >= 2:
                return valid_splits, None
        raise SystemExit(
            "Could not construct at least two forward-chaining inner folds with every class in "
            "both training and validation. Add chronologically distributed examples or revise "
            "the endpoint/design."
        )

    if classification:
        return StratifiedKFold(n_splits=folds, shuffle=True, random_state=seed), None
    return KFold(n_splits=folds, shuffle=True, random_state=seed), None


def build_model_specs(
    task: str,
    requested_models: Sequence[str],
    *,
    seed: int,
    n_jobs: int,
    fast: bool,
    class_count: int,
) -> tuple[list[ModelSpec], list[str]]:
    specs: list[ModelSpec] = []
    notices: list[str] = []
    classification = task == "classification"

    for name in requested_models:
        if name == "rf":
            if classification:
                estimator = RandomForestClassifier(
                    n_estimators=600,
                    random_state=seed,
                    n_jobs=n_jobs,
                    class_weight="balanced_subsample",
                )
            else:
                estimator = RandomForestRegressor(
                    n_estimators=600, random_state=seed, n_jobs=n_jobs
                )
            grid = (
                {"max_features": ["sqrt"], "min_samples_leaf": [1, 3]}
                if fast
                else {
                    "max_features": ["sqrt", 0.25, 0.5],
                    "min_samples_leaf": [1, 2, 5, 10],
                    "max_depth": [None, 12, 24],
                }
            )
            specs.append(ModelSpec("random_forest", estimator, grid))

        elif name == "svm":
            if classification:
                estimator = Pipeline(
                    [
                        ("scale", StandardScaler(with_mean=False)),
                        (
                            "model",
                            SVC(
                                probability=True,
                                class_weight="balanced",
                                random_state=seed,
                            ),
                        ),
                    ]
                )
                grid = (
                    {"model__kernel": ["linear", "rbf"], "model__C": [1.0]}
                    if fast
                    else {
                        "model__kernel": ["linear", "rbf"],
                        "model__C": [0.1, 1.0, 10.0, 100.0],
                        "model__gamma": ["scale", 0.001, 0.01, 0.1],
                    }
                )
            else:
                estimator = Pipeline(
                    [("scale", StandardScaler(with_mean=False)), ("model", SVR())]
                )
                grid = (
                    {
                        "model__kernel": ["linear", "rbf"],
                        "model__C": [1.0],
                        "model__epsilon": [0.1],
                    }
                    if fast
                    else {
                        "model__kernel": ["linear", "rbf"],
                        "model__C": [0.1, 1.0, 10.0, 100.0],
                        "model__gamma": ["scale", 0.001, 0.01, 0.1],
                        "model__epsilon": [0.05, 0.1, 0.25],
                    }
                )
            specs.append(ModelSpec("svm" if classification else "svr", estimator, grid))

        elif name == "gb":
            if classification:
                estimator = GradientBoostingClassifier(random_state=seed)
            else:
                estimator = GradientBoostingRegressor(random_state=seed)
            grid = (
                {
                    "n_estimators": [120],
                    "learning_rate": [0.05],
                    "max_depth": [2],
                }
                if fast
                else {
                    "n_estimators": [100, 300, 600],
                    "learning_rate": [0.03, 0.07, 0.15],
                    "max_depth": [1, 2, 3],
                    "subsample": [0.7, 1.0],
                    "min_samples_leaf": [2, 5, 10],
                }
            )
            specs.append(ModelSpec("gradient_boosting", estimator, grid))

        elif name == "xgb":
            try:
                from xgboost import XGBClassifier, XGBRegressor  # type: ignore
            except ImportError:
                notices.append(
                    "XGBoost was requested but is not installed; xgb was skipped. Install "
                    "`xgboost` and rerun. Classical GradientBoosting is not being renamed XGBoost."
                )
                continue
            common = {
                "n_estimators": 400,
                "learning_rate": 0.05,
                "max_depth": 4,
                "subsample": 0.8,
                "colsample_bytree": 0.8,
                "reg_lambda": 1.0,
                "random_state": seed,
                "n_jobs": n_jobs,
            }
            if classification:
                objective = "binary:logistic" if class_count == 2 else "multi:softprob"
                estimator = XGBClassifier(
                    **common,
                    objective=objective,
                    eval_metric="logloss" if class_count == 2 else "mlogloss",
                )
            else:
                estimator = XGBRegressor(
                    **common, objective="reg:squarederror", eval_metric="mae"
                )
            grid = (
                {
                    "n_estimators": [200],
                    "max_depth": [3],
                    "learning_rate": [0.05],
                }
                if fast
                else {
                    "n_estimators": [200, 500, 900],
                    "max_depth": [3, 5, 8],
                    "learning_rate": [0.02, 0.06, 0.15],
                    "subsample": [0.6, 0.85, 1.0],
                    "colsample_bytree": [0.5, 0.8, 1.0],
                    "min_child_weight": [1, 5, 15],
                    "reg_lambda": [0.1, 1.0, 10.0],
                }
            )
            specs.append(ModelSpec("xgboost", estimator, grid))
        else:  # pragma: no cover - guarded by argparse
            raise ValueError(f"Unknown model name: {name}")

    if not specs:
        raise SystemExit("No runnable model remained after dependency checks.")
    return specs, notices


def prediction_scores(
    model: Any, X: np.ndarray
) -> tuple[np.ndarray | None, np.ndarray | None]:
    probabilities: np.ndarray | None = None
    decisions: np.ndarray | None = None
    if hasattr(model, "predict_proba"):
        probabilities = np.asarray(model.predict_proba(X))
    if hasattr(model, "decision_function"):
        decisions = np.asarray(model.decision_function(X))
    return probabilities, decisions


def classification_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    probabilities: np.ndarray | None,
    decisions: np.ndarray | None,
) -> dict[str, float | None]:
    classes = np.unique(y_true)
    result: dict[str, float | None] = {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
        "mcc": float(matthews_corrcoef(y_true, y_pred)),
        "f1_weighted": float(f1_score(y_true, y_pred, average="weighted")),
        "roc_auc": None,
        "average_precision": None,
        "brier_score": None,
    }
    try:
        if len(classes) == 2:
            score = (
                probabilities[:, 1]
                if probabilities is not None and probabilities.ndim == 2
                else decisions
            )
            if score is not None:
                score = np.asarray(score).reshape(-1)
                result["roc_auc"] = float(roc_auc_score(y_true, score))
                result["average_precision"] = float(
                    average_precision_score(y_true, score)
                )
                if probabilities is not None:
                    result["brier_score"] = float(brier_score_loss(y_true, score))
        elif probabilities is not None and probabilities.ndim == 2:
            result["roc_auc"] = float(
                roc_auc_score(
                    y_true, probabilities, multi_class="ovr", average="weighted"
                )
            )
            binary = label_binarize(y_true, classes=sorted(classes.tolist()))
            result["average_precision"] = float(
                average_precision_score(binary, probabilities, average="weighted")
            )
    except ValueError:
        pass
    return result


def regression_metrics(
    y_true: np.ndarray, y_pred: np.ndarray
) -> dict[str, float | None]:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    r2_value: float | None = None
    spearman_value: float | None = None
    if len(y_true) >= 2 and float(np.std(y_true)) > 0:
        candidate_r2 = float(r2_score(y_true, y_pred))
        r2_value = candidate_r2 if math.isfinite(candidate_r2) else None
        if float(np.std(y_pred)) > 0:
            candidate_spearman = float(
                pd.Series(y_true).corr(pd.Series(y_pred), method="spearman")
            )
            spearman_value = (
                candidate_spearman if math.isfinite(candidate_spearman) else None
            )
    return {
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "rmse": float(math.sqrt(mean_squared_error(y_true, y_pred))),
        "r2": r2_value,
        "spearman": spearman_value,
    }


def nearest_training_neighbors(
    query_fps: Sequence[Any], train_fps: Sequence[Any]
) -> tuple[np.ndarray, np.ndarray]:
    if not train_fps:
        raise RuntimeError("Training fingerprint collection is empty.")
    similarities = np.zeros(len(query_fps), dtype=float)
    indices = np.zeros(len(query_fps), dtype=int)
    for i, fp in enumerate(query_fps):
        values = np.asarray(DataStructs.BulkTanimotoSimilarity(fp, list(train_fps)))
        nearest = int(np.argmax(values))
        similarities[i] = float(values[nearest])
        indices[i] = nearest
    return similarities, indices


def estimate_domain_threshold(
    train_fps: Sequence[Any], *, seed: int, max_sample: int = 800
) -> float:
    """Fifth percentile of leave-one-out nearest-neighbor similarity in a capped sample."""
    if len(train_fps) < 3:
        return 0.0
    rng = np.random.default_rng(seed)
    if len(train_fps) > max_sample:
        sample_idx = np.sort(rng.choice(len(train_fps), size=max_sample, replace=False))
    else:
        sample_idx = np.arange(len(train_fps))
    sample = [train_fps[int(i)] for i in sample_idx]
    maxima: list[float] = []
    for i, fp in enumerate(sample):
        values = np.asarray(DataStructs.BulkTanimotoSimilarity(fp, sample), dtype=float)
        values[i] = -1.0
        maxima.append(float(np.max(values)))
    return float(np.percentile(maxima, 5.0))


def evaluate_nearest_neighbor_baseline(
    *,
    task: str,
    y_train: np.ndarray,
    y_test: np.ndarray,
    train_fps: Sequence[Any],
    test_fps: Sequence[Any],
) -> tuple[dict[str, Any], np.ndarray, np.ndarray]:
    similarities, indices = nearest_training_neighbors(test_fps, train_fps)
    predictions = y_train[indices]
    if task == "classification":
        metrics = classification_metrics(y_test, predictions.astype(int), None, None)
    else:
        metrics = regression_metrics(y_test.astype(float), predictions.astype(float))
    metrics["mean_nearest_similarity"] = float(np.mean(similarities))
    metrics["median_nearest_similarity"] = float(np.median(similarities))
    return metrics, predictions, similarities


def evaluate_constant_baseline(
    task: str, y_train: np.ndarray, y_test: np.ndarray
) -> dict[str, Any]:
    if task == "classification":
        values, counts = np.unique(y_train, return_counts=True)
        majority = int(values[int(np.argmax(counts))])
        prediction = np.full_like(y_test, majority)
        return classification_metrics(y_test, prediction, None, None)
    median = float(np.median(y_train))
    prediction = np.full(y_test.shape, median, dtype=float)
    return regression_metrics(y_test.astype(float), prediction)


def extract_feature_importance(
    model: Any, feature_names: Sequence[str]
) -> pd.DataFrame:
    estimator = model
    if isinstance(model, CalibratedClassifierCV):
        return pd.DataFrame(columns=["feature", "importance"])
    if isinstance(estimator, Pipeline):
        estimator = estimator.named_steps.get("model", estimator)
    values: np.ndarray | None = None
    if hasattr(estimator, "feature_importances_"):
        values = np.asarray(estimator.feature_importances_, dtype=float)
    elif hasattr(estimator, "coef_"):
        coef = np.asarray(estimator.coef_, dtype=float)
        if coef.ndim == 1:
            values = np.abs(coef)
        elif coef.shape[0] == 1:
            values = np.abs(coef[0])
        else:
            values = np.mean(np.abs(coef), axis=0)
    if values is None or len(values) != len(feature_names):
        return pd.DataFrame(columns=["feature", "importance"])
    frame = pd.DataFrame({"feature": list(feature_names), "importance": values})
    return frame.sort_values("importance", ascending=False).reset_index(drop=True)


def sanitize_probability_label(label: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "_", label).strip("_")
    return cleaned[:80] or "class"


def write_model_card(
    path: Path,
    *,
    task: str,
    target_column: str,
    split: str,
    train_size: int,
    test_size: int,
    class_names: Sequence[str] | None,
    winner_name: str,
    best_params: dict[str, Any],
    holdout_metrics: dict[str, Any],
    ad_threshold: float,
    audit: dict[str, Any],
    input_sha256: str,
    notices: Sequence[str],
) -> None:
    class_text = ", ".join(class_names) if class_names is not None else "not applicable"
    notice_text = "\n".join(f"- {item}" for item in notices) if notices else "- None"
    metrics_text = "\n".join(
        f"- **{key}:** {value}" for key, value in holdout_metrics.items()
    )
    params_text = json.dumps(best_params, indent=2, default=json_default)
    content = f"""# Model Card

**Created:** {utc_now()}  
**Tool version:** {TOOL_VERSION}  
**Task:** {task}  
**Response column:** `{target_column}`  
**Selected model:** `{winner_name}`

## Intended use

Prioritize molecular hypotheses within chemistry represented by the training data. Predictions
must be reviewed with applicability-domain information and prospectively tested.

## Prohibited use

Do not represent predictions as proof of binding, efficacy, selectivity, safety, mechanism, or
clinical utility. Do not use this model as the sole basis for clinical or regulatory decisions.

## Data and split

- Input SHA-256: `{input_sha256}`
- Final curated records: {audit["final_modeling_rows"]}
- Unique scaffolds: {audit["unique_scaffolds"]}
- Outer split: `{split}`
- Training records: {train_size}
- Test records: {test_size}
- Classes: {class_text}
- Structural domain threshold (nearest-training Tanimoto): {ad_threshold:.4f}

The structural threshold is not a complete mechanistic applicability domain.

## Holdout performance

{metrics_text}

## Selected hyperparameters

```json
{params_text}
```

## Curation

- Standardized parent structures and largest fragments were used.
- Duplicate parents were collapsed.
- Conflicting-label policy: `{audit["conflict_policy"]}`.
- Temporal parent assignment: `{audit.get("temporal_parent_assignment")}`.
- Invalid structure rows: {audit["invalid_structure_rows"]}.
- Conflicting parent groups: {audit["conflicting_parent_groups"]}.

## Dependency notices

{notice_text}

## Known limitations

- The model is sensitive to assay quality and endpoint consistency.
- Random and scaffold splits can overestimate prospective chemical novelty.
- Tree models extrapolate poorly beyond observed response/feature regions.
- SVM probabilities and tree probabilities require calibration checks.
- Feature importance is associative and may be unstable under correlated descriptors.
- The model has no prospective evidence unless such results are added separately.

## Reproducibility artifacts

Use `metrics.json`, `data_audit.json`, `split_assignments.csv`,
`test_predictions.csv`, and the environment/package versions stored in the model bundle.
"""
    path.write_text(content, encoding="utf-8")


def run_audit(args: argparse.Namespace) -> int:
    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    ensure_no_output_overwrite(
        [input_path],
        [output_dir / "curated_data.csv", output_dir / "data_audit.json"],
    )
    frame = read_csv_checked(input_path, [args.smiles_column, args.target_column])
    curated, audit = curate_labeled_dataframe(
        frame,
        smiles_column=args.smiles_column,
        target_column=args.target_column,
        task=args.task,
        uncharge=not args.keep_charges,
        tautomer_canonicalize=args.tautomer_canonicalize,
        conflict_policy=args.conflict_policy,
    )
    audit["input_path"] = str(input_path)
    audit["input_sha256"] = file_sha256(input_path)
    write_audit_outputs(output_dir, curated, audit)
    print(json.dumps(audit, indent=2, default=json_default))
    print(f"Audit written to {output_dir}")
    return 0


def materialize_cv_splits(
    cv: Any,
    X: np.ndarray,
    y: np.ndarray,
    groups: np.ndarray | None,
) -> list[tuple[np.ndarray, np.ndarray]]:
    """Return reusable split indices from either a splitter or an explicit split iterable."""
    if hasattr(cv, "split"):
        generated = cv.split(X, y, groups) if groups is not None else cv.split(X, y)
        return [(np.asarray(train), np.asarray(valid)) for train, valid in generated]
    return [(np.asarray(train), np.asarray(valid)) for train, valid in cv]


def run_train(args: argparse.Namespace) -> int:
    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    artifact_names = [
        "model.joblib",
        "metrics.json",
        "test_predictions.csv",
        "split_assignments.csv",
        "data_audit.json",
        "curated_data.csv",
        "feature_importance.csv",
        "model_card.md",
    ]
    ensure_no_output_overwrite(
        [input_path], [output_dir / name for name in artifact_names]
    )
    if args.split == "time" and args.time_column is None:
        raise SystemExit("--split time requires --time-column.")
    required_columns = [args.smiles_column, args.target_column]
    if args.split == "time" and args.time_column is not None:
        required_columns.append(args.time_column)
    frame = read_csv_checked(input_path, required_columns)
    curated, audit = curate_labeled_dataframe(
        frame,
        smiles_column=args.smiles_column,
        target_column=args.target_column,
        task=args.task,
        uncharge=not args.keep_charges,
        tautomer_canonicalize=args.tautomer_canonicalize,
        conflict_policy=args.conflict_policy,
        time_column=args.time_column if args.split == "time" else None,
    )

    if args.task == "classification":
        y, class_names = encode_class_labels(
            curated["target"].tolist(), args.positive_label
        )
    else:
        y = curated["target"].astype(float).to_numpy()
        class_names = None

    time_values: pd.Series | None = None
    if args.split == "time":
        time_values = curated["_time_value"]

    molecules = molecules_from_canonical(curated["canonical_smiles"].tolist())
    X, fingerprints, feature_names = featurize_molecules(
        molecules, fp_radius=args.fp_radius, fp_bits=args.fp_bits
    )
    train_idx, test_idx, assignments = make_outer_split(
        curated,
        y,
        split=args.split,
        test_size=args.test_size,
        seed=args.seed,
        time_values=time_values,
    )
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    train_fps = [fingerprints[int(i)] for i in train_idx]
    test_fps = [fingerprints[int(i)] for i in test_idx]
    groups_train = (
        curated.iloc[train_idx]["scaffold"].astype(str).to_numpy()
        if args.split == "scaffold"
        else None
    )
    classification = args.task == "classification"
    cv, cv_groups = make_inner_cv(
        split=args.split,
        y_train=y_train,
        groups_train=groups_train,
        requested_folds=args.cv_folds,
        seed=args.seed,
        classification=classification,
    )
    inner_cv_fold_count = len(materialize_cv_splits(cv, X_train, y_train, cv_groups))
    scoring = (
        "average_precision"
        if classification and len(np.unique(y_train)) == 2
        else "f1_weighted"
        if classification
        else "neg_mean_absolute_error"
    )

    specs, notices = build_model_specs(
        args.task,
        args.models,
        seed=args.seed,
        n_jobs=args.n_jobs,
        fast=args.fast,
        class_count=len(np.unique(y_train)) if classification else 0,
    )

    results: dict[str, Any] = {}
    fitted: dict[str, Any] = {}
    for spec in specs:
        print(f"Training {spec.name} ...", flush=True)
        search = GridSearchCV(
            spec.estimator,
            spec.param_grid,
            scoring=scoring,
            cv=cv,
            n_jobs=args.n_jobs,
            refit=True,
            error_score=np.nan,
            return_train_score=False,
        )
        fit_kwargs: dict[str, Any] = {}
        if cv_groups is not None:
            fit_kwargs["groups"] = cv_groups
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            search.fit(X_train, y_train, **fit_kwargs)
        if not np.isfinite(search.best_score_):
            notices.append(
                f"{spec.name} produced no finite inner-CV score and was omitted."
            )
            continue
        model = search.best_estimator_
        calibration_applied = False
        if classification and args.calibrate:
            split_list = materialize_cv_splits(cv, X_train, y_train, cv_groups)
            calibrated = CalibratedClassifierCV(
                estimator=clone(model), method=args.calibration_method, cv=split_list
            )
            try:
                calibrated.fit(X_train, y_train)
                model = calibrated
                calibration_applied = True
            except (TypeError, ValueError) as exc:
                message = re.sub(r"\s+", " ", str(exc)).strip()[:300]
                notices.append(
                    f"{spec.name} calibration was not applied ({type(exc).__name__}: "
                    f"{message}); the tuned uncalibrated estimator was retained."
                )
        predictions = np.asarray(model.predict(X_test))
        probabilities, decisions = prediction_scores(model, X_test)
        if classification:
            holdout = classification_metrics(
                y_test.astype(int), predictions.astype(int), probabilities, decisions
            )
        else:
            holdout = regression_metrics(
                y_test.astype(float), predictions.astype(float)
            )
        results[spec.name] = {
            "inner_cv_scoring": scoring,
            "inner_cv_folds": inner_cv_fold_count,
            "inner_cv_best_score": float(search.best_score_),
            "best_params": search.best_params_,
            "calibration_requested": bool(classification and args.calibrate),
            "calibration_applied": calibration_applied,
            "calibration_method": (
                args.calibration_method if calibration_applied else None
            ),
            "holdout_metrics": holdout,
        }
        fitted[spec.name] = model

    if not fitted:
        raise SystemExit(
            "Every requested model failed. Inspect data, class counts, and CV design."
        )

    # Select only by inner-CV score. The frozen holdout does not choose the winner.
    winner_name = max(results, key=lambda key: results[key]["inner_cv_best_score"])
    winner = fitted[winner_name]

    constant_metrics = evaluate_constant_baseline(args.task, y_train, y_test)
    nn_metrics, _, nn_similarities = evaluate_nearest_neighbor_baseline(
        task=args.task,
        y_train=y_train,
        y_test=y_test,
        train_fps=train_fps,
        test_fps=test_fps,
    )
    ad_threshold = (
        float(args.ad_threshold)
        if args.ad_threshold is not None
        else estimate_domain_threshold(train_fps, seed=args.seed)
    )
    nearest_similarities, nearest_indices = nearest_training_neighbors(
        test_fps, train_fps
    )
    winner_predictions = np.asarray(winner.predict(X_test))
    winner_probabilities, winner_decisions = prediction_scores(winner, X_test)

    output_dir.mkdir(parents=True, exist_ok=True)
    input_digest = file_sha256(input_path)
    audit["input_path"] = str(input_path)
    audit["input_sha256"] = input_digest
    write_audit_outputs(output_dir, curated, audit)
    assignments.to_csv(output_dir / "split_assignments.csv", index=False)

    test_output = curated.iloc[test_idx][
        ["_input_row", "input_smiles", "canonical_smiles", "scaffold", "target"]
    ].reset_index(drop=True)
    if classification:
        test_output["actual_label"] = decode_class_labels(
            y_test.astype(int), class_names or []
        )
        test_output["predicted_label"] = decode_class_labels(
            winner_predictions.astype(int), class_names or []
        )
        if winner_probabilities is not None and winner_probabilities.ndim == 2:
            for class_index, label in enumerate(class_names or []):
                test_output[
                    f"probability_{class_index}_{sanitize_probability_label(label)}"
                ] = winner_probabilities[:, class_index]
            if winner_probabilities.shape[1] == 2:
                test_output["positive_probability"] = winner_probabilities[:, 1]
        elif winner_decisions is not None:
            test_output["decision_score"] = np.asarray(winner_decisions).reshape(-1)
    else:
        test_output["actual_value"] = y_test.astype(float)
        test_output["predicted_value"] = winner_predictions.astype(float)
        test_output["residual"] = y_test.astype(float) - winner_predictions.astype(
            float
        )
    test_output["nearest_training_similarity"] = nearest_similarities
    test_output["nearest_training_index"] = nearest_indices
    test_output["applicability_domain"] = np.where(
        nearest_similarities >= ad_threshold, "in_domain", "out_of_domain"
    )
    test_output.to_csv(output_dir / "test_predictions.csv", index=False)

    importance = extract_feature_importance(winner, feature_names)
    importance.to_csv(output_dir / "feature_importance.csv", index=False)

    environment = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "scikit_learn": sklearn.__version__,
        "rdkit": getattr(rdBase, "rdkitVersion", "unknown"),
        "joblib": getattr(joblib, "__version__", "unknown"),
    }
    bundle = {
        "bundle_type": "classical_ml_drug_discovery_qsar",
        "tool_version": TOOL_VERSION,
        "created_at": utc_now(),
        "task": args.task,
        "model_name": winner_name,
        "model": winner,
        "class_names": class_names,
        "positive_label": class_names[1]
        if class_names and len(class_names) == 2
        else None,
        "feature_spec": {
            "type": "morgan_bits_plus_rdkit_descriptors",
            "fp_radius": int(args.fp_radius),
            "fp_bits": int(args.fp_bits),
            "descriptor_names": DESCRIPTOR_NAMES,
            "feature_names": feature_names,
        },
        "standardization": audit["standardization"],
        "ad_threshold": float(ad_threshold),
        "training_smiles": curated.iloc[train_idx]["canonical_smiles"].tolist(),
        "training_targets": y_train.tolist(),
        "winner_inner_cv_score": results[winner_name]["inner_cv_best_score"],
        "winner_best_params": results[winner_name]["best_params"],
        "winner_holdout_metrics": results[winner_name]["holdout_metrics"],
        "input_sha256": input_digest,
        "environment": environment,
        "trusted_deserialization_warning": (
            "Only load this joblib bundle from a trusted source; pickle-compatible "
            "deserialization can execute code."
        ),
    }
    joblib.dump(bundle, output_dir / "model.joblib", compress=3)

    metrics = {
        "tool_version": TOOL_VERSION,
        "created_at": utc_now(),
        "task": args.task,
        "split": args.split,
        "test_size_fraction_requested": args.test_size,
        "train_rows": len(train_idx),
        "test_rows": len(test_idx),
        "class_names": class_names,
        "positive_label": class_names[1]
        if class_names and len(class_names) == 2
        else None,
        "selection_rule": "highest inner-CV score; holdout did not choose model",
        "winner": winner_name,
        "models": results,
        "constant_baseline_holdout": constant_metrics,
        "nearest_neighbor_baseline_holdout": nn_metrics,
        "test_similarity": {
            "mean": float(np.mean(nn_similarities)),
            "median": float(np.median(nn_similarities)),
            "min": float(np.min(nn_similarities)),
            "max": float(np.max(nn_similarities)),
        },
        "ad_threshold": float(ad_threshold),
        "test_in_domain_fraction": float(np.mean(nearest_similarities >= ad_threshold)),
        "notices": notices,
        "environment": environment,
    }
    write_json(output_dir / "metrics.json", metrics)
    write_model_card(
        output_dir / "model_card.md",
        task=args.task,
        target_column=args.target_column,
        split=args.split,
        train_size=len(train_idx),
        test_size=len(test_idx),
        class_names=class_names,
        winner_name=winner_name,
        best_params=results[winner_name]["best_params"],
        holdout_metrics=results[winner_name]["holdout_metrics"],
        ad_threshold=ad_threshold,
        audit=audit,
        input_sha256=input_digest,
        notices=notices,
    )

    print(json.dumps(metrics, indent=2, default=json_default))
    print(f"Selected {winner_name} by inner CV; artifacts written to {output_dir}")
    return 0


def prepare_prediction_frame(
    frame: pd.DataFrame,
    *,
    smiles_column: str,
    uncharge: bool,
    tautomer_canonicalize: bool,
) -> tuple[pd.DataFrame, list[Any], pd.DataFrame]:
    valid_records: list[dict[str, Any]] = []
    valid_molecules: list[Any] = []
    invalid_records: list[dict[str, Any]] = []
    for input_row, row in frame.iterrows():
        canonical, mol, error = canonicalize_smiles(
            row[smiles_column],
            uncharge=uncharge,
            tautomer_canonicalize=tautomer_canonicalize,
        )
        if error is not None:
            invalid_records.append(
                {
                    "_input_row": int(input_row),
                    "input_smiles": safe_label(row[smiles_column]),
                    "canonical_smiles": "",
                    "status": error,
                }
            )
            continue
        valid_records.append(
            {
                "_input_row": int(input_row),
                "input_smiles": safe_label(row[smiles_column]),
                "canonical_smiles": canonical,
                "status": "ok",
            }
        )
        valid_molecules.append(mol)
    return pd.DataFrame(valid_records), valid_molecules, pd.DataFrame(invalid_records)


def run_predict(args: argparse.Namespace) -> int:
    require_rdkit()
    model_path = Path(args.model).expanduser().resolve()
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    ensure_no_output_overwrite([model_path, input_path], [output_path])
    if not model_path.is_file():
        raise SystemExit(f"Model does not exist: {model_path}")
    if not args.trust_model:
        print(
            "SECURITY WARNING: joblib/pickle deserialization can execute code. Use only a model "
            "you created or trust. Pass --trust-model to confirm.",
            file=sys.stderr,
        )
        return 2
    try:
        bundle = joblib.load(model_path)
    except Exception as exc:
        raise SystemExit(f"Could not load trusted model bundle: {exc}") from exc
    if not isinstance(bundle, dict) or bundle.get("bundle_type") != (
        "classical_ml_drug_discovery_qsar"
    ):
        raise SystemExit(
            "File is not a recognized classical-ml-drug-discovery model bundle."
        )
    required_bundle_keys = {
        "model",
        "task",
        "class_names",
        "feature_spec",
        "standardization",
        "ad_threshold",
        "training_smiles",
        "model_name",
        "created_at",
    }
    missing_bundle_keys = sorted(required_bundle_keys.difference(bundle))
    if missing_bundle_keys:
        raise SystemExit(
            f"Model bundle is missing required fields: {missing_bundle_keys}"
        )

    frame = read_csv_checked(input_path, [args.smiles_column])
    standardization = bundle["standardization"]
    valid, molecules, invalid = prepare_prediction_frame(
        frame,
        smiles_column=args.smiles_column,
        uncharge=bool(standardization.get("uncharge", True)),
        tautomer_canonicalize=bool(standardization.get("tautomer_canonicalize", False)),
    )
    if valid.empty:
        output = invalid.sort_values("_input_row")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output.to_csv(output_path, index=False)
        raise SystemExit("No valid molecules were available for prediction.")

    feature_spec = bundle["feature_spec"]
    X, query_fps, _ = featurize_molecules(
        molecules,
        fp_radius=int(feature_spec["fp_radius"]),
        fp_bits=int(feature_spec["fp_bits"]),
    )
    model = bundle["model"]
    predictions = np.asarray(model.predict(X))
    probabilities, decisions = prediction_scores(model, X)
    task = bundle["task"]
    if task == "classification":
        classes = bundle["class_names"]
        valid["predicted_label"] = decode_class_labels(predictions.astype(int), classes)
        if probabilities is not None and probabilities.ndim == 2:
            for class_index, label in enumerate(classes):
                valid[
                    f"probability_{class_index}_{sanitize_probability_label(str(label))}"
                ] = probabilities[:, class_index]
            if probabilities.shape[1] == 2:
                valid["positive_probability"] = probabilities[:, 1]
        elif decisions is not None:
            valid["decision_score"] = np.asarray(decisions).reshape(-1)
    else:
        valid["predicted_value"] = predictions.astype(float)

    training_molecules = molecules_from_canonical(bundle["training_smiles"])
    _, training_fps, _ = featurize_molecules(
        training_molecules,
        fp_radius=int(feature_spec["fp_radius"]),
        fp_bits=int(feature_spec["fp_bits"]),
    )
    similarities, nearest_indices = nearest_training_neighbors(query_fps, training_fps)
    threshold = float(bundle["ad_threshold"])
    valid["nearest_training_similarity"] = similarities
    valid["nearest_training_index"] = nearest_indices
    valid["applicability_domain"] = np.where(
        similarities >= threshold, "in_domain", "out_of_domain"
    )
    valid["model_name"] = bundle["model_name"]
    valid["model_created_at"] = bundle["created_at"]

    if not invalid.empty:
        for column in valid.columns:
            if column not in invalid.columns:
                invalid[column] = np.nan
        output = pd.concat([valid, invalid[valid.columns]], ignore_index=True)
    else:
        output = valid
    output = output.sort_values("_input_row").reset_index(drop=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(output_path, index=False)
    print(
        json.dumps(
            {
                "input_rows": len(frame),
                "valid_predictions": len(valid),
                "invalid_rows": len(invalid),
                "in_domain_fraction": float(np.mean(similarities >= threshold)),
                "ad_threshold": threshold,
                "output": str(output_path),
            },
            indent=2,
        )
    )
    return 0


def add_labeled_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--input", required=True, help="Input CSV path.")
    parser.add_argument("--smiles-column", default="smiles", help="SMILES column name.")
    parser.add_argument(
        "--target-column", required=True, help="Response/label column name."
    )
    parser.add_argument(
        "--task", choices=["classification", "regression"], required=True
    )
    parser.add_argument("--output-dir", required=True, help="Output directory.")
    parser.add_argument(
        "--conflict-policy",
        choices=["drop", "aggregate"],
        default="drop",
        help=(
            "For duplicate parents with conflicting labels: drop the parent, or aggregate by "
            "median/majority (classification ties are still dropped)."
        ),
    )
    parser.add_argument(
        "--keep-charges",
        action="store_true",
        help="Do not apply RDKit Uncharger during parent standardization.",
    )
    parser.add_argument(
        "--tautomer-canonicalize",
        action="store_true",
        help="Canonicalize tautomers. Use only if scientifically appropriate for the endpoint.",
    )


# ─────────────────────────────────────────────────────────────────────────────
# Shared helpers for the advanced subcommands (analyze / conformal / ensemble /
# select / interpret). They reuse the existing bundle contract and featurizer so
# the whole CLI stays self-consistent and leakage-aware.
# ─────────────────────────────────────────────────────────────────────────────
def load_trusted_bundle(model_path: Path, trust_model: bool) -> dict[str, Any]:
    if not model_path.is_file():
        raise SystemExit(f"Model does not exist: {model_path}")
    if not trust_model:
        raise SystemExit(
            "SECURITY WARNING: joblib/pickle deserialization can execute code. "
            "Pass --trust-model to confirm the model is one you created/trust."
        )
    try:
        bundle = joblib.load(model_path)
    except Exception as exc:
        raise SystemExit(f"Could not load trusted model bundle: {exc}") from exc
    if not isinstance(bundle, dict) or bundle.get("bundle_type") != (
        "classical_ml_drug_discovery_qsar"
    ):
        raise SystemExit("File is not a recognized classical-ml-drug-discovery model bundle.")
    required = {
        "model", "task", "class_names", "feature_spec", "standardization",
        "ad_threshold", "training_smiles", "model_name", "created_at",
    }
    missing = sorted(required.difference(bundle))
    if missing:
        raise SystemExit(f"Model bundle is missing required fields: {missing}")
    return bundle


def bundle_featurize(bundle: dict[str, Any], smiles_values: list[str]) -> tuple[np.ndarray, list[Any], list[str]]:
    feats = bundle["feature_spec"]
    molecules = molecules_from_canonical(smiles_values)
    X, fps, names = featurize_molecules(
        molecules,
        fp_radius=int(feats["fp_radius"]),
        fp_bits=int(feats["fp_bits"]),
    )
    return X, fps, names


def _canonicalize_list(frame: pd.DataFrame, smiles_column: str) -> tuple[pd.DataFrame, list[Any], pd.DataFrame]:
    """Reuse prepare_prediction_frame's logic but return canonical strings for joins."""
    standardization_defaults = {"uncharge": True, "tautomer_canonicalize": False}
    valid, molecules, invalid = prepare_prediction_frame(
        frame,
        smiles_column=smiles_column,
        uncharge=bool(standardization_defaults["uncharge"]),
        tautomer_canonicalize=bool(standardization_defaults["tautomer_canonicalize"]),
    )
    return valid, molecules, invalid


# ═════════════════════════════════════════════════════════════════════════════
# analyze — dataset EDA (composition, balance, diversity, scaffold structure)
# ═════════════════════════════════════════════════════════════════════════════
def run_analyze(args: argparse.Namespace) -> int:
    require_rdkit()
    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    ensure_no_output_overwrite([input_path], [output_dir])
    if output_dir.exists() and any(output_dir.iterdir()):
        raise SystemExit(f"Output directory is not empty: {output_dir}")

    frame = read_csv_checked(input_path, [args.smiles_column])
    valid, molecules, invalid = prepare_prediction_frame(
        frame,
        smiles_column=args.smiles_column,
        uncharge=True,
        tautomer_canonicalize=False,
    )
    n_input = len(frame)
    n_valid = len(molecules)
    n_invalid = len(invalid)
    canonical_list = valid["canonical_smiles"].tolist()

    X, fps, names = featurize_molecules(molecules, fp_radius=args.fp_radius, fp_bits=args.fp_bits)
    descriptor_names = DESCRIPTOR_NAMES
    descriptor_matrix = np.asarray([descriptor_vector(m) for m in molecules], dtype=float)

    # uniqueness + duplicate families
    unique_smiles, counts = np.unique(canonical_list, return_counts=True)
    duplicate_families = int(np.sum(counts > 1))
    duplicate_rows = int(np.sum(counts[counts > 1] - 1))  # redundant rows beyond the first

    # scaffolds
    scaffolds = []
    for mol in molecules:
        try:
            scaffolds.append(scaffold_for_mol(mol))
        except Exception:
            scaffolds.append("")
    scaffold_array = np.asarray(scaffolds)
    unique_scaffolds, sc_counts = np.unique(scaffold_array[scaffold_array != ""], return_counts=True)
    scaffold_diversity = float(len(unique_scaffolds)) / float(max(1, n_valid))

    # descriptor statistics
    desc_stats = {}
    for i, name in enumerate(descriptor_names):
        col = descriptor_matrix[:, i]
        desc_stats[name] = {
            "min": float(np.nanmin(col)) if len(col) else None,
            "mean": float(np.nanmean(col)) if len(col) else None,
            "max": float(np.nanmax(col)) if len(col) else None,
            "std": float(np.nanstd(col)) if len(col) else None,
        }

    # nearest-neighbor similarity (sample for speed)
    sample_n = min(n_valid, args.sample)
    rng = np.random.default_rng(args.seed)
    if n_valid > sample_n:
        idx = np.sort(rng.choice(n_valid, size=sample_n, replace=False))
    else:
        idx = np.arange(n_valid)
    sample_fps = [fps[int(i)] for i in idx]
    nn_similarity = []
    for i, fp in enumerate(sample_fps):
        vals = np.asarray(DataStructs.BulkTanimotoSimilarity(fp, sample_fps), dtype=float)
        vals[i] = 1.0  # self
        if len(vals) > 1:
            vals[i] = -1.0
            nn_similarity.append(float(np.max(vals)))
    nn_similarity = np.asarray(nn_similarity) if nn_similarity else np.asarray([0.0])

    # target analysis (optional)
    target_summary: dict[str, Any] = {}
    if args.target_column and args.target_column in frame.columns:
        target = frame[args.target_column].astype(object)
        if args.task == "classification":
            values, counts_y = np.unique([safe_label(v) for v in target], return_counts=True)
            target_summary = {
                "classes": [str(v) for v in values],
                "counts": [int(c) for c in counts_y],
                "imbalance_ratio": float(np.max(counts_y) / max(1, np.min(counts_y))),
            }
        else:
            numeric = pd.to_numeric(target, errors="coerce").dropna()
            target_summary = {
                "min": float(numeric.min()) if len(numeric) else None,
                "mean": float(numeric.mean()) if len(numeric) else None,
                "max": float(numeric.max()) if len(numeric) else None,
                "std": float(numeric.std()) if len(numeric) else None,
                "missing": int(target.isna().sum()),
            }

    # descriptor-space PCA + clustering (cheap; fingerprint space is high-D)
    pca_coords = np.zeros((n_valid, 2))
    cluster_labels = np.zeros(n_valid, dtype=int)
    if n_valid >= 3:
        scaled = StandardScaler().fit_transform(descriptor_matrix)
        pca = PCA(n_components=min(2, scaled.shape[1]), random_state=args.seed).fit(scaled)
        pca_coords = pca.transform(scaled)
        k = max(1, min(args.n_clusters, n_valid))
        km = KMeans(n_clusters=k, n_init=3, random_state=args.seed).fit(scaled)
        cluster_labels = km.labels_

    summary = {
        "input_rows": n_input,
        "valid_rows": n_valid,
        "invalid_rows": n_invalid,
        "unique_canonical_smiles": int(len(unique_smiles)),
        "duplicate_families": duplicate_families,
        "duplicate_rows": duplicate_rows,
        "scaffold_diversity_ratio": scaffold_diversity,
        "unique_scaffold_count": int(len(unique_scaffolds)),
        "top_scaffolds": [
            {"scaffold": str(s), "count": int(c)}
            for s, c in sorted(zip(unique_scaffolds.tolist(), sc_counts.tolist()),
                               key=lambda t: -t[1])[:10]
        ],
        "nearest_neighbor_similarity": {
            "mean": float(np.mean(nn_similarity)),
            "p5": float(np.percentile(nn_similarity, 5)),
            "p50": float(np.percentile(nn_similarity, 50)),
            "p95": float(np.percentile(nn_similarity, 95)),
        },
        "descriptors": desc_stats,
        "target": target_summary,
        "feature_dim": int(X.shape[1]),
        "sampled_for_similarity": sample_n,
    }
    write_json(output_dir / "analysis.json", summary)

    rows = []
    for i in range(n_valid):
        rows.append({
            "index": i,
            "canonical_smiles": canonical_list[i],
            "scaffold": scaffolds[i],
            "cluster": int(cluster_labels[i]),
            "pca_1": float(pca_coords[i, 0]),
            "pca_2": float(pca_coords[i, 1]),
        })
    pd.DataFrame(rows).to_csv(output_dir / "dataset_layout.csv", index=False)
    if not invalid.empty:
        invalid.sort_values("_input_row").to_csv(output_dir / "invalid_rows.csv", index=False)

    print(json.dumps({
        "input_rows": n_input, "valid_rows": n_valid, "invalid_rows": n_invalid,
        "unique_canonical_smiles": int(len(unique_smiles)),
        "scaffold_diversity_ratio": round(scaffold_diversity, 3),
        "mean_nn_similarity": round(float(np.mean(nn_similarity)), 3),
        "output_dir": str(output_dir),
    }, indent=2))
    return 0


# ═════════════════════════════════════════════════════════════════════════════
# conformal — inductive (split) conformal prediction: prediction sets / intervals
# ═════════════════════════════════════════════════════════════════════════════
def conformal_ncs(task: str, model: Any, X: np.ndarray, y_true: np.ndarray, class_names: list[str]) -> np.ndarray:
    """Nonconformity scores on calibration data."""
    probabilities, decisions = prediction_scores(model, X)
    y_true = np.asarray([safe_label(v) for v in y_true], dtype=object)
    if task == "classification":
        # nonconformity = 1 - probability of the true class
        probs = probabilities if probabilities is not None else np.ones((len(y_true), len(class_names)))
        true_idx = np.asarray([class_names.index(str(v)) if str(v) in class_names else 0
                               for v in y_true], dtype=int)
        return 1.0 - probs[np.arange(len(y_true)), true_idx]
    # regression
    y_hat = np.asarray(model.predict(X), dtype=float)
    y_num = np.asarray([float(v) for v in y_true], dtype=float)
    return np.abs(y_num - y_hat)


def run_conformal(args: argparse.Namespace) -> int:
    require_rdkit()
    bundle = load_trusted_bundle(Path(args.model).expanduser().resolve(), args.trust_model)
    task = bundle["task"]
    if args.task and args.task != task:
        raise SystemExit(f"--task ({args.task}) disagrees with model bundle task ({task}).")
    calib_path = Path(args.calibration).expanduser().resolve()
    query_path = Path(args.query).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    ensure_no_output_overwrite([Path(args.model), calib_path, query_path], [output_path])

    frame = read_csv_checked(calib_path, [args.smiles_column, args.target_column])
    valid, molecules, invalid = prepare_prediction_frame(
        frame, smiles_column=args.smiles_column, uncharge=True, tautomer_canonicalize=False)
    if len(molecules) < 3:
        raise SystemExit("Conformal prediction needs at least 3 calibration molecules.")
    X_cal, fp_cal, _ = bundle_featurize(bundle, valid["canonical_smiles"].tolist())
    y_cal = frame.loc[valid["_input_row"].to_numpy(), args.target_column].tolist()

    model = bundle["model"]
    class_names = bundle["class_names"]
    ncs = conformal_ncs(task, model, X_cal, np.asarray(y_cal), class_names)
    n = len(ncs)
    alpha = float(args.alpha)
    level = min(0.999, max(0.01, 1.0 - alpha))
    # Standard inductive-conformal threshold: the (1-alpha) coverage quantile of
    # calibration nonconformity. q is 1-indexed; index q-1 in the sorted array.
    q = int(math.ceil((n + 1) * level))
    q = max(1, min(n, q))
    threshold = float(np.sort(ncs)[q - 1])

    # calibration empirical coverage (leave-one-calibration-in estimate)
    coverage = float(np.mean(ncs <= threshold))

    # query
    query_frame = read_csv_checked(query_path, [args.query_smiles_column or args.smiles_column])
    qvalid, qmols, qinvalid = prepare_prediction_frame(
        query_frame,
        smiles_column=args.query_smiles_column or args.smiles_column,
        uncharge=True, tautomer_canonicalize=False)
    if qvalid.empty:
        raise SystemExit("No valid molecules in the query set.")
    X_q, fp_q, _ = bundle_featurize(bundle, qvalid["canonical_smiles"].tolist())

    probs, decisions = prediction_scores(model, X_q)
    results = []
    if task == "classification":
        # prediction sets: include classes whose nonconformity (1 - prob) <= threshold
        pmatrix = probs if probs is not None else np.zeros((len(X_q), len(class_names)))
        for i in range(len(X_q)):
            sets = [class_names[j] for j in range(len(class_names))
                    if (1.0 - float(pmatrix[i, j])) <= threshold]
            if not sets:
                sets = [class_names[int(np.argmax(pmatrix[i]))]]
            results.append({
                "_input_row": int(qvalid.iloc[i]["_input_row"]),
                "input_smiles": qvalid.iloc[i]["input_smiles"],
                "canonical_smiles": qvalid.iloc[i]["canonical_smiles"],
                "prediction_set": " | ".join(sets),
                "set_size": len(sets),
                "set_lower": "",
                "set_upper": "",
            })
    else:
        y_hat = np.asarray(model.predict(X_q), dtype=float)
        for i in range(len(X_q)):
            results.append({
                "_input_row": int(qvalid.iloc[i]["_input_row"]),
                "input_smiles": qvalid.iloc[i]["input_smiles"],
                "canonical_smiles": qvalid.iloc[i]["canonical_smiles"],
                "prediction_set": "",
                "set_size": 0,
                "set_lower": float(y_hat[i] - threshold),
                "set_upper": float(y_hat[i] + threshold),
            })

    out = pd.DataFrame(results).sort_values("_input_row").reset_index(drop=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(output_path, index=False)
    report = {
        "task": task,
        "alpha": alpha,
        "nominal_level": level,
        "calibration_n": n,
        "nonconformity_threshold": threshold,
        "calibration_empirical_coverage": coverage,
        "query_rows": len(results),
        "output": str(output_path),
        "note": (
            "Inductive conformal guarantees marginal coverage only under "
            "exchangeability (i.i.d. or random split). Under scaffold/temporal "
            "drift coverage can degrade — treat as an uncertainty heuristic, not a "
            "safety certificate. See SKILL.md Phase 9."
        ),
    }
    write_json(output_path.with_suffix(".conformal.json"), report)
    print(json.dumps(report, indent=2))
    return 0


# ═════════════════════════════════════════════════════════════════════════════
# ensemble — consensus across prediction CSVs (score averaging + disagreement)
# ═════════════════════════════════════════════════════════════════════════════
def run_ensemble(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir).expanduser().resolve()
    inputs = [Path(p).expanduser().resolve() for p in args.predictions]
    ensure_no_output_overwrite(inputs, [output_dir])
    if output_dir.exists() and any(output_dir.iterdir()):
        raise SystemExit(f"Output directory is not empty: {output_dir}")

    frames = [pd.read_csv(p) for p in inputs]
    join_col = args.smiles_column
    score_col = args.score_column
    frames_with = []
    for name, f in zip(args.predictions, frames):
        if join_col not in f.columns:
            raise SystemExit(f"{name}: missing join column '{join_col}'.")
        if score_col not in f.columns:
            raise SystemExit(f"{name}: missing score column '{score_col}'. "
                             "Use --score-column (e.g. positive_probability or predicted_value).")
        frames_with.append((name, f))

    merged = frames_with[0][1][[join_col, score_col]].rename(columns={score_col: "score_0"})
    for i, (name, f) in enumerate(frames_with[1:], 1):
        sub = f[[join_col, score_col]].rename(columns={score_col: f"score_{i}"})
        merged = merged.merge(sub, on=join_col, how="inner")
    if merged.empty:
        raise SystemExit("No common compounds across all prediction sets.")
    score_cols = [f"score_{i}" for i in range(len(frames_with))]
    matrix = merged[score_cols].astype(float).to_numpy()
    merged["consensus_score"] = np.mean(matrix, axis=1)
    merged["consensus_std"] = np.std(matrix, axis=1)
    merged["n_models"] = matrix.shape[1]
    if args.task == "classification":
        merged["agreement_fraction"] = np.mean(matrix >= 0.5, axis=1)
    # cross-check domain: use availability from the first readable frame
    merged["consensus_rank"] = merged["consensus_score"].rank(
        ascending=False, method="min").astype(int)
    # add domain/nearest-sim if present on the first frame
    for col in ("applicability_domain", "nearest_training_similarity"):
        if col in frames_with[0][1].columns:
            merged[col] = frames_with[0][1][col].to_numpy()

    merged = merged.sort_values("consensus_score", ascending=False).reset_index(drop=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    out_csv = output_dir / "consensus_predictions.csv"
    merged.to_csv(out_csv, index=False)
    report = {
        "n_models": len(frames_with),
        "n_compounds": int(len(merged)),
        "mean_consensus_std": float(np.mean(merged["consensus_std"])) if len(merged) else 0.0,
        "max_consensus_std": float(np.max(merged["consensus_std"])) if len(merged) else 0.0,
        "highest_sensitivity_compounds": int(len(merged[merged["consensus_std"] > 0.1])) if len(merged) else 0,
        "output": str(out_csv),
        "note": "consensus_std is cross-model disagreement (higher = models diverge, worth a follow-up).",
    }
    write_json(output_dir / "consensus_metrics.json", report)
    print(json.dumps(report, indent=2))
    return 0


# ═════════════════════════════════════════════════════════════════════════════
# select — diversity-aware experimental batch (MaxMin / farthest-point)
# ═════════════════════════════════════════════════════════════════════════════
def run_select(args: argparse.Namespace) -> int:
    require_rdkit()
    input_path = Path(args.predictions).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    ensure_no_output_overwrite([input_path], [output_path])
    frame = read_csv_checked(input_path, [args.smiles_column])
    if args.score_column not in frame.columns:
        raise SystemExit(f"Missing score column '{args.score_column}' in predictions.")
    if args.domain_only and "applicability_domain" in frame.columns:
        frame = frame[frame["applicability_domain"] == "in_domain"]
    if args.min_score is not None:
        frame = frame[frame[args.score_column].astype(float) >= args.min_score]
    if getattr(args, "feasibility_column", None) and args.feasibility_column in frame.columns:
        # Treat values liked by a medicinal chemist as "feasible"; drop obvious no-go's.
        vals = frame[args.feasibility_column].astype(str).str.lower().str.strip()
        feasible = vals.isin(["yes", "y", "true", "feasible", "1", "ok", "easy", "synthesizable"])
        frame = frame[feasible]
    if frame.empty:
        raise SystemExit("No candidates after filters (domain/min-score/feasibility).")

    frame = frame.sort_values(args.score_column, ascending=False).reset_index(drop=True)
    max_candidates = int(args.max_candidates or len(frame))
    budget = max(1, int(args.budget or min(max_candidates, 100)))
    # limit the candidate pool to top-scoring ones
    frame = frame.head(max_candidates).reset_index(drop=True)

    smiles = frame[args.smiles_column].tolist()
    molecules = molecules_from_canonical(smiles)
    _, fps, _ = featurize_molecules(molecules, fp_radius=args.fp_radius, fp_bits=args.fp_bits)

    n = len(fps)
    if n == 0:
        raise SystemExit("No compounds to select.")
    # pairwise Tanimoto similarity matrix
    sim = np.zeros((n, n), dtype=float)
    for i, fp in enumerate(fps):
        sim[i, :] = np.asarray(DataStructs.BulkTanimotoSimilarity(fp, fps), dtype=float)
    dist = 1.0 - sim  # dissimilarity

    # Greedy farthest-point (MaxMin) selection starting from the top-scored compound
    selected = [0]
    remaining = list(range(1, n))
    while len(selected) < budget and remaining:
        min_dists = np.asarray([np.min(dist[i, selected]) for i in remaining])
        pick = int(np.argmax(min_dists))
        selected.append(remaining[pick])
        remaining.pop(pick)

    shortlist = frame.iloc[selected].copy().reset_index(drop=True)
    shortlist["selection_rank"] = np.arange(1, len(shortlist) + 1)
    shortlist["selection_method"] = "MaxMin_diversity"
    # diversity metric: mean pairwise similarity of the chosen set
    sel_sim = sim[np.ix_(selected, selected)]
    k = sel_sim.shape[0]
    # Off-diagonal mean Tanimoto (diagonal = 1.0 self-similarity, so subtract k).
    mean_pair = float((sel_sim.sum() - k) / max(1, k * (k - 1)))
    shortlist["pairwise_mean_similarity"] = round(mean_pair, 4)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    shortlist.to_csv(output_path, index=False)
    report = {
        "candidate_pool": int(len(frame)),
        "budget": int(len(shortlist)),
        "selection_method": "MaxMin (farthest-point) on ECFP Tanimoto",
        "mean_pairwise_similarity": round(mean_pair, 4),
        "diversity_note": "Lower mean pairwise similarity = more chemically diverse batch. "
                          "Trade diversity against score: high-scoring analogues may be redundant.",
        "output": str(output_path),
    }
    write_json(output_path.with_suffix(".selection.json"), report)
    print(json.dumps(report, indent=2))
    return 0


# ═════════════════════════════════════════════════════════════════════════════
# interpret — feature importance + fingerprint-bit -> molecule mapping (SAR aid)
# ═════════════════════════════════════════════════════════════════════════════
def run_interpret(args: argparse.Namespace) -> int:
    require_rdkit()
    bundle = load_trusted_bundle(Path(args.model).expanduser().resolve(), args.trust_model)
    data_path = Path(args.data).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    ensure_no_output_overwrite([Path(args.model), data_path], [output_dir])
    if output_dir.exists() and any(output_dir.iterdir()):
        raise SystemExit(f"Output directory is not empty: {output_dir}")

    frame = read_csv_checked(data_path, [args.smiles_column])
    valid, molecules, invalid = prepare_prediction_frame(
        frame, smiles_column=args.smiles_column, uncharge=True, tautomer_canonicalize=False)
    if valid.empty:
        raise SystemExit("No valid molecules in the data set.")
    X, fps, names = bundle_featurize(bundle, valid["canonical_smiles"].tolist())
    model = bundle["model"]
    has_target = bool(args.target_column) and args.target_column in frame.columns

    if has_target:
        y = frame.loc[valid["_input_row"].to_numpy(), args.target_column].tolist()
        if bundle["task"] == "classification":
            y_enc, _ = encode_class_labels(y, bundle["class_names"][-1] if len(bundle["class_names"]) == 2 else None)
            y_arr = y_enc.astype(int)
        else:
            y_arr = np.asarray([float(v) for v in y], dtype=float)
        try:
            perm = permutation_importance(model, X, y_arr, n_repeats=args.n_repeats,
                                          random_state=args.seed, scoring=None)
            importance = perm.importances_mean
        except Exception as exc:
            print(f"  [!] permutation importance failed ({type(exc).__name__}); "
                  "falling back to intrinsic importance.", file=sys.stderr)
            importance = _intrinsic_importance(model, names)
    else:
        importance = _intrinsic_importance(model, names)

    frame_imp = pd.DataFrame({"feature": list(names), "importance": importance})
    frame_imp = frame_imp.sort_values("importance", ascending=False).reset_index(drop=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    frame_imp.to_csv(output_dir / "feature_importance.csv", index=False)

    # fingerprint-bit -> training molecule mapping for the top bits
    bit_count = int(bundle["feature_spec"]["fp_bits"])
    training = bundle["training_smiles"][: args.max_training]
    tr_mol = molecules_from_canonical(training)
    _, tr_fps, _ = featurize_molecules(tr_mol,
                                       fp_radius=int(bundle["feature_spec"]["fp_radius"]),
                                       fp_bits=bit_count)
    tr_arrays = []
    for fp in tr_fps:
        arr = np.zeros((bit_count,), dtype=np.float32)
        DataStructs.ConvertToNumpyArray(fp, arr)
        tr_arrays.append(arr)
    tr_matrix = np.asarray(tr_arrays)
    top_bits = [int(re.match(r"MorganBit_(\d+)", f).group(1))
                for f in frame_imp["feature"].head(args.top_n)
                if re.match(r"MorganBit_(\d+)", f)]
    mapping_rows = []
    for bit in top_bits:
        holders = np.where(tr_matrix[:, bit] > 0)[0]
        mapping_rows.append({
            "bit_index": bit,
            "count_in_training": int(len(holders)),
            "example_training_smiles": "; ".join(str(training[i]) for i in holders[:3]),
        })
    if mapping_rows:
        pd.DataFrame(mapping_rows).to_csv(output_dir / "top_bits_mapping.csv", index=False)
    summary = {
        "model_name": bundle["model_name"],
        "task": bundle["task"],
        "data_rows": int(len(valid)),
        "importance_method": "permutation" if has_target else "intrinsic",
        "has_target": has_target,
        "top_features": frame_imp.head(args.top_n).to_dict("records"),
        "output": str(output_dir),
        "note": (
            "Feature attributions are associative, not causal. Fingerprint bits map to "
            "atomic environments; they generate SAR hypotheses, not mechanism. See "
            "SKILL.md Phase 10."
        ),
    }
    write_json(output_dir / "interpretation.json", summary)
    print(json.dumps({"importance_method": summary["importance_method"],
                      "top_features": summary["top_features"][:5],
                      "output_dir": str(output_dir)}, indent=2))
    return 0


def _intrinsic_importance(model: Any, feature_names: Sequence[str]) -> np.ndarray:
    frame = extract_feature_importance(model, feature_names)
    if frame.empty or "importance" not in frame:
        return np.zeros(len(feature_names))
    return np.asarray(
        [float(frame.set_index("feature").loc[f, "importance"]) if f in set(frame["feature"]) else 0.0
         for f in feature_names],
        dtype=float
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Local, leakage-aware RF/SVM/gradient-boosting workflow for molecular drug "
            "discovery. Predictions are hypotheses, not efficacy or safety evidence."
        )
    )
    parser.add_argument("--version", action="version", version=TOOL_VERSION)
    subparsers = parser.add_subparsers(dest="command", required=True)

    audit_parser = subparsers.add_parser(
        "audit", help="Standardize, deduplicate, and audit a labeled molecular CSV."
    )
    add_labeled_common(audit_parser)
    audit_parser.set_defaults(func=run_audit)

    train_parser = subparsers.add_parser(
        "train", help="Train and compare RF, SVM/SVR, GB, and optional XGBoost."
    )
    add_labeled_common(train_parser)
    train_parser.add_argument(
        "--split", choices=["random", "scaffold", "time"], default="scaffold"
    )
    train_parser.add_argument(
        "--time-column", help="Date/time column required when --split time."
    )
    train_parser.add_argument("--test-size", type=float, default=0.2)
    train_parser.add_argument("--seed", type=int, default=2026)
    train_parser.add_argument("--cv-folds", type=int, default=5)
    train_parser.add_argument("--n-jobs", type=int, default=-1)
    train_parser.add_argument(
        "--models",
        nargs="+",
        choices=["rf", "svm", "gb", "xgb"],
        default=["rf", "svm", "gb"],
    )
    train_parser.add_argument(
        "--fast",
        action="store_true",
        help="Use a small smoke-test hyperparameter grid.",
    )
    train_parser.add_argument(
        "--calibrate",
        action="store_true",
        help="Cross-calibrate classification winner candidates.",
    )
    train_parser.add_argument(
        "--calibration-method", choices=["sigmoid", "isotonic"], default="sigmoid"
    )
    train_parser.add_argument(
        "--positive-label",
        help="Binary label to encode as class 1. Default: lexicographically last label.",
    )
    train_parser.add_argument(
        "--ad-threshold",
        type=float,
        help=(
            "Explicit minimum nearest-training Tanimoto for in-domain. Default: estimate the "
            "5th percentile of training leave-one-out nearest similarities."
        ),
    )
    train_parser.add_argument("--fp-radius", type=int, default=DEFAULT_FP_RADIUS)
    train_parser.add_argument("--fp-bits", type=int, default=DEFAULT_FP_BITS)
    train_parser.set_defaults(func=run_train)

    predict_parser = subparsers.add_parser(
        "predict", help="Score a molecular CSV using a trusted model bundle."
    )
    predict_parser.add_argument(
        "--model", required=True, help="Trusted model.joblib path."
    )
    predict_parser.add_argument(
        "--trust-model",
        action="store_true",
        help="Confirm trusted pickle/joblib input.",
    )
    predict_parser.add_argument("--input", required=True, help="Input library CSV.")
    predict_parser.add_argument("--smiles-column", default="smiles")
    predict_parser.add_argument(
        "--output", required=True, help="Output predictions CSV."
    )
    predict_parser.set_defaults(func=run_predict)

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Explore a dataset: composition, balance, scaffold diversity, similarity.",
    )
    analyze_parser.add_argument("--input", required=True)
    analyze_parser.add_argument("--smiles-column", default="smiles")
    analyze_parser.add_argument("--target-column", help="Optional label column.")
    analyze_parser.add_argument(
        "--task", choices=["classification", "regression"], default="classification"
    )
    analyze_parser.add_argument("--output-dir", required=True)
    analyze_parser.add_argument("--fp-radius", type=int, default=DEFAULT_FP_RADIUS)
    analyze_parser.add_argument("--fp-bits", type=int, default=DEFAULT_FP_BITS)
    analyze_parser.add_argument("--n-clusters", type=int, default=10)
    analyze_parser.add_argument("--seed", type=int, default=2026)
    analyze_parser.add_argument("--sample", type=int, default=2000,
                                help="Max molecules for the similarity sample.")
    analyze_parser.set_defaults(func=run_analyze)

    conformal_parser = subparsers.add_parser(
        "conformal",
        help="Inductive (split) conformal prediction sets / intervals for a model.",
    )
    conformal_parser.add_argument("--model", required=True)
    conformal_parser.add_argument("--trust-model", action="store_true")
    conformal_parser.add_argument("--calibration", required=True,
                                  help="Calibration CSV with smiles + target.")
    conformal_parser.add_argument("--smiles-column", default="smiles")
    conformal_parser.add_argument("--target-column", required=True)
    conformal_parser.add_argument("--task", choices=["classification", "regression"])
    conformal_parser.add_argument("--alpha", type=float, default=0.1,
                                  help="Miscoverage rate (coverage = 1-alpha).")
    conformal_parser.add_argument("--query", required=True, help="Query library CSV.")
    conformal_parser.add_argument("--query-smiles-column", default=None)
    conformal_parser.add_argument("--output", required=True)
    conformal_parser.set_defaults(func=run_conformal)

    ensemble_parser = subparsers.add_parser(
        "ensemble",
        help="Consensus/agreement over multiple prediction CSVs (cross-model ranking).",
    )
    ensemble_parser.add_argument("--predictions", nargs="+", required=True,
                                 help="One or more prediction CSVs.")
    ensemble_parser.add_argument("--smiles-column", default="canonical_smiles")
    ensemble_parser.add_argument(
        "--score-column", default="positive_probability",
        help="Column to average (positive_probability for classification, predicted_value for regression).",
    )
    ensemble_parser.add_argument(
        "--task", choices=["classification", "regression"], default="classification"
    )
    ensemble_parser.add_argument("--output-dir", required=True)
    ensemble_parser.set_defaults(func=run_ensemble)

    select_parser = subparsers.add_parser(
        "select",
        help="Diversity-aware (MaxMin) experimental batch from a predictions CSV.",
    )
    select_parser.add_argument("--predictions", required=True)
    select_parser.add_argument("--smiles-column", default="canonical_smiles")
    select_parser.add_argument("--score-column", default="positive_probability")
    select_parser.add_argument("--budget", type=int, default=100)
    select_parser.add_argument("--min-score", type=float, default=None)
    select_parser.add_argument("--domain-only", action="store_true")
    select_parser.add_argument(
        "--feasibility-column",
        help="Optional column of feasibility flags (e.g. yes/no or synthesizable/easy); "
             "only rows flagged feasible are kept.",
    )
    select_parser.add_argument("--output", required=True)
    select_parser.add_argument("--fp-radius", type=int, default=DEFAULT_FP_RADIUS)
    select_parser.add_argument("--fp-bits", type=int, default=DEFAULT_FP_BITS)
    select_parser.add_argument("--max-candidates", type=int, default=5000)
    select_parser.set_defaults(func=run_select)

    interpret_parser = subparsers.add_parser(
        "interpret",
        help="Feature importance + fingerprint-bit -> molecule mapping (SAR aid).",
    )
    interpret_parser.add_argument("--model", required=True)
    interpret_parser.add_argument("--trust-model", action="store_true")
    interpret_parser.add_argument("--data", required=True, help="CSV with smiles (+ optional target).")
    interpret_parser.add_argument("--smiles-column", default="smiles")
    interpret_parser.add_argument("--target-column", help="Optional label for permutation importance.")
    interpret_parser.add_argument("--output-dir", required=True)
    interpret_parser.add_argument("--n-repeats", type=int, default=5)
    interpret_parser.add_argument("--top-n", type=int, default=20)
    interpret_parser.add_argument("--max-training", type=int, default=300)
    interpret_parser.add_argument("--seed", type=int, default=2026)
    interpret_parser.set_defaults(func=run_interpret)
    return parser


def validate_args(args: argparse.Namespace) -> None:
    if hasattr(args, "test_size") and not (0.05 <= args.test_size <= 0.5):
        raise SystemExit("--test-size must be between 0.05 and 0.5.")
    if hasattr(args, "cv_folds") and args.cv_folds < 2:
        raise SystemExit("--cv-folds must be at least 2.")
    if hasattr(args, "fp_radius") and args.fp_radius < 1:
        raise SystemExit("--fp-radius must be at least 1.")
    if hasattr(args, "fp_bits") and args.fp_bits < 128:
        raise SystemExit("--fp-bits must be at least 128.")
    if (
        hasattr(args, "ad_threshold")
        and args.ad_threshold is not None
        and not 0.0 <= args.ad_threshold <= 1.0
    ):
        raise SystemExit("--ad-threshold must be between 0 and 1.")
    if hasattr(args, "n_jobs") and args.n_jobs == 0:
        raise SystemExit("--n-jobs cannot be 0; use -1 or a nonzero processor count.")
    if (
        getattr(args, "task", None) == "regression"
        and getattr(args, "positive_label", None) is not None
    ):
        raise SystemExit("--positive-label applies only to classification.")
    if getattr(args, "task", None) == "regression" and getattr(
        args, "calibrate", False
    ):
        raise SystemExit("--calibrate applies only to classification.")
    if hasattr(args, "models") and len(set(args.models)) != len(args.models):
        raise SystemExit("--models contains a duplicate model name.")


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    validate_args(args)
    require_rdkit()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
