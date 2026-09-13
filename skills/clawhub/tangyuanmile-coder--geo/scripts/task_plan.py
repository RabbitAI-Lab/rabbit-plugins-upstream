"""Price, confirm and track AIDSO product-diagnosis calls; never sends requests."""
import argparse
import json
import re
import uuid
from collections import OrderedDict
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

from common import *

CONFIRMATION_TEXT = '确认执行'
PRICE_SOURCE = '用户提供的《爱搜GEOAPI文档》价格表（2026-08-25）；提交前以爱搜实时价格页为准'
PRICE_CHECKED_AT = '2026-08-25'
CATALOG = OrderedDict([
    (('DOUBA', 0), {'平台': '豆包', '终端': '手机', '模式': '快速', '显示名称': '豆包·手机版', '单次积分': '0.8'}),
    (('TXYB', 0), {'平台': '元宝', '终端': '网页', '模式': '快速', '显示名称': '腾讯元宝·网页版', '单次积分': '0.8'}),
    (('TXYBA', 0), {'平台': '元宝', '终端': '手机', '模式': '快速', '显示名称': '腾讯元宝·手机版', '单次积分': '1'}),
    (('TYQWA', 0), {'平台': '千问', '终端': '手机', '模式': '快速', '显示名称': '千问·手机版', '单次积分': '1'}),
    (('TYQWA', 1), {'平台': '千问', '终端': '手机', '模式': '深度', '显示名称': '千问·手机版', '单次积分': '1'}),
])


def decimal_text(value):
    value = Decimal(str(value))
    if not value.is_finite() or value < 0:
        raise ValueError('单价必须为非负有效数')
    text = format(value.normalize(), 'f')
    return '0' if text == '-0' else text


def default_quote():
    return {
        'source': PRICE_SOURCE,
        'checked_at': PRICE_CHECKED_AT,
        'prices': {code + ':' + str(mode): item['单次积分'] for (code, mode), item in CATALOG.items()},
    }


def platform_catalog():
    return [
        {**item, 'API编码': code, 'thinking_enabled': mode,
         '价格来源': PRICE_SOURCE, '核对日期': PRICE_CHECKED_AT}
        for (code, mode), item in CATALOG.items()
    ]


def task_name(scope):
    label = '-'.join(filter(None, [scope.get('brand') or '无品牌', scope['name'],
                                   str(len(scope['questions'])) + '题',
                                   str(len(scope['combinations'])) + '组合', scope['date']]))
    return re.sub(r'[\\/:*?"<>|\s]+', '-', label).strip('-.')[:160]


def confirmation(plan_value):
    lines = [
        '# 爱搜 GEO 商品诊断任务提交前确认', '',
        '- 汇总任务名称：' + plan_value['task_name'],
        '- 汇总诊断 ID：' + plan_value['diagnosis_id'],
        '- 诊断品牌：' + (plan_value['scope'].get('brand') or '未设置'),
        '- 诊断商品／类目：' + plan_value['scope']['name'],
        '- 名称层级：' + ('类目' if plan_value['scope']['name_type'] == 'category' else '具体商品'),
        '- 问题数：' + str(len(plan_value['scope']['questions'])),
        '- 平台终端模式组合数：' + str(len(plan_value['scope']['combinations'])),
        '- 每题每组合采样次数：' + str(plan_value['scope']['repeats']),
        '- 原子对话总数：' + str(plan_value['task_count']),
        '- 确认报价积分：' + plan_value['total_points'],
        '- 计划摘要：' + plan_value['plan_hash'],
        '- 自动轮询：否；提交后凭汇总任务 ID、名称或原子任务 ID 查询',
        '- 预计耗时：每轮对话约 10～30 分钟', '',
        '## 问题清单', '',
    ]
    lines.extend(str(index) + '. ' + q['prompt'] for index, q in enumerate(plan_value['scope']['questions'], 1))
    lines.extend(['', '## 积分明细', ''])
    for item in plan_value['breakdown']:
        lines.append('- ' + item['display_name'] + ' · ' + item['mode_label'] + '：' +
                     str(item['calls']) + ' 次 × ' + item['unit_points'] + ' = ' +
                     item['subtotal_points'] + ' 积分')
    lines.extend(['', '> 价格来源：' + plan_value['quote']['source'],
                  '> 只有明确回复“确认执行”后才会调用接口提交并产生积分消耗。'])
    return '\n'.join(lines)


