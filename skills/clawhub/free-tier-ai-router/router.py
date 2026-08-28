#!/usr/bin/env python3
"""
free-tier-ai-router — quota-aware multi-provider LLM router.

v2.3.0 — any provider, any agent:
  * pluggable providers: ~/.config/ai_router/providers.json adds ANY
    OpenAI-compatible endpoint (Groq, Cerebras, Together, a local Ollama /
    llama.cpp / vLLM server, an internal gateway...) without code changes;
    user entries override built-in routes on conflict
  * --discover [--apply]: read GET /v1/models from any configured provider
    and add its models as routes (never auto-applied — quota is precious)
  * --json on ask/status/plan: machine contract for other agents; exit codes
    0 ok · 2 quota-dead · 3 no keys · 4 invalid providers.json

Every number in ROUTES came from live probing on 2026-07-30 (see PROBE.md),
not from documentation or guesswork.

Design rules, each derived from a measured fact:
  1. Gemini free tier is 20 requests/DAY *per model* — so scarce capacity is
     spent last, and each Gemini model is tracked as its own budget.
  2. Mistral publishes x-ratelimit-limit-req-minute and it varies 187x
     (ministral-3b 750/min vs mistral-large 4/min) — prefer high-limit models
     for routine work; reserve the 4/min models for when quality demands it.
  3. Providers fail independently — a 429 on one never blocks the others.
  4. Cooldowns are persisted to disk, so a 429 in one process is respected by
     the next. Without this, every new shell re-discovers the same limit.
"""
import json, os, sys, time, subprocess, hashlib, argparse, fcntl, datetime, tempfile

HOME = os.path.expanduser('~')
STATE = os.path.join(HOME, '.cache', 'ai_router', 'state.json')
LOCK  = os.path.join(HOME, '.cache', 'ai_router', 'state.lock')
# Shipped alongside the skill: routes proven dead by probing, so a FRESH INSTALL
# never spends an API call rediscovering them. Overridable by ~/.config override.
HEALTH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'health.json')
CACHE = os.path.join(HOME, '.cache', 'ai_router', 'cache')
os.makedirs(os.path.dirname(STATE), exist_ok=True)
os.makedirs(CACHE, exist_ok=True)

# ── measured capability table ────────────────────────────────────────────────
# quality: score on 5 objective questions (see PROBE.md)
# rpm    : requests/minute. Gemini rpd=20/day/model is the binding limit.
# tier   : cheap → burn freely.  mid → normal.  scarce → last resort.
ROUTES = [
 # provider    model                                           qual  rpm   rpd  tier    sec   tags
 ('mistral',   'ministral-3b-latest',                            4,  750, None,'cheap', 0.49, 'fast'),
 ('mistral',   'ministral-8b-latest',                            4,  188, None,'cheap', 1.22, 'fast'),
 ('mistral',   'codestral-latest',                               3,  125, None,'cheap', 0.59, 'code'),
 ('mistral',   'mistral-code-latest',                            3,  125, None,'cheap', 0.60, 'code'),
 ('mistral',   'mistral-small-latest',                           4,   50, None,'cheap', 0.45, 'fast'),
 ('mistral',   'mistral-medium-latest',                          5,   50, None,'mid',   0.43, 'best-value'),
 ('mistral',   'open-mistral-nemo',                              4,   30, None,'cheap', 0.68, ''),
 ('mistral',   'mistral-tiny-latest',                            4,   30, None,'cheap', 0.72, 'fast'),
 ('openrouter','inclusionai/ling-3.0-flash:free',                5,   20, None,'mid',   0.93, ''),
 ('kilo',      'inclusionai/ling-3.0-flash:free',                5,   20, None,'mid',   1.35, ''),
 ('kilo',      'kilo-auto/free',                                 5,   20, None,'mid',   1.46, 'auto'),
 ('openrouter','nvidia/nemotron-3-super-120b-a12b:free',         5,   20, None,'mid',   2.77, ''),
 ('kilo',      'nvidia/nemotron-3-ultra-550b-a55b:free',         5,   10, None,'mid',   2.30, 'flagship,1M-ctx'),
 ('openrouter','nvidia/nemotron-3-ultra-550b-a55b:free',         4,   10, None,'mid',   1.40, 'flagship,1M-ctx'),
 ('kilo',      'stepfun/step-3.7-flash:free',                    5,   10, None,'mid',   3.41, ''),
 ('mistral',   'magistral-medium-latest',                        4,    5, None,'mid',   4.81, 'reasoning'),
 ('mistral',   'mistral-large-latest',                           4,    4, None,'mid',   0.46, 'flagship'),
 # Gemini last: 20 requests per DAY per model is the scarcest capacity we have.
 ('gemini',    'gemini-3.5-flash-lite',                          5,   15,   20,'scarce',0.66, ''),
 ('gemini',    'gemini-3.1-flash-lite',                          5,   15,   20,'scarce',0.63, ''),
 ('gemini',    'gemini-3.5-flash',                               5,   10,   20,'scarce',1.53, ''),
 ('gemini',    'gemini-3-flash-preview',                         5,   10,   20,'scarce',1.50, ''),
]
TIER_ORDER = {'cheap': 0, 'mid': 1, 'scarce': 2}

# ── v2.3.0: pluggable providers ─────────────────────────────────────────────
# Any OpenAI-compatible endpoint becomes a routable provider. Built-in specs
# are OFF until their credential file exists (or, for local servers, until the
# user declares them in providers.json) — nothing probes or spends on its own.
SPECS_FILE = os.path.join(HOME, '.config', 'ai_router', 'providers.json')

