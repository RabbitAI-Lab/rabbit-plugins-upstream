# Authentication and environment

Read early when starting an actual Vibbit analysis, resource query, or production task, before discovering missing credentials midway through execution. See [API client](api-client.md) for paths. Discussion, capability explanations, dry runs, and explicitly requested local-only work do not trigger setup.

## Reuse before setup

~~~bash
node "$VIBBIT_SKILL_DIR/scripts/vibbit.js" auth_status
~~~

This offline command reports availability, source, API environment, and account links without exposing the key. Precedence: `VIBBIT_API_KEY`, then `VIBBIT_OPENAPI_KEY`, then the private credential file for this package region. If configured, use `auth_status --check` once before the first operation; reuse successful authentication instead of checking every step.

If `configured=false`, immediately use the setup path below: open a supported entry, explain create/paste/verify, and preserve the original task for continuation. A missing-key notice alone is insufficient. Do not switch to local frame inspection or other tools to bypass setup. If the user explicitly declines configuration, explain the unavailable Vibbit capabilities and follow their new direction for the feasible scope.

A missing variable does not prove the user never configured it. When they confirm prior setup, check host credential injection and the actual execution environment. Bash does not automatically load Zsh configuration. Use supported inheritance from the user-identified location; never dump values, whole environments, or configuration files, and do not automatically edit shell profiles.

## Provide an actionable setup entry

Preserve the task using [account continuation](account-continuation.md). Prefer the host's native credential settings where available. Open a verified settings entry when supported; otherwise provide the actual host instructions. Do not invent a universal secret-settings button or deep link. After the user pastes once, run `auth_status --check` in the **environment actually executing the Skill**, then continue the original step.

On a local computer accessible to the user's browser:

~~~bash
node "$VIBBIT_SKILL_DIR/scripts/vibbit.js" auth_setup --open
~~~

- With `--open`, attempts to open the browser; if this fails, show the returned `setup_url`. The page links to [Vibbit API Keys](https://app.vibbit.ai/api-keys) and has a password field and Verify and save button. The user creates and pastes the key. The agent must not read the field, clipboard, or request body.
- Keep the process alive using a supported background/persistent session, normally for up to ten minutes. Success returns `configured=true, verified=true`; continue without another health check. Expiry is not success; open a fresh setup page if necessary.
- Binds only to `127.0.0.1`, with a random session URL. Verification uses this package's fixed HTTPS API without redirects. Success, cancellation, or expiry closes the entry. Do not expose it publicly or forward its port.
- Saves under `~/.vibbit/credentials/` for the current OS user, with directory mode 0700 and file mode 0600. This is an **unencrypted private file**, not an OS keychain. The helper supports local macOS/Linux environments with these permissions. Use native host credential settings on shared devices, Windows, or environments without private-file enforcement. `VIBBIT_CONFIG_DIR` may specify another absolute private directory outside projects, Skills, synced folders, and release packages.
- If an environment key already exists, the helper refuses to save a key that would be overridden. Update the original host setting instead. Existing files are replaced only after successful verification and saving; cancellation or verification failure preserves them.

For cloud agents, containers, or remote servers, their loopback address generally does not refer to the user's computer. Use the host's Secret/environment settings in that execution environment; local terminal configuration does not configure a cloud process. If no user-accessible credential entry exists, explain that specific limitation and continue independent planning. Do not claim an inaccessible page was opened or authentication succeeded.

Never put keys in chat, command arguments, request files, or task journals. Do not search chat history or read the clipboard for keys, or create a key on the user's behalf through browser automation.

## Region, verification, and replacement

Default API: `https://openapi.vibbit.ai/openapi/v1`. `VIBBIT_BASE_URL` accepts an origin or full API base; change it only for the user's selected environment. Stored keys bind to this package's exact API base and never follow a custom domain or another region. For a custom environment, use its matching host credential. Get website links from `account_links`; never guess domains for unknown environments.

`auth_status --check` / `health` proves authentication and reachability only, not every model, permission, or sufficient credits. A 401 requires credential attention; a 403 may involve IP allowlists, permissions, or task ownership. Network errors preserve configuration. After an account or region change, refresh private avatars and voices rather than reusing old mappings.

Only on the user's explicit request, `auth_clear` removes this regional private file. It neither edits environment variables nor revokes the server key; revocation happens on the API Keys page.

[Authentication reference](https://vibbit.apifox.cn/514565013e0) · [Troubleshooting](troubleshooting.md)
