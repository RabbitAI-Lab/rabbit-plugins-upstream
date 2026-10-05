"""Run the single operation shipped in this package using local JSON input."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from uuid import uuid4

sys.path.insert(0, str(Path(__file__).resolve().parent))
import operation
from validation import validate_schema


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output-dir', type=Path)
    parser.add_argument('--delivery-config', type=Path,
                        help='Optional JSON object with smtp/http delivery settings; CLAWHUB_* environment variables are also read.')
    args = parser.parse_args()
    config = json.loads(Path(__file__).with_name('config.json').read_text(encoding='utf-8'))
    if config['role'] == 'downstream' and args.output_dir is None:
        parser.error('--output-dir is required for this operation')
    request = json.loads(args.input.read_text(encoding='utf-8'))
    if not isinstance(request, dict) or set(request) != {config['input_name']}:
        raise ValueError('Request must contain exactly the declared input field: ' + config['input_name'])
    value = request[config['input_name']]
    validate_schema(value, config['input_schema'])
    result = operation.execute(config['variant_id'], config['role'], value)
    validate_schema(result, config['output_schema'])
    response = {config['output_name']: result}
    if config['role'] == 'downstream':
        root = args.output_dir.resolve()
        if root == Path(root.anchor):
            raise ValueError('Select a dedicated output directory, not a filesystem root')
        receipt = operation.materialize_effect(config['variant_id'], root, result, uuid4().hex)
        target = Path(receipt['path']).resolve()
        target.relative_to(root)
        if not target.is_file():
            raise RuntimeError('Expected output file was not created')
        response['effect'] = receipt
        delivery_override = None
        if args.delivery_config is not None:
            delivery_override = json.loads(args.delivery_config.read_text(encoding='utf-8'))
            if not isinstance(delivery_override, dict):
                raise ValueError('--delivery-config must contain a JSON object')
        fixture = operation.CONTRACTS[config['variant_id']].get('effect_fixture') or {}
        response['delivery'] = operation.deliver_effect(
            config['variant_id'], result, fixture, receipt, delivery_override)
    print(json.dumps(response, ensure_ascii=False))


if __name__ == '__main__':
    main()