def plan(c, quote=None, diagnosis_id=None):
    validate_config(c)
    quote = quote or default_quote()
    if not isinstance(quote, dict) or not quote.get('source') or not quote.get('checked_at'):
        raise ValueError('报价必须附来源及核对时间')
    prices = quote.get('prices')
    if not isinstance(prices, dict):
        raise ValueError('报价缺少平台模式单价')
    tasks = []
    breakdown = OrderedDict()
    for q in c['questions']:
        for combo in c['combinations']:
            code = combo['name']
            mode = combo['thinking_enabled']
            key = code + ':' + str(mode)
            if (code, mode) not in CATALOG or key not in prices:
                raise ValueError('报价未覆盖已选商品诊断组合')
            unit = Decimal(decimal_text(prices[key]))
            catalog_item = CATALOG[(code, mode)]
            bucket = breakdown.setdefault(key, {
                'display_name': catalog_item['显示名称'], 'mode_label': catalog_item['模式'],
                'calls': 0, 'unit_points': decimal_text(unit),
            })
            for repeat in range(1, c['repeats'] + 1):
                body = {'prompt': q['prompt'], 'name': code, 'thinking_enabled': mode}
                bucket['calls'] += 1
                tasks.append({
                    'id': 'T' + str(len(tasks) + 1).zfill(5), 'question_id': q['id'], 'repeat': repeat,
                    'api_body': body,
                    'mcp_arguments': {'prompt': body['prompt'], 'name': body['name'], 'thinkingEnabled': mode},
                    'unit_points': decimal_text(unit), 'state': 'PLANNED', 'reqId': None,
                })
    for item in breakdown.values():
        item['subtotal_points'] = decimal_text(Decimal(item['unit_points']) * item['calls'])
    scope = {k: v for k, v in c.items() if k != 'sources'}
    signature = digest({'scope': scope, 'requests': [t['api_body'] for t in tasks], 'quote': quote})
    total = decimal_text(sum((Decimal(t['unit_points']) for t in tasks), Decimal('0')))
    result = {
        'schema_version': 2,
        'diagnosis_id': diagnosis_id or 'aidso-product-' + c['date'].replace('-', '') + '-' + uuid.uuid4().hex[:10],
        'task_name': task_name(scope),
        'created_at': datetime.now(timezone.utc).isoformat(),
        'status': 'PLANNED', 'plan_hash': signature, 'scope': scope, 'quote': quote,
        'price_source_checked_at': str(quote['checked_at']), 'total_points': total,
        'task_count': len(tasks), 'breakdown': list(breakdown.values()), 'approval': None, 'tasks': tasks,
    }
    result['confirmation_card'] = confirmation(result)
    return result


def verify_plan(p):
    expected = digest({'scope': p['scope'], 'requests': [t['api_body'] for t in p['tasks']], 'quote': p['quote']})
    if expected != p['plan_hash']:
        raise ValueError('计划已变化，须重新生成报价并取得对应授权')
    expected_plan = plan(p['scope'], p['quote'])
    immutable_fields = ('id', 'question_id', 'repeat', 'api_body', 'mcp_arguments', 'unit_points')
    actual_immutable = [{field: task[field] for field in immutable_fields} for task in p['tasks']]
    expected_immutable = [{field: task[field] for field in immutable_fields} for task in expected_plan['tasks']]
    if actual_immutable != expected_immutable:
        raise ValueError('原子任务或报价不符合计划范围')
    if p.get('task_count') != expected_plan['task_count'] or p.get('breakdown') != expected_plan['breakdown']:
        raise ValueError('任务数量或积分明细与计划不一致')
    for task in p['tasks']:
        body = task['api_body']
        if task['mcp_arguments'] != {'prompt': body['prompt'], 'name': body['name'],
                                    'thinkingEnabled': body['thinking_enabled']}:
            raise ValueError('MCP/API参数不一致')
    if p.get('total_points') != expected_plan['total_points']:
        raise ValueError('确认报价与原子任务金额不一致')


