# Agentar CLI Quick Reference

This reference mirrors the public production Agentar CLI install and smoke-test workflow. Do not invent versions, download URLs, or install paths; use the URLs and paths below unless the caller explicitly provides a newer artifact.

## Install

Check the local runtime first:

```bash
node -v
npm -v
```

Agentar CLI installation uses npm internally. If npm is unavailable, fix npm rather than switching to pnpm or yarn.

Public production install script URL:

```text
https://dtaiagtavtr.antdigital.com/agentar-cli/install.sh
```

Confirm the installer is reachable:

```bash
curl -I 'https://dtaiagtavtr.antdigital.com/agentar-cli/install.sh'
```

Install from the public production script:

```bash
curl -fsSL 'https://dtaiagtavtr.antdigital.com/agentar-cli/install.sh' | bash
```

Verify the default binary path:

```bash
/tmp/agentar-cli/bin/agentar --version
/tmp/agentar-cli/bin/agentar --help
```

Use `agentar` directly in the current shell:

```bash
export PATH="/tmp/agentar-cli/bin:$PATH"
agentar --version
```

Public production Skill zip URL:

```text
https://dtaiagtavtr.antdigital.com/agentar-cli/skill.zip
```

Install the Agentar Skill with the official Skills command:

```bash
npx skills add OpenAgentar/agentar-skills
```

For validation or CI-style checks, keep credential state isolated:

```bash
mkdir -p "$PWD/.tmp"
AGENTAR_TOKEN_FILE=$PWD/.tmp/tokens.json agentar auth login --api-key <YOUR_API_KEY>
AGENTAR_PLAYGROUND_STATE_FILE=$PWD/.tmp/state.json agentar "hello"
```

Override package URLs only when testing an explicitly supplied newer artifact:

```bash
curl -fsSL 'https://dtaiagtavtr.antdigital.com/agentar-cli/install.sh' -o install-agentar-cli.sh
chmod +x install-agentar-cli.sh
./install-agentar-cli.sh --package-url 'https://example.com/agentar-cli.tgz'
```

## Basic Commands

```bash
agentar --version
agentar --help
agentar auth login --api-key <YOUR_API_KEY>
agentar auth status
agentar "hello"
agentar chat "hello"
agentar agents
agentar session list
```

## Environment Variables

```bash
AGENTAR_API_KEY=<YOUR_API_KEY> agentar "hello"
AGENTAR_TOKEN_FILE=$PWD/.tmp/tokens.json agentar auth login --api-key <YOUR_API_KEY>
AGENTAR_PLAYGROUND_STATE_FILE=$PWD/.tmp/state.json agentar "hello"
```

## Output Modes

```bash
agentar "hello" --output text
agentar "hello" --output json
agentar "hello" --output jsonl
agentar "hello" --output sse
agentar "hello" --output debug
```

## Attachments

```bash
agentar "summarize this file" --attach ./example.pdf
```

## Scenario Agents

```bash
agentar -a office-agent "draft an office document outline"
agentar -a image-agent "generate an image"
agentar -a video-agent "generate a 5 second video of an orange cat resting by a sunny window" --duration 5
```

`agentar agents` lists local presets only: `office-agent`, `image-agent`, and `video-agent`. Prefer these presets for supported scenes. Use `--agent <backendAgentId>` only when the task or platform supplies an explicit backend Agent ID; unknown `--agent` values are passed through as `agentId`.

## Host CLI Skill Smoke Test

After installing the Skill, restart the host CLI if needed, then run a Skill-triggering request:

```bash
claude "使用 agentar skill，帮我生成一段 5 秒短视频：一只橘猫趴在窗边晒太阳，画面温暖自然。"
```

## Troubleshooting

| Symptom | Likely Cause | Action |
| --- | --- | --- |
| `agentar: command not found` | `/tmp/agentar-cli/bin` is not on `PATH` | Run `export PATH="/tmp/agentar-cli/bin:$PATH"` and retry |
| Install script download fails | Network cannot reach the download domain | Check network, proxy, or install script reachability |
| Auth fails or returns 401 | API key is missing or invalid | Run `agentar auth login --api-key <YOUR_API_KEY>` again |
| Skill does not trigger | Skill is not installed or the host CLI has not restarted | Run `npx skills add OpenAgentar/agentar-skills`, then restart the host CLI |
