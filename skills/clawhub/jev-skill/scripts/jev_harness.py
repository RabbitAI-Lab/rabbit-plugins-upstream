#!/usr/bin/env python3
"""A dependency-free, schema-validating Jev evaluation harness.

The harness validates questions and golden cases offline, calls the TypeSafe
System One endpoint with bounded concurrency and retries, validates every
typed response, and reports accuracy/calibration/latency/token metrics without
including input state or API keys in the report.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import os
import random
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any


HARNESS_VERSION = "2.1.0"
API_URL = "https://api.typesafe.ai/v1/systemone"
QUESTION_TYPES = {"noul", "choice", "score"}
TRANSIENT_HTTP_CODES = {408, 429, 500, 502, 503, 504, 529}
REQUEST_ID_HEADERS = ("x-typesafe-request-id", "x-request-id", "request-id")
CALIBRATION_THRESHOLDS = (0.5, 0.6, 0.7, 0.8, 0.9)
EPSILON = 1e-12


class HarnessInputError(ValueError):
    pass


class RequestError(RuntimeError):
    """A request failure with safe provider metadata for the report."""

    def __init__(self, message: str, status_code: int | None = None, request_id: str | None = None):
        super().__init__(message)
        self.status_code = status_code
        self.request_id = request_id


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(2)


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"file not found: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")


def read_cases(path: Path) -> list[dict[str, Any]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        fail(f"file not found: {path}")
    cases: list[dict[str, Any]] = []
    for line_number, line in enumerate(lines, 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON on {path}:{line_number}: {exc}")
        if not isinstance(value, dict):
            fail(f"case on {path}:{line_number} must be an object")
        value.setdefault("id", f"case-{len(cases) + 1}")
        value["_source_line"] = line_number
        cases.append(value)
    if not cases:
        fail(f"no cases found in {path}")
    return cases


def is_json_value(value: Any) -> bool:
    if value is None or isinstance(value, (str, int, float, bool)):
        return not isinstance(value, float) or math.isfinite(value)
    if isinstance(value, list):
        return all(is_json_value(item) for item in value)
    if isinstance(value, dict):
        return all(isinstance(key, str) and is_json_value(item) for key, item in value.items())
    return False


def require_finite_number(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(float(value)):
        raise HarnessInputError(f"{label} must be a finite number")
    return float(value)


def validate_questions(questions: Any) -> dict[str, dict[str, Any]]:
    if not isinstance(questions, dict) or not questions:
        raise HarnessInputError("questions must be a non-empty JSON object")
    normalized: dict[str, dict[str, Any]] = {}
    for question_id, question in questions.items():
        if not isinstance(question_id, str) or not question_id.strip():
            raise HarnessInputError("question IDs must be non-empty strings")
        if not isinstance(question, dict):
            raise HarnessInputError(f"question {question_id!r} must be an object")
        question_type = question.get("type")
        if question_type not in QUESTION_TYPES:
            raise HarnessInputError(f"question {question_id!r} type must be one of {sorted(QUESTION_TYPES)}")
        instructions = question.get("instructions")
        if not isinstance(instructions, (str, dict, list)) or not instructions:
            raise HarnessInputError(f"question {question_id!r} needs non-empty instructions")
        if not is_json_value(instructions):
            raise HarnessInputError(f"question {question_id!r} instructions must be JSON-compatible")
        if question_type == "noul":
            criteria = question.get("criteria")
            if criteria is not None:
                if not isinstance(criteria, dict) or not set(criteria).issubset({"true", "false"}):
                    raise HarnessInputError(f"noul question {question_id!r} criteria must use true/false keys")
        elif question_type == "choice":
            criteria = question.get("criteria")
            if not isinstance(criteria, dict) or not 2 <= len(criteria) <= 255:
                raise HarnessInputError(f"choice question {question_id!r} needs 2–255 criteria")
            if any(not isinstance(key, str) or not key.strip() for key in criteria):
                raise HarnessInputError(f"choice question {question_id!r} has an empty option key")
            if not all(value is None or is_json_value(value) for value in criteria.values()):
                raise HarnessInputError(f"choice question {question_id!r} criteria must be JSON-compatible")
        else:
            criteria = question.get("criteria")
            if not isinstance(criteria, list) or not 2 <= len(criteria) <= 10:
                raise HarnessInputError(f"score question {question_id!r} needs 2–10 ordered criteria")
            if not all(is_json_value(value) and value is not None for value in criteria):
                raise HarnessInputError(f"score question {question_id!r} criteria must be non-null JSON values")
        normalized[question_id] = question
    return normalized


def validate_expected(question: dict[str, Any], value: Any, case_label: str, question_id: str) -> None:
    question_type = question["type"]
    if question_type == "noul":
        if not isinstance(value, bool) and not (isinstance(value, (int, float)) and not isinstance(value, bool) and value in (0, 1)):
            raise HarnessInputError(f"{case_label} expected {question_id!r} must be boolean or 0/1")
    elif question_type == "choice":
        if not isinstance(value, str) or value not in question["criteria"]:
            raise HarnessInputError(f"{case_label} expected {question_id!r} must be one of the Choice keys")
    else:
        level = value.get("level") if isinstance(value, dict) else value
        numeric_level = require_finite_number(level, f"{case_label} expected {question_id!r} score")
        if not 0 <= numeric_level <= len(question["criteria"]) - 1:
            raise HarnessInputError(f"{case_label} expected {question_id!r} score is outside the defined levels")
        if isinstance(value, dict) and "tolerance" in value:
            tolerance = require_finite_number(value["tolerance"], f"{case_label} expected {question_id!r} tolerance")
            if tolerance < 0:
                raise HarnessInputError(f"{case_label} expected {question_id!r} tolerance cannot be negative")


def validate_cases(cases: list[dict[str, Any]], questions: dict[str, dict[str, Any]]) -> None:
    question_ids = set(questions)
    seen_ids: set[str] = set()
    for index, case in enumerate(cases, 1):
        case_label = f"case {case.get('id', index)!r}"
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            raise HarnessInputError(f"case {index} id must be a non-empty string")
        if case_id in seen_ids:
            raise HarnessInputError(f"duplicate case id {case_id!r}")
        seen_ids.add(case_id)
        state = case.get("state")
        if not isinstance(state, (str, dict, list)) or not is_json_value(state):
            raise HarnessInputError(f"{case_label} state must be a JSON string, object, or array")
        tags = case.get("tags", [])
        if not isinstance(tags, list) or any(not isinstance(tag, str) or not tag.strip() for tag in tags):
            raise HarnessInputError(f"{case_label} tags must be a list of non-empty strings")
        if len(set(tags)) != len(tags):
            raise HarnessInputError(f"{case_label} tags must not contain duplicates")
        case["tags"] = tags
        expected = case.get("expected", {})
        if not isinstance(expected, dict):
            raise HarnessInputError(f"{case_label} expected must be an object")
        unknown = set(expected) - question_ids
        if unknown:
            raise HarnessInputError(f"{case_label} expected unknown question IDs: {sorted(unknown)}")
        for question_id, value in expected.items():
            validate_expected(questions[question_id], value, case_label, question_id)


def canonical_hash(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def request_id_from_headers(headers: Any) -> str | None:
    for header_name in REQUEST_ID_HEADERS:
        value = headers.get(header_name) if headers is not None else None
        if value:
            return str(value)
    return None


def request(payload: dict[str, Any], api_key: str, timeout: float, retries: int, max_backoff: float) -> tuple[dict[str, Any], str | None, int]:
    body = json.dumps(payload, ensure_ascii=False, allow_nan=False).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": f"jev-skill-harness/{HARNESS_VERSION}",
    }
    for attempt in range(retries + 1):
        req = urllib.request.Request(API_URL, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                try:
                    value = json.loads(response.read().decode("utf-8"))
                except json.JSONDecodeError as exc:
                    raise RuntimeError("TypeSafe returned invalid JSON") from exc
                if not isinstance(value, dict):
                    raise RuntimeError("TypeSafe returned a non-object JSON response")
                return value, request_id_from_headers(response.headers), attempt + 1
        except urllib.error.HTTPError as exc:
            response_body = exc.read().decode("utf-8", errors="replace")[:1000]
            if exc.code not in TRANSIENT_HTTP_CODES or attempt >= retries:
                raise RequestError(
                    f"TypeSafe HTTP {exc.code}: {response_body}",
                    status_code=exc.code,
                    request_id=request_id_from_headers(exc.headers),
                ) from exc
            retry_after = exc.headers.get("Retry-After")
            if retry_after:
                try:
                    delay = float(retry_after)
                except ValueError:
                    delay = min(max_backoff, 2**attempt)
            else:
                delay = random.uniform(0.0, min(max_backoff, 2**attempt))
            time.sleep(max(0.0, min(delay, max_backoff)))
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt >= retries:
                reason = getattr(exc, "reason", str(exc))
                raise RequestError(f"TypeSafe connection failed: {reason}") from exc
            time.sleep(random.uniform(0.0, min(max_backoff, 2**attempt)))
    raise RequestError("request failed")


def validate_distribution(value: Any, expected_keys: set[str], label: str, warnings: list[str]) -> dict[str, float]:
    if not isinstance(value, dict) or set(value) != expected_keys:
        raise ValueError(f"{label} probabilities must contain exactly {sorted(expected_keys)}")
    probabilities: dict[str, float] = {}
    for key, probability in value.items():
        numeric = require_finite_number(probability, f"{label} probability {key!r}")
        if not 0 <= numeric <= 1:
            raise ValueError(f"{label} probability {key!r} must be between 0 and 1")
        probabilities[key] = numeric
    total = sum(probabilities.values())
    if abs(total - 1.0) > 0.02:
        raise ValueError(f"{label} probabilities sum to {total:.6f}, not 1")
    if abs(total - 1.0) > 1e-6:
        warnings.append(f"{label} probabilities sum to {total:.6f} after rounding")
    return probabilities


def validate_answer(question: dict[str, Any], answer: Any, question_id: str, warnings: list[str]) -> None:
    if not isinstance(answer, dict):
        raise ValueError(f"answer {question_id!r} is not an object")
    question_type = question["type"]
    if answer.get("type") != question_type:
        raise ValueError(f"answer {question_id!r} type does not match its question")
    if question_type == "noul":
        probability = require_finite_number(answer.get("noul"), f"answer {question_id!r}.noul")
        if not 0 <= probability <= 1:
            raise ValueError(f"answer {question_id!r}.noul must be between 0 and 1")
        return
    confidence = require_finite_number(answer.get("confidence"), f"answer {question_id!r}.confidence")
    if not 0 <= confidence <= 1:
        raise ValueError(f"answer {question_id!r}.confidence must be between 0 and 1")
    if question_type == "choice":
        choice = answer.get("choice")
        criteria = question["criteria"]
        if choice not in criteria:
            raise ValueError(f"answer {question_id!r}.choice is not in the question criteria")
        validate_distribution(answer.get("probabilities"), set(criteria), f"answer {question_id!r}", warnings)
        return
    score = require_finite_number(answer.get("score"), f"answer {question_id!r}.score")
    level_count = len(question["criteria"])
    if not 0 <= score <= level_count - 1:
        raise ValueError(f"answer {question_id!r}.score is outside the defined levels")
    expected_keys = {str(index) for index in range(level_count)}
    legend = answer.get("legend")
    if not isinstance(legend, dict) or set(legend) != expected_keys:
        raise ValueError(f"answer {question_id!r}.legend must contain every score level")
    validate_distribution(answer.get("probabilities"), expected_keys, f"answer {question_id!r}", warnings)


def validate_response(response: Any, questions: dict[str, dict[str, Any]]) -> tuple[dict[str, Any], list[str]]:
    if not isinstance(response, dict):
        raise ValueError("TypeSafe response is not an object")
    if not isinstance(response.get("model"), str):
        raise ValueError("TypeSafe response is missing model")
    answers = response.get("answers")
    if not isinstance(answers, dict):
        raise ValueError("TypeSafe response is missing answers")
    question_ids = set(questions)
    missing = question_ids - set(answers)
    extra = set(answers) - question_ids
    if missing:
        raise ValueError(f"TypeSafe response is missing answers: {sorted(missing)}")
    if extra:
        raise ValueError(f"TypeSafe response returned unknown answers: {sorted(extra)}")
    warnings: list[str] = []
    usage = response.get("usage")
    if usage is None:
        warnings.append("response omitted usage; token totals and cost are unavailable for this case")
    elif not isinstance(usage, dict):
        raise ValueError("TypeSafe response usage must be an object when present")
    else:
        for field in ("input_tokens", "output_tokens"):
            tokens = usage.get(field)
            if tokens is None:
                warnings.append(f"response usage omitted {field}")
            elif isinstance(tokens, bool) or not isinstance(tokens, (int, float)) or not math.isfinite(float(tokens)) or tokens < 0:
                raise ValueError(f"TypeSafe response usage.{field} must be a non-negative finite number")
    for question_id, question in questions.items():
        validate_answer(question, answers[question_id], question_id, warnings)
    return response, warnings


def expected_bool(value: Any) -> bool:
    return bool(value) if isinstance(value, bool) else bool(int(value))


def evaluate(question: dict[str, Any], answer: dict[str, Any], expected: Any, noul_threshold: float, score_tolerance: float, question_id: str) -> dict[str, Any]:
    question_type = question["type"]
    result: dict[str, Any] = {"id": question_id, "type": question_type, "expected": expected}
    if question_type == "noul":
        probability = float(answer["noul"])
        label = expected_bool(expected)
        prediction = probability >= noul_threshold
        result["expected"] = label
        result.update({
            "actual": prediction,
            "yes_probability": probability,
            "correct": prediction == label,
            "brier": (probability - float(label)) ** 2,
            "log_loss": -math.log(max(EPSILON, probability if label else 1.0 - probability)),
        })
        return result
    if question_type == "choice":
        actual = answer["choice"]
        probabilities = answer["probabilities"]
        ordered = sorted(probabilities.values(), reverse=True)
        margin = ordered[0] - ordered[1] if len(ordered) > 1 else ordered[0]
        result.update({
            "actual": actual,
            "correct": actual == expected,
            "confidence": answer["confidence"],
            "margin": margin,
            "probabilities": probabilities,
        })
        return result
    actual_score = float(answer["score"])
    expected_level = float(expected["level"] if isinstance(expected, dict) else expected)
    tolerance = float(expected.get("tolerance", score_tolerance) if isinstance(expected, dict) else score_tolerance)
    absolute_error = abs(actual_score - expected_level)
    predicted_level = min(len(question["criteria"]) - 1, max(0, math.floor(actual_score + 0.5)))
    result.update({
        "actual": actual_score,
        "expected_level": expected_level,
        "absolute_error": absolute_error,
        "within_tolerance": absolute_error <= tolerance,
        "predicted_level": predicted_level,
        "level_correct": predicted_level == expected_level,
        "correct": predicted_level == expected_level,
        "confidence": answer["confidence"],
        "probabilities": answer["probabilities"],
    })
    return result


def json_size(value: Any) -> int:
    return len(json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8"))


def normalized_usage(response: dict[str, Any]) -> dict[str, int | float]:
    usage = response.get("usage")
    if not isinstance(usage, dict):
        return {}
    return {
        field: usage[field]
        for field in ("input_tokens", "output_tokens")
        if field in usage and usage[field] is not None
    }


def run_case(case: dict[str, Any], questions: dict[str, dict[str, Any]], model: str, timeout: float, retries: int, max_backoff: float, api_key: str, noul_threshold: float, score_tolerance: float) -> dict[str, Any]:
    started = time.perf_counter()
    payload = {"state": case["state"], "model": model, "questions": questions}
    state_bytes = json_size(case["state"])
    try:
        response, request_id, attempts = request(payload, api_key, timeout, retries, max_backoff)
        response, warnings = validate_response(response, questions)
        answers = response["answers"]
        evaluations = [
            evaluate(questions[question_id], answers[question_id], expected, noul_threshold, score_tolerance, question_id)
            for question_id, expected in case.get("expected", {}).items()
        ]
        return {
            "index": case["_index"],
            "id": case["id"],
            "tags": case.get("tags", []),
            "ok": True,
            "latency_ms": round((time.perf_counter() - started) * 1000, 1),
            "state_bytes": state_bytes,
            "model": response["model"],
            "request_id": request_id,
            "attempts": attempts,
            "answers": answers,
            "expected": case.get("expected", {}),
            "evaluations": evaluations,
            "usage": normalized_usage(response),
            "warnings": warnings,
        }
    except Exception as exc:  # noqa: BLE001 - preserve a case-level failure in the report
        return {
            "index": case["_index"],
            "id": case["id"],
            "tags": case.get("tags", []),
            "ok": False,
            "latency_ms": round((time.perf_counter() - started) * 1000, 1),
            "state_bytes": state_bytes,
            "request_id": getattr(exc, "request_id", None),
            "status_code": getattr(exc, "status_code", None),
            "error": str(exc),
            "expected": case.get("expected", {}),
            "answers": {},
            "evaluations": [],
            "usage": {},
            "warnings": [],
        }


def percentile(values: list[float], fraction: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    position = (len(ordered) - 1) * fraction
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return round(ordered[lower], 1)
    return round(ordered[lower] + (ordered[upper] - ordered[lower]) * (position - lower), 1)


def mean(values: list[float]) -> float | None:
    return round(sum(values) / len(values), 6) if values else None


def finite_numbers(records: list[dict[str, Any]], field: str) -> list[float]:
    values: list[float] = []
    for record in records:
        value = record.get(field)
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(float(value)):
            continue
        values.append(float(value))
    return values


def usage_numbers(records: list[dict[str, Any]], field: str) -> list[float]:
    values: list[float] = []
    for record in records:
        usage = record.get("usage", {})
        value = usage.get(field) if isinstance(usage, dict) else None
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(float(value)):
            continue
        values.append(float(value))
    return values


def confidence_metrics(items: list[dict[str, Any]]) -> dict[str, Any]:
    confidences = [float(item["confidence"]) for item in items]
    correct_confidence = [float(item["confidence"]) for item in items if item["correct"]]
    wrong_confidence = [float(item["confidence"]) for item in items if not item["correct"]]
    bins: list[dict[str, Any]] = []
    ece = 0.0
    for index in range(10):
        lower = index / 10
        upper = (index + 1) / 10
        bucket = [item for item in items if lower <= float(item["confidence"]) < upper or index == 9 and float(item["confidence"]) == upper]
        bucket_confidence = [float(item["confidence"]) for item in bucket]
        bucket_accuracy = [1.0 if item["correct"] else 0.0 for item in bucket]
        accuracy = mean(bucket_accuracy)
        if bucket:
            ece += len(bucket) / len(items) * abs((mean(bucket_confidence) or 0.0) - (accuracy or 0.0))
        bins.append({
            "lower": lower,
            "upper": upper,
            "count": len(bucket),
            "mean_confidence": mean(bucket_confidence),
            "accuracy": accuracy,
        })
    selective: dict[str, Any] = {}
    for threshold in CALIBRATION_THRESHOLDS:
        selected = [item for item in items if float(item["confidence"]) >= threshold]
        selective[str(threshold)] = {
            "count": len(selected),
            "coverage": round(len(selected) / len(items), 6) if items else None,
            "accuracy": round(sum(item["correct"] for item in selected) / len(selected), 6) if selected else None,
            "error_rate": round(sum(not item["correct"] for item in selected) / len(selected), 6) if selected else None,
        }
    return {
        "mean_confidence": mean(confidences),
        "mean_confidence_when_correct": mean(correct_confidence),
        "mean_confidence_when_wrong": mean(wrong_confidence),
        "ece": round(ece, 6) if items else None,
        "calibration_bins": bins,
        "selective": selective,
    }


def summarize_evaluations(items: list[dict[str, Any]], question_type: str) -> dict[str, Any]:
    correct = [item for item in items if item.get("correct") is True]
    result: dict[str, Any] = {
        "total": len(items),
        "accuracy": round(len(correct) / len(items), 6) if items else None,
    }
    if question_type == "noul":
        briers = [float(item["brier"]) for item in items]
        log_losses = [float(item["log_loss"]) for item in items]
        result.update({"brier": mean(briers), "log_loss": mean(log_losses)})
    elif question_type in {"choice", "score"}:
        result.update(confidence_metrics(items))
        if question_type == "choice":
            result["mean_margin"] = mean([float(item["margin"]) for item in items])
        else:
            errors = [float(item["absolute_error"]) for item in items]
            result.update({
                "within_tolerance": round(sum(item["within_tolerance"] for item in items) / len(items), 6) if items else None,
                "mae": mean(errors),
                "rmse": round(math.sqrt(sum(error * error for error in errors) / len(errors)), 6) if errors else None,
            })
    return result


def summarize(records: list[dict[str, Any]], questions: dict[str, dict[str, Any]], input_price: float | None, output_price: float | None) -> dict[str, Any]:
    evaluations = [evaluation for record in records for evaluation in record.get("evaluations", [])]
    successful = [record for record in records if record.get("ok")]
    latencies = finite_numbers(records, "latency_ms")
    input_tokens = usage_numbers(successful, "input_tokens")
    output_tokens = usage_numbers(successful, "output_tokens")
    state_bytes = finite_numbers(records, "state_bytes")
    attempts = finite_numbers(records, "attempts")
    correct = [evaluation for evaluation in evaluations if evaluation.get("correct") is True]
    model_counts: dict[str, int] = defaultdict(int)
    for record in successful:
        if isinstance(record.get("model"), str):
            model_counts[record["model"]] += 1
    summary: dict[str, Any] = {
        "cases": len(records),
        "successful_cases": len(successful),
        "failed_cases": len(records) - len(successful),
        "error_rate": round((len(records) - len(successful)) / len(records), 6) if records else None,
        "questions": len(questions),
        "scored_answers": len(evaluations),
        "exact_accuracy": round(len(correct) / len(evaluations), 6) if evaluations else None,
        "models": dict(model_counts),
        "requests_with_ids": sum(bool(record.get("request_id")) for record in records),
        "latency_ms": {
            "mean": mean(latencies),
            "p50": percentile(latencies, 0.50),
            "p95": percentile(latencies, 0.95),
            "max": max(latencies) if latencies else None,
        },
        "usage": {
            "input_tokens": int(sum(input_tokens)) if input_tokens else None,
            "output_tokens": int(sum(output_tokens)) if output_tokens else None,
        },
        "attempts": {
            "total": int(sum(attempts)) if attempts else None,
            "mean": mean(attempts),
            "max": max(attempts) if attempts else None,
        },
        "state_bytes": {
            "total": int(sum(state_bytes)) if state_bytes else None,
            "mean": mean(state_bytes),
            "max": max(state_bytes) if state_bytes else None,
        },
    }
    if input_price is not None or output_price is not None:
        input_cost = sum(input_tokens) * (input_price or 0.0) / 1_000_000
        output_cost = sum(output_tokens) * (output_price or 0.0) / 1_000_000
        summary["estimated_cost_usd"] = round(input_cost + output_cost, 8)

    by_type: dict[str, dict[str, Any]] = {}
    for question_type in ("noul", "choice", "score"):
        items = [evaluation for evaluation in evaluations if evaluation["type"] == question_type]
        type_summary: dict[str, Any] = summarize_evaluations(items, question_type)
        if question_type == "noul":
            tp = sum(item["actual"] is True and item["expected"] is True for item in items)
            tn = sum(item["actual"] is False and item["expected"] is False for item in items)
            fp = sum(item["actual"] is True and item["expected"] is False for item in items)
            fn = sum(item["actual"] is False and item["expected"] is True for item in items)
            precision = tp / (tp + fp) if tp + fp else None
            recall = tp / (tp + fn) if tp + fn else None
            type_summary.update({
                "confusion": {"true_positive": tp, "true_negative": tn, "false_positive": fp, "false_negative": fn},
                "precision": round(precision, 6) if precision is not None else None,
                "recall": round(recall, 6) if recall is not None else None,
                "f1": round((2 * precision * recall) / (precision + recall), 6) if precision is not None and recall is not None and precision + recall else None,
            })
        elif question_type == "choice":
            confusion: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
            for item in items:
                confusion[str(item["expected"])][str(item["actual"])] += 1
            type_summary.update({
                "confusion": {expected: dict(predicted) for expected, predicted in confusion.items()},
            })
        else:
            level_hits = [item for item in items if item["level_correct"]]
            type_summary.update({
                "level_accuracy": round(len(level_hits) / len(items), 6) if items else None,
            })
        by_type[question_type] = type_summary
    summary["by_type"] = by_type

    by_question: dict[str, dict[str, Any]] = {}
    for question_id, question in questions.items():
        items = [evaluation for evaluation in evaluations if evaluation["id"] == question_id]
        by_question[question_id] = summarize_evaluations(items, question["type"])
        if question["type"] == "score":
            by_question[question_id]["level_accuracy"] = round(sum(item["level_correct"] for item in items) / len(items), 6) if items else None
    summary["by_question"] = by_question

    by_tag: dict[str, dict[str, Any]] = {}
    known_tags = sorted({tag for record in records for tag in record.get("tags", [])})
    for tag in known_tags:
        tagged_records = [record for record in records if tag in record.get("tags", [])]
        tagged_evaluations = [evaluation for record in tagged_records for evaluation in record.get("evaluations", [])]
        tagged_correct = [evaluation for evaluation in tagged_evaluations if evaluation.get("correct") is True]
        by_tag[tag] = {
            "cases": len(tagged_records),
            "successful_cases": sum(record.get("ok") is True for record in tagged_records),
            "error_rate": round(sum(record.get("ok") is not True for record in tagged_records) / len(tagged_records), 6) if tagged_records else None,
            "scored_answers": len(tagged_evaluations),
            "exact_accuracy": round(len(tagged_correct) / len(tagged_evaluations), 6) if tagged_evaluations else None,
            "latency_ms_p95": percentile(finite_numbers(tagged_records, "latency_ms"), 0.95),
            "input_tokens": int(sum(usage_numbers(tagged_records, "input_tokens"))) if usage_numbers(tagged_records, "input_tokens") else None,
        }
    summary["by_tag"] = by_tag
    return summary


def gates(summary: dict[str, Any], args: argparse.Namespace) -> list[str]:
    failures: list[str] = []
    exact_accuracy = summary.get("exact_accuracy")
    if args.min_accuracy is not None and (exact_accuracy is None or exact_accuracy < args.min_accuracy):
        failures.append(f"exact_accuracy {exact_accuracy} < required {args.min_accuracy}")
    error_rate = summary.get("error_rate")
    if args.max_error_rate is not None and (error_rate is None or error_rate > args.max_error_rate):
        failures.append(f"error_rate {error_rate} > allowed {args.max_error_rate}")
    noul_brier = summary.get("by_type", {}).get("noul", {}).get("brier")
    if args.max_noul_brier is not None and (noul_brier is None or noul_brier > args.max_noul_brier):
        failures.append(f"noul brier {noul_brier} > allowed {args.max_noul_brier}")
    score_mae = summary.get("by_type", {}).get("score", {}).get("mae")
    if args.max_score_mae is not None and (score_mae is None or score_mae > args.max_score_mae):
        failures.append(f"score MAE {score_mae} > allowed {args.max_score_mae}")
    estimated_cost = summary.get("estimated_cost_usd")
    if args.max_cost_usd is not None and (estimated_cost is None or estimated_cost > args.max_cost_usd):
        failures.append(f"estimated cost {estimated_cost} > allowed {args.max_cost_usd}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate Jev typed questions over a JSONL golden set.")
    parser.add_argument("--questions", required=True, type=Path, help="JSON file containing the questions map")
    parser.add_argument("--cases", required=True, type=Path, help="JSONL file containing state and optional expected answers")
    parser.add_argument("--output", type=Path, help="Write the report JSON to this path")
    parser.add_argument("--model", default="jev-latest")
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--max-backoff", type=float, default=10.0)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--case-id", action="append", help="Run only this case ID; may be repeated")
    parser.add_argument("--tag", action="append", help="Run only cases containing every requested tag; may be repeated")
    parser.add_argument("--noul-threshold", type=float, default=0.5)
    parser.add_argument("--score-tolerance", type=float, default=0.5)
    parser.add_argument("--input-price-per-million", type=float)
    parser.add_argument("--output-price-per-million", type=float)
    parser.add_argument("--min-accuracy", type=float)
    parser.add_argument("--max-error-rate", type=float)
    parser.add_argument("--max-noul-brier", type=float)
    parser.add_argument("--max-score-mae", type=float)
    parser.add_argument("--max-cost-usd", type=float)
    parser.add_argument("--validate-only", action="store_true", help="Validate inputs without calling the API")
    args = parser.parse_args()
    if args.concurrency < 1 or args.concurrency > 64:
        fail("concurrency must be between 1 and 64")
    if args.retries < 0 or args.max_backoff < 0 or args.timeout <= 0:
        fail("retries cannot be negative; timeout must be positive and max-backoff non-negative")
    if args.offset < 0 or args.limit is not None and args.limit < 1:
        fail("offset cannot be negative and limit must be positive")
    if not isinstance(args.model, str) or not args.model.strip():
        fail("model must be a non-empty string")
    for name in ("noul_threshold", "score_tolerance", "input_price_per_million", "output_price_per_million", "min_accuracy", "max_error_rate", "max_noul_brier", "max_score_mae", "max_cost_usd"):
        value = getattr(args, name)
        if value is not None and (not math.isfinite(value) or value < 0):
            fail(f"{name} must be a non-negative finite number")
    if not 0 <= args.noul_threshold <= 1:
        fail("noul-threshold must be between 0 and 1")
    if args.min_accuracy is not None and args.min_accuracy > 1:
        fail("min-accuracy cannot exceed 1")
    if args.max_error_rate is not None and args.max_error_rate > 1:
        fail("max-error-rate cannot exceed 1")

    try:
        questions = validate_questions(read_json(args.questions))
        all_cases = read_cases(args.cases)
        validate_cases(all_cases, questions)
    except HarnessInputError as exc:
        fail(str(exc))

    selected = all_cases[args.offset:]
    if args.limit is not None:
        selected = selected[: args.limit]
    if args.case_id:
        wanted = set(args.case_id)
        selected = [case for case in selected if case["id"] in wanted]
    if args.tag:
        wanted_tags = set(args.tag)
        selected = [case for case in selected if wanted_tags.issubset(set(case.get("tags", [])))]
    if not selected:
        fail("no cases selected")
    for index, case in enumerate(selected):
        case["_index"] = index

    config = {
        "model": args.model,
        "concurrency": args.concurrency,
        "timeout_seconds": args.timeout,
        "retries": args.retries,
        "max_backoff_seconds": args.max_backoff,
        "noul_threshold": args.noul_threshold,
        "score_tolerance": args.score_tolerance,
        "question_sha256": canonical_hash(questions),
        "case_id_sha256": canonical_hash([case["id"] for case in selected]),
        "tag_filter": args.tag or [],
    }
    if args.validate_only:
        print(json.dumps({"valid": True, "harness_version": HARNESS_VERSION, "config": config, "cases": len(selected), "questions": list(questions)}, indent=2))
        return 0

    api_key = os.environ.get("TYPESAFE_API_KEY")
    if not api_key:
        fail("set TYPESAFE_API_KEY or use --validate-only")

    records: list[dict[str, Any] | None] = [None] * len(selected)
    with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        futures = {
            executor.submit(
                run_case,
                case,
                questions,
                args.model,
                args.timeout,
                args.retries,
                args.max_backoff,
                api_key,
                args.noul_threshold,
                args.score_tolerance,
            ): index
            for index, case in enumerate(selected)
        }
        for future in as_completed(futures):
            index = futures[future]
            try:
                records[index] = future.result()
            except Exception as exc:  # pragma: no cover - defensive future boundary
                records[index] = {"index": index, "id": selected[index]["id"], "tags": selected[index].get("tags", []), "ok": False, "latency_ms": 0, "state_bytes": json_size(selected[index]["state"]), "error": str(exc), "answers": {}, "evaluations": [], "usage": {}, "warnings": []}
    final_records = [record for record in records if record is not None]
    summary = summarize(final_records, questions, args.input_price_per_million, args.output_price_per_million)
    gate_failures = gates(summary, args)
    report = {
        "harness_version": HARNESS_VERSION,
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "config": {**config, "case_count": len(final_records)},
        "summary": summary,
        "gates": gate_failures,
        "status": "passed" if not gate_failures and summary["failed_cases"] == 0 else "failed",
        "records": final_records,
    }
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except HarnessInputError as exc:
        fail(str(exc))
