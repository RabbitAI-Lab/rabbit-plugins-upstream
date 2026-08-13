#!/usr/bin/env python3
"""Find the REAL sustained rate limit per provider: fire N sequential calls, count 429s.
Deliberately small N — the goal is to measure headroom, not to burn the quota."""
import json, os, subprocess, time, sys

def creds(p): return json.load(open(os.path.expanduser(f'~/.config/{p}/credentials.json')))

TARGETS = [
    ('gemini',     'gemini-3.5-flash-lite'),
    ('gemini',     'gemini-3.6-flash'),
    ('mistral',    'mistral-small-latest'),
    ('mistral',    'mistral-large-latest'),
    ('openrouter', 'nvidia/nemotron-3-super-120b-a12b:free'),
    ('openrouter', 'inclusionai/ling-3.0-flash:free'),
    ('kilo',       'kilo-auto/free'),
    ('kilo',       'inclusionai/ling-3.0-flash:free'),
]
N = 8

def call(prov, model):
    body_common = json.dumps({'model':model,'messages':[{'role':'user','content':'hi'}],'max_tokens':800})
    if prov=='gemini':
        k=creds('gemini')['api_key']
        url=f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent'
        h=['Content-Type: application/json',f'X-goog-api-key: {k}']
        body=json.dumps({'contents':[{'parts':[{'text':'hi'}]}],'generationConfig':{'maxOutputTokens':800}})
    else:
        url,key,extra={
         'mistral':('https://api.mistral.ai/v1/chat/completions',creds('mistral')['api_key'],[]),
         'openrouter':('https://openrouter.ai/api/v1/chat/completions',creds('openrouter')['api_key'],
                       ['HTTP-Referer: https://arena.ai','X-Title: ArenaAgentMode']),
         'kilo':('https://api.kilo.ai/api/gateway/chat/completions',creds('kilo')['api_key'],
                 ['X-KILOCODE-FEATURE: arena-agent']),
        }[prov]
        h=['Content-Type: application/json',f'Authorization: Bearer {key}']+extra
        body=body_common
    # capture headers too — providers often advertise their limits
    p=subprocess.run(['curl','-sS','-D','-','-o','/dev/null','-w','%{http_code}',url,
                      '-X','POST','--data-binary','@-','--max-time','40']+
                     [x for hh in h for x in ('-H',hh)],
                     input=body,capture_output=True,text=True)
    out=p.stdout
    code=out.strip().split('\n')[-1].strip()
    hdrs={}
    for line in out.split('\n'):
        l=line.lower()
        if any(t in l for t in ('ratelimit','retry-after','x-request-limit','quota')):
            if ':' in line:
                k2,v=line.split(':',1); hdrs[k2.strip().lower()]=v.strip()
    return code, hdrs

report={}
for prov,model in TARGETS:
    codes=[]; seen={}
    t0=time.time()
    for i in range(N):
        c,h=call(prov,model); codes.append(c); seen.update(h)
    dur=time.time()-t0
    ok=sum(1 for c in codes if c=='200')
    r429=sum(1 for c in codes if c=='429')
    rps=N/dur if dur else 0
    report[f'{prov}/{model}']={'ok':ok,'n':N,'http429':r429,
        'codes':codes,'sec':round(dur,1),'req_per_s':round(rps,2),'limit_headers':seen}
    print(f"  {prov:11} {model[:40]:40} {ok}/{N} ok, {r429}x429, {dur:.1f}s ({rps:.1f} req/s)", file=sys.stderr)
    if seen:
        for k2,v in list(seen.items())[:4]:
            print(f"       ↳ {k2}: {v}", file=sys.stderr)
    time.sleep(2)
json.dump(report, open(os.path.expanduser('~/ai_probe/ratelimits.json'),'w'), indent=1)