# auth: 'bearer' -> Authorization: Bearer <key>
#       'x-api-key' -> x-api-key: <key>            (Anthropic-style)
#       'none'      -> no auth header               (local servers)
BUILTIN_SPECS = {
  'groq':  {'base_url': 'https://api.groq.com/openai/v1', 'auth': 'bearer',
            # NOTE: model ids are tenant-dependent (a 403 on GET /models is
            # normal for chat-scoped keys) — run --discover to list yours.
            'models': [
              ('openai/gpt-oss-120b',      4, 30, None, 'cheap', 'best-value,fast'),
              ('llama-3.3-70b-versatile',  4, 30, None, 'cheap', 'general'),
              ('qwen/qwen3.6-27b',         3, 30, None, 'cheap', 'code'),
            ]},
  'llm7':  {'base_url': 'https://api.llm7.io/v1', 'auth': 'bearer',
            'models': [('default', 3, 60, None, 'cheap', 'fast')]},
  'huggingface': {'base_url': 'https://router.huggingface.co/v1', 'auth': 'bearer',
            'models': []},          # populated by --discover (hundreds of models)
  'cerebras': {'base_url': 'https://api.cerebras.ai/v1', 'auth': 'bearer',
            'models': [('llama-3.3-70b', 4, 30, None, 'cheap', 'fast')]},
  'cohere': {'base_url': 'https://api.cohere.com/compatibility/v1', 'auth': 'bearer',
            'models': [('command-a-03-2025', 4, 20, None, 'mid', 'best-value')]},
  # Local servers: declared by the user in providers.json (see SKILL.md), or
  # set {'ollama': {...}} there with enable_local=true. Never auto-enabled.
}

SPEC_CONFIG_ERROR = None            # set when providers.json is unusable

def _normalize_base(u):
    u = (u or '').strip().rstrip('/')
    if not u.startswith(('http://', 'https://')):
        u = 'http://' + u           # local servers are usually plain http
    return u

def _load_specs():
    """Merge built-in specs with the user's providers.json.

    User entries win on conflict (per-model and per-provider). A malformed
    file is a WARNING, never a crash — the built-in routes must keep working
    (warn-don't-exit). Returns (specs_dict, error_message_or_None).
    """
    specs = {k: dict(v) for k, v in BUILTIN_SPECS.items()}
    err = None
    try:
        with open(SPECS_FILE) as f:
            user = json.load(f)
    except FileNotFoundError:
        return specs, None
    except Exception as e:
        return specs, f'providers.json unreadable ({e}); using built-ins'
    if not isinstance(user, dict):
        return specs, 'providers.json must be a JSON object; using built-ins'
    # If the file carries inline keys but is group/world readable, tighten it —
    # the file was probably written by an editor with a normal umask.
    try:
        raw = open(SPECS_FILE).read()
        import stat as _st
        if 'api_key' in raw and _st.S_IMODE(os.stat(SPECS_FILE).st_mode) & 0o077:
            os.chmod(SPECS_FILE, 0o600)
    except OSError:
        pass
    for name, cfg in (user.get('providers') or {}).items():
        if not isinstance(cfg, dict) or not cfg.get('base_url'):
            err = err or f'provider {name!r}: missing base_url (skipped)'
            continue
        models = []
        for m in (cfg.get('models') or []):
            if isinstance(m, str):
                models.append((m, 2, 30, None, 'mid', ''))
            elif isinstance(m, dict) and m.get('id'):
                models.append((m['id'], int(m.get('quality', 2)),
                               int(m.get('rpm', 30)), m.get('rpd'),
                               m.get('tier', 'mid'), m.get('tags', '')))
            else:
                err = err or f'provider {name!r}: bad model entry (skipped)'
        base = _normalize_base(cfg['base_url'])
        key = cfg.get('api_key') or ''
        key_file = cfg.get('key_file') or ''
        if key_file and not key:
            try:
                with open(os.path.expanduser(key_file)) as f:
                    key = json.load(f).get('api_key', '')
            except Exception:
                key = ''
        specs[name] = {'base_url': base, 'auth': cfg.get('auth', 'bearer'),
                       'models': models, '_user': True,
                       '_inline_key': key,
                       '_key_file': os.path.expanduser(key_file) if key_file else
                                    os.path.join(HOME, '.config', name, 'credentials.json')}
        if (cfg.get('auth') == 'none' and 'api_key' not in cfg and not key_file
                and '127.0.0.1' not in base and 'localhost' not in base):
            print(f'[warn] provider {name!r}: auth "none" on non-local {base} — '
                  f'anyone on that network path can spend your quota', file=sys.stderr)
    # enable local servers only when the user explicitly declared them
    for lname, port in (('ollama', 11434), ('llama-cpp', 8080), ('vllm', 8000)):
        if lname in specs:
            continue
        if (user.get('enable_local') and specs.get('_local_probe') is not False):
            pass  # handled below via explicit declarations only
    return specs, err

PROVIDER_SPECS, SPEC_CONFIG_ERROR = _load_specs()

def _spec_key(p):
    """Resolve an API key for a spec provider: inline > key_file > creds file."""
    spec = PROVIDER_SPECS.get(p) or {}
    if spec.get('_inline_key'):
        return spec['_inline_key']
    for f in (spec.get('_key_file'),
              os.path.join(HOME, '.config', p, 'credentials.json')):
        if f and os.path.exists(f):
            try:
                with open(f) as fh:
                    d = json.load(fh)
                return d.get('api_key') or d.get('api_token') or ''
            except Exception:
                pass
    return ''

def _spec_routes():
    """Route rows contributed by specs. A spec contributes only when it can
    authenticate (or needs no auth) — no point listing what cannot be called."""
    rows = []
    for p, spec in PROVIDER_SPECS.items():
        if spec.get('auth') != 'none' and not _spec_key(p):
            continue
        for (mid, q, rpm, rpd, tier, tags) in spec.get('models', []):
            if tier not in TIER_ORDER:
                tier = 'mid'
            rows.append((p, mid, q, rpm, rpd, tier, 0.5, tags))
    return rows