def approve(p, displayed_hash, evidence, quoted_points=None):
    verify_plan(p)
    if evidence.strip() != CONFIRMATION_TEXT:
        raise ValueError('必须提供精确确认文本“确认执行”')
    if displayed_hash != p['plan_hash']:
        raise ValueError('确认卡计划摘要与当前计划不一致')
    if quoted_points is not None and decimal_text(quoted_points) != p['total_points']:
        raise ValueError('确认卡积分与当前报价不一致')
    p['approval'] = {'plan_hash': displayed_hash, 'confirmation_text': CONFIRMATION_TEXT,
                     'quoted_points': p['total_points'], 'at': datetime.now(timezone.utc).isoformat()}
    p['status'] = 'CONFIRMED'


def begin(p, task_id):
    verify_plan(p)
    approval = p.get('approval')
    if not approval or approval.get('plan_hash') != p['plan_hash'] or \
            approval.get('confirmation_text') != CONFIRMATION_TEXT or \
            approval.get('quoted_points') != p['total_points']:
        raise ValueError('必须先取得本计划的用户授权')
    if any(t['state'] in ('UNKNOWN', 'ERROR', 'SENDING') for t in p['tasks']):
        raise ValueError('存在未明确受理或异常任务，停止剩余提交并核实')
    task = next(t for t in p['tasks'] if t['id'] == task_id)
    if task['state'] != 'PLANNED':
        raise ValueError('此任务不可重复提交')
    task['state'] = 'SENDING'
    p['status'] = 'PARTIAL'
    return task['mcp_arguments']


def record(p, task_id, response):
    task = next(t for t in p['tasks'] if t['id'] == task_id)
    if task['state'] != 'SENDING':
        raise ValueError('只能记录刚发起的原子提交')
    if response is None:
        task['state'] = 'UNKNOWN'
        p['status'] = 'PARTIAL'
        return
    if response.get('code') == 200 and isinstance(response.get('data'), str) and response['data'].strip():
        if any(t['reqId'] == response['data'] for t in p['tasks']):
            raise ValueError('服务返回重复reqId，需核验')
        task['reqId'] = response['data']
        task['state'] = 'SUBMITTED'
    else:
        task['state'] = 'UNKNOWN' if response.get('code') not in (400, 401, 405, 406, 429) else 'ERROR'
        task['code'] = response.get('code')
    states = [t['state'] for t in p['tasks']]
    p['status'] = 'SUBMITTED' if all(x == 'SUBMITTED' for x in states) else 'PARTIAL'


def registry_path(value, must_exist=False):
    workspace = Path.cwd().resolve()
    root = (workspace / '.aidso-geo' / 'tasks').resolve()
    path = Path(value)
    path = (path if path.is_absolute() else workspace / path).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise ValueError('任务台账必须位于当前工作区 .aidso-geo/tasks/ 下') from exc
    if must_exist and not path.is_file():
        raise ValueError('任务台账不存在')
    return path


def canonical_points(value):
    try:
        return decimal_text(Decimal(str(value)))
    except InvalidOperation as exc:
        raise ValueError('报价积分格式无效') from exc


