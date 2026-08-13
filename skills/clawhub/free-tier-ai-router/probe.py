#!/usr/bin/env python3
"""Probe EVERY model on EVERY key with a real completion. No assumptions."""
import json, os, subprocess, time, sys
from concurrent.futures import ThreadPoolExecutor

CAT = json.load(open(os.path.expanduser('~/ai_probe/catalog.json')))
def creds(p):
    return json.load(open(os.path.expanduser(f'~/.config/{p}/credentials.json')))

PROMPT = "Reply with exactly one word: OK"

def curl(url, headers, body, timeout=70):
    cmd = ['curl','-sS','-o','/dev/null' if False else '-','-w','\n__HTTP__%{http_code}__%{time_total}',
           url,'--max-time',str(timeout)]
    for h in headers: cmd += ['-H', h]
    if body is not None:
        cmd += ['-X','POST','--data-binary','@-']
        r = subprocess.run(cmd, input=body, capture_output=True, text=True)
    else:
        r = subprocess.run(cmd, capture_output=True, text=True)
    out = r.stdout
    code, t = '000', 0.0
    if '__HTTP__' in out:
        out, tail = out.rsplit('__HTTP__', 1)
        parts = tail.strip('_').split('__')
        code = parts[0]
        try: t = float(parts[1])
        except Exception: t = 0.0
    return out, code, t

def extract(txt):
    """Return (text, err) from any OpenAI/Gemini-ish payload."""
    try: d = json.loads(txt)
    except Exception: return None, 'unparseable'
    if isinstance(d, dict) and 'error' in d:
        e = d['error']
        return None, str(e.get('message', e))[:110] if isinstance(e, dict) else str(e)[:110]
    if isinstance(d, dict) and d.get('type','').endswith('error'):
        return None, str(d.get('message'))[:110]
    # Gemini
    try:
        parts = d['candidates'][0]['content']['parts']
        s = ''.join(p.get('text','') for p in parts).strip()
        if s: return s, None
    except Exception: pass
    # OpenAI-style
    try:
        m = d['choices'][0]['message']
        s = (m.get('content') or '')
        if isinstance(s, list):
            s = ''.join(c.get('text','') for c in s if isinstance(c, dict))
        s = (s or '').strip() or (m.get('reasoning') or '').strip()
        if s: return s, None
        return None, 'empty content'
    except Exception: pass
    if isinstance(d, dict) and 'message' in d and 'choices' not in d:
        return None, str(d['message'])[:110]
    return None, 'unknown shape'

def probe(prov, model):
    try:
        if prov == 'gemini':
            k = creds('gemini')['api_key']
            body = json.dumps({'contents':[{'parts':[{'text':PROMPT}]}],
                               'generationConfig':{'maxOutputTokens':2000}})
            url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent'
            txt, code, t = curl(url, ['Content-Type: application/json', f'X-goog-api-key: {k}'], body)
        else:
            cfg = {
             'mistral':    ('https://api.mistral.ai/v1/chat/completions',    creds('mistral')['api_key'], []),
             'openrouter': ('https://openrouter.ai/api/v1/chat/completions', creds('openrouter')['api_key'],
                            ['HTTP-Referer: https://arena.ai','X-Title: ArenaAgentMode']),
             'kilo':       ('https://api.kilo.ai/api/gateway/chat/completions', creds('kilo')['api_key'],
                            ['X-KILOCODE-FEATURE: arena-agent']),
             'cerebras':   ('https://api.cerebras.ai/v1/chat/completions',   creds('cerebras')['api_key'], []),
            }[prov]
            url, key, extra = cfg
            body = json.dumps({'model':model,'messages':[{'role':'user','content':PROMPT}],'max_tokens':2000})
            txt, code, t = curl(url, ['Content-Type: application/json', f'Authorization: Bearer {key}']+extra, body)
        s, err = extract(txt)
        return {'provider':prov,'model':model,'http':code,'sec':round(t,2),
                'ok': bool(s), 'sample': (s or '')[:60], 'error': err}
    except Exception as e:
        return {'provider':prov,'model':model,'http':'exc','sec':0,'ok':False,
                'sample':'','error':str(e)[:110]}

jobs = [(p, m) for p, ms in CAT.items() for m in ms]
print(f'probing {len(jobs)} models …', file=sys.stderr)
res = []
# modest concurrency: avoid self-inflicted rate limits
with ThreadPoolExecutor(max_workers=4) as ex:
    for i, r in enumerate(ex.map(lambda a: probe(*a), jobs), 1):
        res.append(r)
        mark = '✅' if r['ok'] else '❌'
        print(f"  [{i:3}/{len(jobs)}] {mark} {r['provider']:11} {r['model'][:46]:46} {r['http']:>4} {r['sec']:6.2f}s "
              f"{'' if r['ok'] else (r['error'] or '')[:44]}", file=sys.stderr)
json.dump(res, open(os.path.expanduser('~/ai_probe/results.json'), 'w'), indent=1)
ok = [r for r in res if r['ok']]
print(f"\nWORKING: {len(ok)}/{len(res)}", file=sys.stderr)