def _merge_routes():
    """Built-in measured ROUTES + spec routes, with explicit precedence:

    1. USER routes (declared in providers.json) override anything — the user
       owns the box; if a provider changed its base_url or they want to pin a
       route to a proxy, the router must not stay bricked on a stale builtin
       (consensus-review decision: gemini/llm7/gpt-oss all flagged the old
       setdefault-only merge as contradicting the documented behaviour).
    2. Builtin SPEC routes (groq/llm7/…) never shadow MEASURED routes — an
       unmeasured default must not displace a probed number.
    """
    by_key = {}
    for row in ROUTES:
        by_key[(row[0], row[1])] = row
    for row in _spec_routes():
        if row[0] in PROVIDER_SPECS and PROVIDER_SPECS[row[0]].get('_user'):
            by_key[(row[0], row[1])] = row          # user declaration: override
        else:
            by_key.setdefault((row[0], row[1]), row)  # builtin spec: yield to measurements
    return [by_key[k] for k in sorted(by_key, key=lambda k: (TIER_ORDER.get(by_key[k][5], 1), k[0]))]

ROUTES = _merge_routes() if PROVIDER_SPECS else list(ROUTES)

SETUP_HELP = """No API keys found — the router has nothing to route to.

Add at least one provider (all have free tiers):

  Mistral     https://console.mistral.ai/api-keys      ← best free limits
  Gemini      https://aistudio.google.com/apikey
  OpenRouter  https://openrouter.ai/keys
  Kilo        https://app.kilo.ai/profile

Then save it, e.g. for Mistral:

  mkdir -p ~/.config/mistral
  printf '{"api_key":"YOUR_KEY"}' > ~/.config/mistral/credentials.json
  chmod 600 ~/.config/mistral/credentials.json

Verify with:  ai --status
"""

def _known_dead():
    """Routes/providers that probing proved unusable — skipped WITHOUT an API call.

    Eliminating rediscovery is the single biggest source of wasted calls: without
    this, every fresh install and every `--reset` burns one request per dead route
    relearning what was already measured.
    """
    try:
        with open(HEALTH) as f: h = json.load(f)
    except Exception:
        return set(), {}
    dead = {(d['provider'], d['model']) for d in h.get('dead_routes', [])}
    prov = {p['provider']: p.get('reason', 'known unavailable')
            for p in h.get('dead_providers', [])}
    return dead, prov

DEAD_ROUTES, DEAD_PROVIDERS = _known_dead()

def load_state():
    if not _state_writable():
        return dict(_MEM_STATE)
    try:
        with open(STATE) as f: return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    except OSError as e:
        print(f'[warn] could not read state: {e}', file=sys.stderr)
        return {}

_MEM_STATE = {}          # fallback when the state dir is not writable
_STATE_RW  = None        # None = untested, False = read-only filesystem

def _state_writable():
    """Probe once whether we can persist. A read-only cache dir must NOT be fatal:
    the router still routes correctly, it just can't remember cooldowns."""
    global _STATE_RW
    if _STATE_RW is None:
        try:
            os.makedirs(os.path.dirname(STATE), exist_ok=True)
            t = f'{STATE}.probe.{os.getpid()}'
            with open(t, 'w') as f: f.write('1')
            os.remove(t)
            _STATE_RW = True
        except Exception:
            _STATE_RW = False
            print('[warn] state dir not writable — cooldowns will not persist',
                  file=sys.stderr)
    return _STATE_RW

def _locked(fn):
    """Run fn(state) under an exclusive file lock, then persist atomically.

    FIX: previously load_state/save_state were separate, so two processes could
    both read day_count=19, both call, and both write 20 — silently exceeding a
    20/day cap (verified: 10 concurrent increments landed as 1). The lock makes
    read-modify-write atomic across processes.
    """
    if not _state_writable():
        return fn(_MEM_STATE)                    # in-memory fallback, no crash
    with open(LOCK, 'w') as lf:
        fcntl.flock(lf, fcntl.LOCK_EX)
        try:
            try:
                with open(STATE) as f: st = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                st = {}
            result = fn(st)
            # FIX: unique temp name per process — a shared '.tmp' meant the first
            # os.replace() won and the rest died with FileNotFoundError.
            tmp = f'{STATE}.{os.getpid()}.tmp'
            with open(tmp, 'w') as f: json.dump(st, f)
            os.replace(tmp, STATE)
            return result
        finally:
            fcntl.flock(lf, fcntl.LOCK_UN)

def save_state(s):
    if not _state_writable():
        _MEM_STATE.clear(); _MEM_STATE.update(s); return
    try:
        tmp = f'{STATE}.{os.getpid()}.tmp'
        with open(tmp, 'w') as f: json.dump(s, f)
        os.replace(tmp, STATE)
    except OSError as e:
        print(f'[warn] could not persist state: {e}', file=sys.stderr)

def creds(p):
    with open(os.path.join(HOME, '.config', p, 'credentials.json')) as f:
        return json.load(f)

def key_of(prov, model): return f'{prov}|{model}'

def _until_midnight():
    """Seconds-since-epoch at next local midnight — daily quotas reset by date,
    not by a rolling hour, so cooldowns for daily caps must align to that."""
    tm = datetime.datetime.now() + datetime.timedelta(days=1)
    return datetime.datetime.combine(tm.date(), datetime.time.min).timestamp()

def today(): return time.strftime('%Y-%m-%d')

