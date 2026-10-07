"""Run the complete probe workflow as one artifact: identify, then deliver.

Stage 1 (identify) reads the upstream input and computes the identification
result. Stage 2 (deliver) feeds that result into the downstream operation,
writes the local business artifact under --output-dir, and -- when a delivery
target is configured -- performs the declared business action (sends the
message / registers or submits the record) and returns a delivery receipt.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
from uuid import uuid4


def load(module_name: str, path: Path):
    spec = importlib.util.spec_from_file_location(module_name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    parser.add_argument('--delivery-config', type=Path,
                        help='Optional JSON object with smtp/http delivery settings; CLAWHUB_* environment variables are also read.')
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    config = json.loads((here / 'config.json').read_text(encoding='utf-8'))
    up_cfg = json.loads((here / 'upstream/config.json').read_text(encoding='utf-8'))
    down_cfg = json.loads((here / 'downstream/config.json').read_text(encoding='utf-8'))
    up_op = load('upstream_operation', here / 'upstream/operation.py')
    up_val = load('upstream_validation', here / 'upstream/validation.py')
    down_op = load('downstream_operation', here / 'downstream/operation.py')
    down_val = load('downstream_validation', here / 'downstream/validation.py')
    request = json.loads(args.input.read_text(encoding='utf-8'))
    if not isinstance(request, dict) or set(request) != {up_cfg['input_name']}:
        raise ValueError('Request must contain exactly the declared input field: ' + up_cfg['input_name'])
    value = request[up_cfg['input_name']]
    up_val.validate_schema(value, up_cfg['input_schema'])
    identified = up_op.execute(up_cfg['variant_id'], up_cfg['role'], value)
    up_val.validate_schema(identified, up_cfg['output_schema'])
    down_val.validate_schema(identified, down_cfg['input_schema'])
    result = down_op.execute(down_cfg['variant_id'], down_cfg['role'], identified)
    down_val.validate_schema(result, down_cfg['output_schema'])
    root = args.output_dir.resolve()
    if root == Path(root.anchor):
        raise ValueError('Select a dedicated output directory, not a filesystem root')
    receipt = down_op.materialize_effect(down_cfg['variant_id'], root, result, uuid4().hex)
    target = Path(receipt['path']).resolve()
    target.relative_to(root)
    if not target.is_file():
        raise RuntimeError('Expected output file was not created')
    delivery_override = None
    if args.delivery_config is not None:
        delivery_override = json.loads(args.delivery_config.read_text(encoding='utf-8'))
        if not isinstance(delivery_override, dict):
            raise ValueError('--delivery-config must contain a JSON object')
    fixture = down_op.CONTRACTS[down_cfg['variant_id']].get('effect_fixture') or {}
    delivery = down_op.deliver_effect(down_cfg['variant_id'], result, fixture, receipt, delivery_override)
    response = {
        'identified': {up_cfg['output_name']: identified},
        'delivered': {down_cfg['output_name']: result},
        'effect': receipt,
        'delivery': delivery,
    }
    print(json.dumps(response, ensure_ascii=False))


if __name__ == '__main__':
    main()
