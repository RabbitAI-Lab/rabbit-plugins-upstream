---
name: clawtopics-link
description: Install, enroll, verify, diagnose, or remove the official ClawTopics Embedded Link Plugin for an OpenClaw Gateway. Use when an owner asks to connect OpenClaw to ClawTopics Web or Mobile without exposing a public port, VPN, remote shell, Go connector, Redis, or Sidecar.
---

# ClawTopics Embedded Link

Use only the signed OpenClaw background-service Plugin
`@clawtopics/openclaw-link@1.0.0`. Docker, Linux, Windows and macOS follow the
same Plugin workflow.

## Security boundary

- Never install or start a Go binary, Python connector daemon, Docker Sidecar,
  SOCKS proxy, remote shell, arbitrary downloader or arbitrary cloud command.
- Never place an Enrollment Code, Gateway token/password, device token, ticket,
  private key or setup code in argv, an environment variable, a URL, a log or a
  response summary.
- Run OpenClaw commands as the OS user that owns the Gateway state directory.
  Do not use root merely for convenience.
- Do not auto-approve an OpenClaw device request. Show only its safe request ID
  and require the owner to approve it.
- Never upload or persist the limited OpenClaw Setup Code. The browser parses it
  locally and ignores its embedded LAN endpoint.

## Install and enroll

1. Verify `openclaw --version` is `>=2026.7.1 <2026.8.0`.
2. Install the fixed pinned Plugin:

   ```bash
   openclaw plugins install npm:@clawtopics/openclaw-link@1.0.0 --pin
   ```

3. Configure and enable it:

   ```bash
   openclaw config set plugins.entries.clawtopics-link.config.controlApiBaseUrl https://openclaw.tekoai.com/api
   openclaw plugins enable clawtopics-link
   openclaw gateway restart
   ```

4. Start enrollment in an interactive no-echo PTY. Do not include the code in
   the command:

   ```bash
   openclaw clawtopics-link enroll --interactive --json
   ```

5. When the prompt is waiting, paste exactly the single-use Enrollment Code and
   a newline through the execution tool's protected input action. Do not echo,
   repeat or summarize it.
6. Verify canonical runtime state:

   ```bash
   openclaw clawtopics-link doctor --json
   openclaw clawtopics-link status --json
   openclaw plugins inspect clawtopics-link --runtime --json
   ```

Success requires `enrolled=true`, runtime state `online`, and
`controlConnected=true`. Do not infer success from installer prose.

## Authorize a browser or mobile client

Generate the Setup Code locally:

```bash
openclaw qr --setup-code-only
```

The owner enters it only in ClawTopics Web or Mobile. If OpenClaw returns a
pairing request:

```bash
openclaw devices list
openclaw devices approve <requestId>
```

After approval, retry with the same pending client identity. Do not generate a
new client key for every approval check.

## Diagnostics and removal

Use only:

```bash
openclaw clawtopics-link doctor --json
openclaw clawtopics-link status --json
```

Report safe identifiers, versions, OS/architecture, Relay node and online
state. Redact credentials, codes, keys, tickets, route keys and message data.
`SIDECAR_REQUIRED` is an obsolete error and must not be returned.

For removal, require explicit owner approval, then run:

```bash
openclaw clawtopics-link unenroll --interactive
openclaw plugins disable clawtopics-link
```

Do not manually delete the OpenClaw state directory.