def summary(p):
    counts = {}
    for task in p['tasks']:
        counts[task['state']] = counts.get(task['state'], 0) + 1
    return {'diagnosis_id': p['diagnosis_id'], 'task_name': p['task_name'], 'status': p['status'],
            'total_points': p['total_points'], 'task_count': p['task_count'], 'task_states': counts}


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('list-platforms')
    q = sub.add_parser('plan')
    q.add_argument('--config', required=True)
    q.add_argument('--quote')
    q.add_argument('--out', required=True)
    q.add_argument('--format', choices=('json', 'confirmation'), default='json')
    q = sub.add_parser('approve')
    q.add_argument('--manifest', required=True)
    q.add_argument('--displayed-hash', required=True)
    q.add_argument('--quoted-points', required=True)
    q.add_argument('--confirmation-text')
    q.add_argument('--evidence-file')
    for command in ('begin', 'record', 'unknown'):
        q = sub.add_parser(command)
        q.add_argument('--manifest', required=True)
        q.add_argument('--task-id', required=True)
        if command == 'record':
            q.add_argument('--response', required=True)
    q = sub.add_parser('result')
    q.add_argument('--manifest', required=True)
    q.add_argument('--task-id', required=True)
    q.add_argument('--response', required=True)
    q.add_argument('--out', required=True)
    q = sub.add_parser('summary')
    q.add_argument('--manifest', required=True)
    q = sub.add_parser('find')
    q.add_argument('query')
    args = parser.parse_args()
    try:
        if args.command == 'list-platforms':
            print(json.dumps(platform_catalog(), ensure_ascii=False, indent=2))
            return 0
        if args.command == 'plan':
            output = registry_path(args.out)
            if output.exists():
                raise ValueError('拒绝覆盖已有任务台账')
            p = plan(read_json(args.config), read_json(args.quote) if args.quote else None)
            write_json(output, p)
            print(p['confirmation_card'] if args.format == 'confirmation' else json.dumps(summary(p), ensure_ascii=False))
            return 0
        if args.command == 'find':
            root = Path.cwd() / '.aidso-geo' / 'tasks'
            matches = []
            for path in root.rglob('*.json') if root.is_dir() else []:
                p = read_json(path)
                ids = {p.get('diagnosis_id'), p.get('task_name'), *[t.get('reqId') for t in p.get('tasks', [])]}
                if args.query in ids:
                    matches.append(summary(p))
            if len(matches) != 1:
                raise ValueError('未找到唯一任务，请使用汇总任务 ID、精确名称或原子任务 ID')
            print(json.dumps(matches[0], ensure_ascii=False))
            return 0
        manifest = registry_path(args.manifest, must_exist=True)
        p = read_json(manifest)
        if args.command == 'approve':
            if bool(args.confirmation_text) == bool(args.evidence_file):
                raise ValueError('请仅提供一种确认文本来源')
            evidence = args.confirmation_text or Path(args.evidence_file).read_text()
            approve(p, args.displayed_hash, evidence, canonical_points(args.quoted_points))
        elif args.command == 'begin':
            request = begin(p, args.task_id)
            write_json(manifest, p)
            print(json.dumps(request, ensure_ascii=False))
            return 0
        elif args.command in ('record', 'unknown'):
            record(p, args.task_id, read_json(args.response) if args.command == 'record' else None)
        elif args.command == 'summary':
            print(json.dumps(summary(p), ensure_ascii=False))
            return 0
        else:
            verify_plan(p)
            task = next(t for t in p['tasks'] if t['id'] == args.task_id)
            if task['state'] not in ('SUBMITTED', 'ING', 'SUCCESS'):
                raise ValueError('只查询有明确原子任务 ID 的已提交任务')
            response = read_json(args.response)
            data = response.get('data', {})
            if response.get('code') != 200 or not isinstance(data, dict):
                raise ValueError('本次查询失败，保留原任务，不重新提交')
            if data.get('prompt') != task['api_body']['prompt']:
                raise ValueError('查询结果问题与原任务不一致')
            task['state'] = data.get('status', 'UNKNOWN')
            if task['state'] == 'SUCCESS':
                if not data.get('fetch_time'):
                    raise ValueError('结果无采样时间，须人工核验')
                write_json(args.out, {'reqId': task['reqId'], **task['api_body'], 'code': 200, 'data': data})
            print(json.dumps({'task_id': task['id'], 'status': task['state']}, ensure_ascii=False))
        write_json(manifest, p)
        return 0
    except (ValueError, OSError, KeyError) as exc:
        print('ERROR: ' + str(exc), file=__import__('sys').stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
