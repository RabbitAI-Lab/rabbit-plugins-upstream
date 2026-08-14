# Setup — install, auth, and OpenClaw wiring

One-time. Read this when `ticktick auth status` fails.

## Install the CLI

Requires Node.js (current LTS) on the server.

```bash
node --version
npm install -g @ticktick/ticktick-cli
ticktick --version
```

If the global install fails with `EACCES`, the npm global prefix isn't writable by this user. Don't reach for `sudo npm -g` — it creates root-owned files under a systemd *user* service and breaks later upgrades. Use a user-owned prefix:

```bash
mkdir -p ~/.npm-global
npm config set prefix ~/.npm-global
export PATH="$HOME/.npm-global/bin:$PATH"   # add to ~/.zshrc
```

This skill declares `requires.bins: ["ticktick"]`, so OpenClaw only loads it when `ticktick` is on the gateway's `PATH`. If the skill doesn't appear in `openclaw skills list`, a missing or non-PATH binary is the first thing to check — not a problem with the skill file.

## Authenticate — token only

The server is headless. `ticktick auth login` launches an OAuth PKCE browser flow, and there is no browser, so it hangs. Use the token path.

The token must be created by hand in a browser — on a laptop or phone, not the server:

1. Open the TickTick web app and log in.
2. Click the avatar, top-left.
3. **Settings → Account → API Token**.
4. Create a token and copy it.

Then on the server:

```bash
ticktick auth token <token>
ticktick auth status
```

The token is a full-access credential for the user's task data. Don't echo it back in chat, don't write it into logs, notes, or workspace files, and don't include it in a summary. If it arrives in a Telegram message, use it and move on without repeating it — that chat history is stored.

## Auth subcommands

```bash
ticktick auth status      # check login state
ticktick auth token <t>   # set token — the one to use here
ticktick auth login       # OAuth browser flow — NOT usable on this server
ticktick auth logout      # clears the token; only on explicit request
```

## If auth breaks later

Tokens expire; the symptom is a 401 on any command. Recovery is the same manual browser flow above — there is no refresh command. Say plainly that the token needs regenerating from the web app; nothing can be done server-side.

## Exec approvals

Every command here runs through the `exec` tool. Depending on the configured permission mode, the gateway may prompt for approval on each call, which is tedious over Telegram. If that happens, add `ticktick` to the exec allowlist rather than loosening the mode globally — see https://docs.openclaw.ai/tools/exec-approvals.