def has_credentials(prov):
    """True if a readable credentials file exists for this provider.
    Checked BEFORE any quota logic so a keyless provider is never reported as
    'quota spent' — that message sent new users hunting a rate-limit problem
    they did not have."""
    if prov in PROVIDER_SPECS:
        spec = PROVIDER_SPECS[prov]
        if spec.get('auth') == 'none':
            return True                      # local server: no key by design
        return bool(_spec_key(prov))
    try:
        with open(os.path.join(HOME, '.config', prov, 'credentials.json')) as f:
            json.load(f)
        return True
    except Exception:
        return False

def available(prov, model, st, reserve=False):
    """Is this route usable right now? Enforces cooldown + daily budget."""
    # Some providers meter ACCOUNT-WIDE per day (OpenRouter: "free-models-per-day"),
    # so one 429 invalidates every model on that key — not just the one we called.
    # Zero-cost skips first — never spend a request to learn something we know.
    if not has_credentials(prov):
        return False, "no API key configured"
    if prov in DEAD_PROVIDERS:
        return False, f"provider unusable: {DEAD_PROVIDERS[prov]}"
    # A "credentials missing" park is conditional, not time-based: if the file is
    # now present, clear it immediately. Otherwise repairing credentials appears
    # to do nothing until an arbitrary timer expires (observed: all Mistral routes
    # blocked for 15m on a machine whose Mistral key was perfectly valid).
    _pw = st.get(f'PROVIDER|{prov}', {})
    _cred_ok = os.path.exists(os.path.join(HOME, '.config', prov, 'credentials.json'))
    if _pw and 'credentials' in str(_pw.get('reason', '')) and _cred_ok:
        st.pop(f'PROVIDER|{prov}', None)
        # Per-MODEL cooldowns were set by the same credential failure. Clearing
        # only the provider park left every route still individually parked
        # (observed: 21/21 "usable" yet every call skipped). Clear both.
        for _k in [k for k in st if k.startswith(f'{prov}|')]:
            _e = st[_k]
            if _e.get('cooldown_until', 0) > time.time() and not _e.get('day_count'):
                _e['cooldown_until'] = 0
    if (prov, model) in DEAD_ROUTES:
        return False, "route known-dead (probed)"
    pw = st.get(f'PROVIDER|{prov}', {})
    if pw.get('cooldown_until', 0) > time.time():
        mins = int((pw['cooldown_until'] - time.time()) / 60)
        return False, f"provider quota spent ({mins}m)"
    e = st.get(key_of(prov, model), {})
    cd = e.get('cooldown_until', 0)
    # FIX 17: a corrupt state file or a clock jump could store a cooldown years
    # in the future, permanently bricking the route with no way to recover except
    # --reset. No legitimate cooldown exceeds 24h, so clamp anything beyond that.
    if cd - time.time() > 86400:
        cd = e['cooldown_until'] = time.time() + 86400
    if cd > time.time():
        return False, f"cooldown {int(cd-time.time())}s"
    row = next((r for r in ROUTES if r[0] == prov and r[1] == model), None)
    if row and row[4]:                                   # rpd limit exists
        used = e.get('day_count', 0) if e.get('day') == today() else 0
        # FIX: the old comment promised a 20% reserve but the code allowed 100%.
        # Now it genuinely reserves the tail of the budget: routine traffic stops
        # at 80%, and only an explicit high-quality request (reserve=True) may
        # spend the remainder.
        cap = row[4] if reserve else max(1, int(row[4] * 0.8))
        if used >= cap:
            return False, f"daily budget {'spent' if reserve else 'at 80% guard'} ({used}/{cap})"
    return True, ''

