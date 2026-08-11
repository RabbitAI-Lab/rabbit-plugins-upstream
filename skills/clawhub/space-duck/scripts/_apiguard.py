#!/usr/bin/env python3
"""Space Duck — api_base guard (0.7.1, marker [HARDEN-071]).

Every script in this skill sends the Beak Key to the host in
cfg['api_base']. A tampered config could therefore redirect the key to an
attacker-controlled endpoint. This guard pins api_base to the official
Space Duck domain unless the operator explicitly opts out.

Opt-out (for self-hosted/staging backends, both required to be silent):
  config.json:  "allow_custom_api": true
Or env var:     SPACEDUCK_ALLOW_CUSTOM_API=1
With opt-out set, a custom host still prints a one-line warning to stderr
so the redirect is never invisible.
"""
import os
import sys
from urllib.parse import urlparse

OFFICIAL_SUFFIX = 'spaceduckling.com'


def check_api_base(cfg):
    """Validate cfg['api_base']. Exits(3) on an unauthorized custom host.
    Returns the effective api_base string for convenience."""
    api = (cfg or {}).get('api_base') or 'https://beak.spaceduckling.com'
    try:
        host = (urlparse(api).hostname or '').lower()
    except Exception:
        host = ''
    official = host == OFFICIAL_SUFFIX or host.endswith('.' + OFFICIAL_SUFFIX)
    if official:
        return api
    allowed = bool((cfg or {}).get('allow_custom_api')) or \
        os.environ.get('SPACEDUCK_ALLOW_CUSTOM_API') == '1'
    if allowed:
        print(f'⚠️  SPACE DUCK: api_base is a CUSTOM host ({host or api!r}) — '
              'your Beak Key will be sent there (allow_custom_api is set).',
              file=sys.stderr)
        return api
    print('✗ SPACE DUCK SAFETY STOP: config api_base points to '
          f'{host or api!r}, not {OFFICIAL_SUFFIX}.\n'
          '  Your Beak Key would be sent to that host. If this is intentional '
          '(self-hosted backend), set "allow_custom_api": true in '
          '~/.space-duck/config.json or export SPACEDUCK_ALLOW_CUSTOM_API=1.\n'
          '  If you did NOT change api_base, your config may have been '
          'tampered with — inspect ~/.space-duck/config.json before retrying.',
          file=sys.stderr)
    sys.exit(3)
