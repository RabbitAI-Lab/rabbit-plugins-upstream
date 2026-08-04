#!/usr/bin/env python3
"""data/units.json의 변환표를 읽어 값을 다른 단위로 바꾼다.

    python3 scripts/convert.py 5 km mi
    python3 scripts/convert.py 100 화씨 섭씨
    python3 scripts/convert.py --list
"""

import argparse
import json
import sys
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "units.json"


def load_table():
    try:
        with DATA_PATH.open(encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        sys.exit(f"오류: 변환표를 찾을 수 없다 ({DATA_PATH})")
    except json.JSONDecodeError as exc:
        sys.exit(f"오류: 변환표가 올바른 JSON이 아니다 ({exc})")


def normalize(name):
    """사용자가 흔히 붙이지만 표에는 없는 문자를 떼어낸다."""
    return name.strip().lower().replace("°", "").replace(" ", "").replace("_", "")


def lookup(table, key):
    for dimension, spec in table.items():
        if key in spec["units"]:
            return dimension, key
        alias = spec.get("aliases", {}).get(key)
        if alias:
            return dimension, alias
    return None, None


def resolve(table, name):
    """단위가 어느 차원에 속하는지 찾는다. (차원, 표준심볼)을 돌려준다."""
    key = normalize(name)
    dimension, unit = lookup(table, key)
    if dimension:
        return dimension, unit
    # 영어 단위는 복수형으로 들어오는 경우가 더 많다.
    if key.endswith("es") and len(key) > 3:
        dimension, unit = lookup(table, key[:-2])
        if dimension:
            return dimension, unit
    if key.endswith("s") and len(key) > 2:
        return lookup(table, key[:-1])
    return None, None


def convert(table, value, src, dst):
    src_dim, src_unit = resolve(table, src)
    if src_dim is None:
        raise ValueError(f"모르는 단위다: {src}")

    dst_dim, dst_unit = resolve(table, dst)
    if dst_dim is None:
        raise ValueError(f"모르는 단위다: {dst}")

    if src_dim != dst_dim:
        raise ValueError(f"{src_unit}와 {dst_unit}는 서로 다른 차원이라 변환할 수 없다")

    spec = table[src_dim]

    if spec.get("affine"):
        # 온도는 눈금의 0점이 서로 달라서 배율만으로는 계산이 틀어진다.
        s, d = spec["units"][src_unit], spec["units"][dst_unit]
        in_base = value * s["scale"] + s["offset"]
        result = (in_base - d["offset"]) / d["scale"]
    else:
        in_base = value * spec["units"][src_unit]
        result = in_base / spec["units"][dst_unit]

    return result, src_dim, src_unit, dst_unit


def format_number(value):
    """작은 값의 유효숫자는 지키면서 부동소수점 찌꺼기만 털어낸다."""
    if value == 0:
        return "0"
    text = f"{round(value, 10):.10f}".rstrip("0").rstrip(".")
    return text if text else "0"


def print_units(table):
    labels = {
        "length": "길이",
        "mass": "무게",
        "volume": "부피",
        "area": "넓이",
        "speed": "속도",
        "data": "용량",
        "temperature": "온도",
    }
    for dimension, spec in table.items():
        label = labels.get(dimension, dimension)
        print(f"{label:4s} {', '.join(spec['units'].keys())}")


def main():
    parser = argparse.ArgumentParser(description="같은 차원의 단위끼리 값을 변환한다.")
    parser.add_argument("value", nargs="?", type=float, help="변환할 숫자")
    parser.add_argument("source", nargs="?", help="원래 단위 (예: km)")
    parser.add_argument("target", nargs="?", help="바꿀 단위 (예: mi)")
    parser.add_argument("--list", action="store_true", help="지원하는 단위를 출력한다")
    parser.add_argument("--json", action="store_true", help="문장 대신 JSON으로 출력한다")
    args = parser.parse_args()

    table = load_table()

    if args.list:
        print_units(table)
        return

    if args.value is None or not args.source or not args.target:
        parser.error("숫자, 원래 단위, 바꿀 단위를 모두 넣어야 한다")

    try:
        result, dimension, src_unit, dst_unit = convert(
            table, args.value, args.source, args.target
        )
    except ValueError as exc:
        sys.exit(f"오류: {exc}\n--list 로 지원하는 단위를 확인할 수 있다")

    if args.json:
        print(
            json.dumps(
                {
                    "value": args.value,
                    "from": src_unit,
                    "to": dst_unit,
                    "dimension": dimension,
                    "result": result,
                },
                ensure_ascii=False,
            )
        )
    else:
        print(f"{format_number(args.value)} {src_unit} = {format_number(result)} {dst_unit}")


if __name__ == "__main__":
    main()