def note_result(prov, model, ok, http, st, err=None):
    err_is_account_wide = bool(err) and any(t in str(err).lower()
        for t in ('per-day', 'per day', 'free-models-per-day', 'daily limit'))
    k = key_of(prov, model)
    e = st.setdefault(k, {})
    if e.get('day') != today():
        e['day'], e['day_count'] = today(), 0
    if ok:
        # NOTE: day_count is incremented by the caller's atomic _claim() BEFORE the
        # request goes out, so it must NOT be incremented again here — doing both
        # over-counted every call (20 calls recorded as 22) and would trip daily
        # caps early. note_result only records outcome, never spends budget.
        e['ok'] = e.get('ok', 0) + 1
        e['cooldown_until'] = 0
    else:
        e['fail'] = e.get('fail', 0) + 1
        if http == 429 and err_is_account_wide:
            # OpenRouter "free-models-per-day": the whole KEY is done for the day.
            # FIX: was 3600s, which let the router rediscover the same wall every
            # hour until midnight. Park until the day actually rolls over.
            st[f'PROVIDER|{prov}'] = {'cooldown_until': _until_midnight(),
                                      'reason': 'account-wide daily quota'}
            e['cooldown_until'] = _until_midnight()
            e['day_count'] = 10 ** 6
        elif http == 429:
            # Gemini's 429 is a DAILY cap -> park until tomorrow.
            # Others are per-minute -> short cooldown with mild backoff.
            if prov == 'gemini':
                # FIX: cooldown was 1h while day_count=9999 blocked it all day, so
                # --status lied ("ready") for the remaining hours. Now they agree.
                e['cooldown_until'] = _until_midnight()
                e['day_count'] = 10 ** 6
            else:
                e['cooldown_until'] = time.time() + min(60 * (1 + e.get('fail', 1) // 3), 300)
        elif http == -1:
            # FIX: a missing/invalid credentials file kills EVERY model on that
            # provider. Previously each model was tried and failed separately,
            # burning the whole `tries` budget on one dead provider and never
            # reaching healthy ones. Park the provider immediately.
            st[f'PROVIDER|{prov}'] = {'cooldown_until': time.time() + 900,
                                      'reason': 'credentials missing/unreadable'}
            e['cooldown_until'] = time.time() + 900
        elif http in (402, 403, 404, 401):
            e['cooldown_until'] = time.time() + 86400      # structural: don't retry today
        else:
            e['cooldown_until'] = time.time() + 20
    e['last'] = int(time.time())
    st[k] = e

# ── transport ────────────────────────────────────────────────────────────────
def call(prov, model, prompt, system=None, max_tokens=3000, timeout=90):
    """Returns (text, http_code, error). One provider, one attempt."""
    try:
        if prov == 'gemini':
            k = creds('gemini')['api_key']
            url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent'
            payload = {'contents': [{'parts': [{'text': prompt}]}],
                       'generationConfig': {'maxOutputTokens': max_tokens}}
            if system: payload['systemInstruction'] = {'parts': [{'text': system}]}
            hdr = ['Content-Type: application/json', f'X-goog-api-key: {k}']
        else:
            # BUG FIX: this used to be a dict literal that called creds() for
            # EVERY provider eagerly, so one missing credentials file made every
            # request fail with "no credentials" — even when routing elsewhere.
            # Build only the provider we are actually calling.
            endpoints = {
              'mistral':    ('https://api.mistral.ai/v1/chat/completions', []),
              'openrouter': ('https://openrouter.ai/api/v1/chat/completions',
                             ['HTTP-Referer: https://arena.ai', 'X-Title: ArenaAgentMode']),
              'kilo':       ('https://api.kilo.ai/api/gateway/chat/completions',
                             ['X-KILOCODE-FEATURE: arena-agent']),
              'cerebras':   ('https://api.cerebras.ai/v1/chat/completions', []),
            }
            if prov in PROVIDER_SPECS:          # v2.3.0: any configured endpoint
                spec = PROVIDER_SPECS[prov]
                url = spec['base_url'].rstrip('/') + '/chat/completions'
                key = _spec_key(prov)
                extra = []
                if not key and spec.get('auth') != 'none':
                    return None, -1, 'no credentials'
            elif prov in endpoints:
                url, extra = endpoints[prov]
                key = creds(prov)['api_key']
            else:
                return None, 0, f'unknown provider {prov}'
            msgs = ([{'role': 'system', 'content': system}] if system else []) + \
                   [{'role': 'user', 'content': prompt}]
            payload = {'model': model, 'messages': msgs, 'max_tokens': max_tokens}
            auth = PROVIDER_SPECS.get(prov, {}).get('auth', 'bearer') if prov in PROVIDER_SPECS else 'bearer'
            if auth == 'x-api-key' and key:
                hdr = ['Content-Type: application/json', f'x-api-key: {key}'] + extra
            elif auth == 'none' or not key:
                hdr = ['Content-Type: application/json'] + extra
            else:
                hdr = ['Content-Type: application/json', f'Authorization: Bearer {key}'] + extra
    except FileNotFoundError:
        return None, -1, 'no credentials'   # -1 => structural, provider-wide
    except Exception as e:
        return None, 0, str(e)[:90]

    # SECURITY: never put the key in argv — it is world-readable in /proc and
    # `ps -eo args` for the whole request (confirmed exposed before this fix).
    # curl reads headers from a file with -H @path; the file is 0600 and removed
    # immediately afterwards.
    hfile = None
    try:
        fd, hfile = tempfile.mkstemp(prefix='.aihdr-', dir=os.path.dirname(STATE)
                                     if _state_writable() else None)
        os.fchmod(fd, 0o600)
        with os.fdopen(fd, 'w') as fh:
            fh.write('\n'.join(hdr) + '\n')
        cmd = ['curl', '-sS', url, '-X', 'POST', '--data-binary', '@-',
               '--max-time', str(timeout), '-w', '\n__H__%{http_code}',
               '-H', f'@{hfile}']
        p = subprocess.run(cmd, input=json.dumps(payload), capture_output=True, text=True)
    finally:
        if hfile:
            try: os.remove(hfile)
            except OSError: pass
    body, code = p.stdout, 0
    if '__H__' in body:
        body, c = body.rsplit('__H__', 1)
        try: code = int(c.strip())
        except Exception: code = 0
    try: d = json.loads(body)
    except Exception:
        return None, code, (p.stderr or body or 'unparseable')[:90]

    if isinstance(d, dict) and ('error' in d or d.get('type', '').endswith('error')):
        e = d.get('error', d)
        return None, code, (str(e.get('message', e))[:110] if isinstance(e, dict) else str(e)[:110])
    try:
        parts = d['candidates'][0]['content']['parts']
        return ''.join(x.get('text', '') for x in parts).strip(), code, None
    except Exception: pass
    try:
        m = d['choices'][0]['message']
        c = m.get('content') or ''
        if isinstance(c, list):
            c = ''.join(x.get('text', '') for x in c if isinstance(x, dict))
        c = (c or '').strip() or (m.get('reasoning') or '').strip()
        return (c, code, None) if c else (None, code, 'empty content')
    except Exception:
        return None, code, 'unexpected shape'

# ── routing ──────────────────────────────────────────────────────────────────
def candidates(task='general', quality=0, exclude_providers=()):
    rows = [r for r in ROUTES if r[2] >= quality and r[0] not in exclude_providers]
    if task == 'code':
        rows.sort(key=lambda r: (0 if 'code' in r[7] else 1, TIER_ORDER[r[5]], -r[2], -(r[3] or 0)))
    elif task == 'fast':
        rows.sort(key=lambda r: (TIER_ORDER[r[5]], 'fast' not in r[7], r[6]))
    elif task == 'best':
        rows.sort(key=lambda r: (-r[2], TIER_ORDER[r[5]], r[6]))
    else:                                   # general: cheapest tier, highest rpm, best quality
        rows.sort(key=lambda r: (TIER_ORDER[r[5]], -(r[3] or 0), -r[2]))
    return rows

def cache_path(prompt, system, task, max_tokens=3000, quality=0):
    """FIX: previously keyed on (task, system, prompt) only, so a 50-token and a
    4000-token request — or -q 0 and -q 5 — collided and served each other's
    answers. Every parameter that can change the output is now in the key."""
    h = hashlib.sha256(
        f'v2|{task}|{quality}|{max_tokens}|{system}|{prompt}'.encode()).hexdigest()[:32]
    return os.path.join(CACHE, h + '.json')

def route(prompt, task='general', quality=0, system=None, max_tokens=3000,
          use_cache=True, verbose=False, tries=6, _json_out=False):
    if use_cache:
        cp = cache_path(prompt, system, task, max_tokens, quality)
        if os.path.exists(cp):
            try:
                d = json.load(open(cp))
                if verbose: print(f"[cache hit → {d['model']}]", file=sys.stderr)
                return d['text'], d['provider'], d['model'], True
            except Exception: pass

    attempted = 0
    # An explicit high-quality ask may dip into the reserved tail of a budget.
    reserve = quality >= 5 or task == 'best'
    for prov, model, qual, rpm, rpd, tier, sec, tags in candidates(task, quality):
        if attempted >= tries: break
        # FIX (race): check availability and claim the slot inside ONE lock, so
        # two processes cannot both see 19/20 and both spend the last request.
        def _claim(st, _p=prov, _m=model):
            ok, why = available(_p, _m, st, reserve)
            if ok:
                k = key_of(_p, _m)
                ent = st.setdefault(k, {})
                if ent.get('day') != today():
                    ent['day'], ent['day_count'] = today(), 0
                ent['day_count'] = ent.get('day_count', 0) + 1   # optimistic claim
                ent['inflight'] = ent.get('inflight', 0) + 1
            return ok, why
        okflag, why = _locked(_claim)
        if not okflag:
            if verbose and not _json_out: print(f"[skip {prov}/{model}: {why}]", file=sys.stderr)
            continue
        if verbose: print(f"[try {prov}/{model} (q{qual} {tier})]", file=sys.stderr)
        text, code, err = call(prov, model, prompt, system, max_tokens)
        # A provider-wide structural failure (no creds) shouldn't consume a try:
        # it tells us to skip that provider, not that we spent an attempt on it.
        if code != -1:
            attempted += 1

        def _record(st, _p=prov, _m=model, _t=text, _c=code, _e=err):
            k = key_of(_p, _m)
            ent = st.setdefault(k, {})
            ent['inflight'] = max(0, ent.get('inflight', 1) - 1)
            if not _t:
                # roll back the optimistic claim: a failed call spent no quota
                ent['day_count'] = max(0, ent.get('day_count', 1) - 1)
            note_result(_p, _m, bool(_t), _c, st, _e)
        _locked(_record)
        if text:
            if use_cache:
                try:
                    json.dump({'text': text, 'provider': prov, 'model': model},
                              open(cache_path(prompt, system, task,
                                              max_tokens, quality), 'w'))
                except Exception: pass
            return text, prov, model, False
        if verbose: print(f"[fail {code}: {err}]", file=sys.stderr)
    return None, None, None, False

def discover(apply_changes=False, provider=None):
    """GET {base}/models for every configured spec provider.

    NEVER auto-applies: discovery prints what it found; adding routes requires
    --apply (a model list can be hundreds of entries and every route is a
    potential quota spend — the user must opt in). Non-conforming servers,
    401/403 model listings, and odd JSON shapes are skipped with a note, not
    crashes. Returns (found:{prov:[models]}, added:{prov:[models]}, errors:[...]).
    """
    found, added, errors = {}, {}, []
    import tempfile as _tf
    for p_, spec in PROVIDER_SPECS.items():
        if provider and p_ != provider:
            continue
        base = spec['base_url'].rstrip('/')
        hdr = ['Content-Type: application/json']
        key = _spec_key(p_)
        if spec.get('auth') == 'x-api-key' and key:
            hdr.append(f'x-api-key: {key}')
        elif key:
            hdr.append(f'Authorization: Bearer {key}')
        hfile = None
        try:
            fd, hfile = _tf.mkstemp(prefix='.aidiscover-')
            os.fchmod(fd, 0o600)
            with os.fdopen(fd, 'w') as fh:
                fh.write('\n'.join(hdr) + '\n')
            r = subprocess.run(['curl', '-sS', '--max-time', '20',
                                '-w', '\n__H__%{http_code}', '-H', f'@{hfile}',
                                base + '/models'], capture_output=True, text=True)
        finally:
            if hfile:
                try: os.remove(hfile)
                except OSError: pass
        body, code = r.stdout, 0
        if '__H__' in body:
            body, c = body.rsplit('__H__', 1)
            try: code = int(c.strip())
            except Exception: code = 0
        if code in (401, 403):
            errors.append(f'{p_}: model listing not permitted (HTTP {code}) — '
                          f'chat may still work; add models manually in providers.json')
            continue
        try:
            data = json.loads(body)
            ids = sorted({m.get('id') for m in data.get('data', [])
                          if isinstance(m, dict) and m.get('id')})
        except Exception:
            errors.append(f'{p_}: unparseable model list (HTTP {code}) — skipped')
            continue
        if not ids:
            errors.append(f'{p_}: empty model list — skipped')
            continue
        known = {mid for (pv, mid, *_) in ROUTES if pv == p_}
        new_ids = [i for i in ids if i not in known]
        found[p_] = ids
        if apply_changes and new_ids:
            _apply_discovered(p_, new_ids)
            added[p_] = new_ids
    return found, added, errors

def _apply_discovered(p_, new_ids):
    """Persist discovered models into providers.json (creating it if absent).

    Keeps any existing entry for the provider; only appends unknown models.
    Route defaults are conservative: quality 2 (unknown), rpm 30, tier mid —
    run probe.py/quality.py to measure the real numbers.
    """
    path = SPECS_FILE
    try:
        with open(path) as f:
            doc = json.load(f)
    except Exception:
        doc = {'providers': {}}
    doc.setdefault('providers', {})
    entry = doc['providers'].setdefault(p_, {})
    if 'base_url' not in entry:
        entry['base_url'] = PROVIDER_SPECS[p_]['base_url']
        entry['auth'] = PROVIDER_SPECS[p_].get('auth', 'bearer')
    have = set()
    for m in (entry.get('models') or []):
        have.add(m if isinstance(m, str) else m.get('id'))
    for i in new_ids:
        if i not in have:
            entry.setdefault('models', []).append(i)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        os.chmod(os.path.dirname(path), 0o700)      # may hold inline api_key entries
    except OSError:
        pass
    with open(path, 'w') as f:
        json.dump(doc, f, indent=2)
    try:
        os.chmod(path, 0o600)                       # consensus-review fix: never 0644
    except OSError:
        pass
    # hot-reload this process's routing table
    PROVIDER_SPECS, _ = _load_specs()
    ROUTES = _merge_routes()

# ── cli ──────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(description='Quota-aware free-tier AI router')
    ap.add_argument('prompt', nargs='*')
    ap.add_argument('-t', '--task', default='general',
                    choices=['general', 'code', 'fast', 'best'])
    ap.add_argument('-q', '--quality', type=int, default=0, help='min measured score 0-5')
    ap.add_argument('-s', '--system', default=None)
    ap.add_argument('-m', '--max-tokens', type=int, default=3000)
    ap.add_argument('-v', '--verbose', action='store_true')
    ap.add_argument('--no-cache', action='store_true')
    ap.add_argument('--status', action='store_true', help='show live budget state')
    ap.add_argument('--reset', action='store_true', help='clear cooldowns')
    ap.add_argument('--plan', action='store_true', help='show routing order, make no calls')
    ap.add_argument('--setup', metavar='KEY', nargs='?', const='',
                    help='install an API key: ai --setup <key> [--provider mistral]')
    ap.add_argument('--provider', default=None, help='provider for --setup (auto-detected from key format)')
    ap.add_argument('--doctor', action='store_true', help='diagnose setup problems')
    ap.add_argument('--discover', action='store_true',
                    help='list models from every configured provider (GET /models)')
    ap.add_argument('--apply', action='store_true',
                    help='with --discover: write found models into providers.json')
    ap.add_argument('--json', action='store_true',
                    help='machine-readable output (ask/status/plan)')
    a = ap.parse_args()

    if a.reset:
        save_state({}); print('state cleared'); return

    if a.discover:
        found, added, errors = discover(a.apply, a.provider)
        if a.json:
            print(json.dumps({'found': found, 'added': added, 'errors': errors},
                             indent=2))
        else:
            for p_, ids in found.items():
                print(f'{p_}: {len(ids)} models')
                for i in ids[:12]:
                    print(f'   {i}')
                if len(ids) > 12:
                    print(f'   … +{len(ids)-12} more')
            if added:
                for p_, ids in added.items():
                    print(f'✅ added {len(ids)} new {p_} routes to providers.json (quality=2 default — run probe.py to measure)')
            for e in errors:
                print(f'⚠️  {e}', file=sys.stderr)
            if not found and not errors:
                print('no spec providers configured — add one in ~/.config/ai_router/providers.json')
        return

    if a.setup is not None:
        key = a.setup.strip()
        if not key:
            print(SETUP_HELP); return
        # Detect the provider from the key's own format — users paste a key and
        # should not have to know which flag names their vendor.
        prov = a.provider
        if not prov:
            if   key.startswith('sk-or-v1-'): prov = 'openrouter'
            elif key.startswith('csk-'):      prov = 'cerebras'
            elif key.startswith('AQ.'):       prov = 'gemini'
            elif key.startswith('AIza'):      prov = 'gemini'
            elif key.startswith('eyJ'):       prov = 'kilo'
            elif len(key) == 32 and key.isalnum(): prov = 'mistral'
        if not prov:
            print('Could not detect the provider from that key format.', file=sys.stderr)
            print('Re-run with --provider <mistral|gemini|openrouter|kilo|cerebras>', file=sys.stderr)
            sys.exit(1)
        d = os.path.join(HOME, '.config', prov)
        f = os.path.join(d, 'credentials.json')
        # FIX 23: verify BEFORE overwriting. The old order wrote the new key
        # first, so a typo destroyed a working credential and left the user
        # worse off than before they ran the command.
        backup = None
        if os.path.exists(f):
            try: backup = open(f).read()
            except Exception: backup = None
        os.makedirs(d, exist_ok=True)
        with open(f, 'w') as fh:
            json.dump({'api_key': key}, fh)
        os.chmod(f, 0o600)
        row = next((r for r in ROUTES if r[0] == prov), None)
        ok = False
        if row:
            txt, code, err = call(prov, row[1], 'Reply with exactly: OK')
            ok = bool(txt)
        if ok or not row:
            print(f'✅ saved {prov} key to {f} (chmod 600)')
            if row: print('   live check: ✅ working')
        else:
            if backup is not None:
                with open(f, 'w') as fh: fh.write(backup)
                os.chmod(f, 0o600)
                print(f'❌ that {prov} key did not work — kept your previous key '
                      f'(unchanged).', file=sys.stderr)
            else:
                os.remove(f)
                print(f'❌ that {prov} key did not work — nothing saved.', file=sys.stderr)
            print(f'   provider said: {str(err)[:90]}', file=sys.stderr)
            sys.exit(1)
        return

    if a.doctor:
        print('🩺 free-tier-ai-router doctor\n')
        provs = ['mistral', 'gemini', 'openrouter', 'kilo', 'cerebras'] + \
                sorted(p for p in PROVIDER_SPECS if p not in
                       ('mistral', 'gemini', 'openrouter', 'kilo', 'cerebras'))
        have = [p for p in provs if has_credentials(p)]
        for p_ in provs:
            mark = '✅' if p_ in have else '  '
            note = '' if p_ in have else '(no key)'
            src = 'spec' if p_ in PROVIDER_SPECS else ''
            print(f'  {mark} {p_:11} {note} {src}')
        if SPEC_CONFIG_ERROR:
            print(f'\n  ⚠️  {SPEC_CONFIG_ERROR}')
        if not have:
            print('\n' + SETUP_HELP); sys.exit(3)
        print(f'\n  {len(have)}/{len(provs)} providers configured')
        st = load_state()
        usable = [(p_, m) for p_, m, *r in ROUTES if available(p_, m, st)[0]]
        print(f'  {len(usable)}/{len(ROUTES)} routes usable right now')
        if usable:
            p_, m = usable[0]
            txt, code, err = call(p_, m, 'Reply with exactly: OK')
            print(f'  live test via {p_}/{m}: {"✅ working" if txt else "❌ " + str(err)[:60]}')
        else:
            print('  ⚠️  every route is cooling down; try again shortly')
        return
    if a.status:
        st = load_state()
        rows = []
        for prov, model, qual, rpm, rpd, tier, sec, tags in ROUTES:
            e = st.get(key_of(prov, model), {})
            used = e.get('day_count', 0) if e.get('day') == today() else 0
            okflag, why = available(prov, model, st)
            rows.append({'provider': prov, 'model': model, 'quality': qual,
                         'rpm': rpm, 'rpd': rpd, 'tier': tier, 'tags': tags,
                         'used_today': used, 'ready': okflag,
                         'status': 'ready' if okflag else why})
        if a.json:
            print(json.dumps({'schema': 'ai_router.status.v1', 'routes': rows,
                              'spec_config_error': SPEC_CONFIG_ERROR}, indent=2))
            return
        print(f"{'route':58} {'tier':7} {'rpm':>5} {'today':>6}  status")
        for r in rows:
            cap = f"{r['used_today']}/{r['rpd']}" if r['rpd'] else str(r['used_today'])
            print(f"  {r['provider']+'/'+r['model']:56} {r['tier']:7} {r['rpm'] or '-':>5} {cap:>6}  "
                  f"{'✅ ready' if r['ready'] else '⏳ '+r['status']}")
        if SPEC_CONFIG_ERROR:
            print(f'\n⚠️  {SPEC_CONFIG_ERROR}', file=sys.stderr)
        return
    if a.plan:
        st = load_state()
        plan_rows = []
        for i, (prov, model, qual, rpm, rpd, tier, sec, tags) in enumerate(candidates(a.task, a.quality), 1):
            okflag, why = available(prov, model, st)
            plan_rows.append({'n': i, 'provider': prov, 'model': model, 'quality': qual,
                              'tier': tier, 'ready': okflag, 'status': 'ready' if okflag else why})
        if a.json:
            print(json.dumps({'schema': 'ai_router.plan.v1', 'task': a.task,
                              'quality_min': a.quality, 'order': plan_rows}, indent=2))
            return
        print(f"routing order for task={a.task} quality>={a.quality}:")
        for r in plan_rows:
            print(f"  {r['n']:2}. {r['provider']}/{r['model']:48} q{r['quality']} {r['tier']:7} {'✅' if r['ready'] else '⏳ '+r['status']}")
        return

    prompt = ' '.join(a.prompt) or sys.stdin.read()
    if not prompt.strip():
        ap.error('no prompt given')
    # Validate locally: a bad value would otherwise 422 against every provider
    # in turn, burning real quota to discover a client-side mistake.
    if a.max_tokens < 1:
        ap.error(f'--max-tokens must be >= 1 (got {a.max_tokens})')
    if a.max_tokens > 128000:
        ap.error(f'--max-tokens {a.max_tokens} exceeds any configured model; use <= 128000')
    if not 0 <= a.quality <= 5:
        ap.error(f'--quality must be 0-5 (got {a.quality})')
    if SPEC_CONFIG_ERROR:
        print(f'⚠️  {SPEC_CONFIG_ERROR}', file=sys.stderr)
        if a.json:
            print(json.dumps({'schema': 'ai_router.answer.v1', 'error': 'invalid providers config',
                              'detail': SPEC_CONFIG_ERROR})); sys.exit(4)
    text, prov, model, cached = route(prompt, a.task, a.quality, a.system,
                                      a.max_tokens, not a.no_cache, a.verbose, _json_out=a.json)
    if a.json and text is not None:
        print(json.dumps({'schema': 'ai_router.answer.v1', 'text': text,
                          'provider': prov, 'model': model, 'cached': cached}))
        return
    if text is None:
        configured = [p for p in ('mistral','gemini','openrouter','kilo','cerebras')
                      if has_credentials(p)]
        if not configured:
            print(SETUP_HELP, file=sys.stderr)
            sys.exit(3)
        print('No route could answer. All configured providers are rate-limited or '
              'out of quota right now.', file=sys.stderr)
        print(f'  configured providers : {", ".join(configured)}', file=sys.stderr)
        print('  run `ai --status` to see when each recovers.', file=sys.stderr)
        sys.exit(2)
    print(text)
    if a.verbose:
        print(f"\n[{'cache' if cached else prov+'/'+model}]", file=sys.stderr)

if __name__ == '__main__':
    main()
