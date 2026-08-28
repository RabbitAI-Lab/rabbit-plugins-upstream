## Description:

Prompt injection detection and security scanning for OpenClaw agents. Installs the ai-sentinel plugin via OpenClaw CLI, configures plugin settings, and offers local (Community) or remote (Pro) classification with dashboard reporting. All configuration changes require explicit user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[amandiwakar](https://clawhub.ai/user/amandiwakar)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install and configure the AI Sentinel OpenClaw plugin for prompt-injection scanning. The setup flow supports local Community scanning and consent-gated Pro reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pro mode can send telemetry or raw cloud-scan content to an external service.

Mitigation: Use Community mode for local-only scanning, or explicitly review and consent to Pro telemetry, cloud-scan, and raw input settings before enabling them.

Risk: The Pro API key may be exposed if environment files are mishandled.

Mitigation: Store `AI_SENTINEL_API_KEY` in `.env`, keep `.env` out of version control, and restrict access to workspaces that use Pro mode.

Risk: Configuration changes can alter OpenClaw gateway behavior.

Mitigation: Review the generated plugin configuration before applying it and require explicit confirmation before updating `.env`, `.gitignore`, or `~/.openclaw/openclaw.json`.

## Reference(s):

- [AI Sentinel ClawHub Page](https://clawhub.ai/amandiwakar/skills/ai-sentinel)
- [Zetro](https://zetro.ai)
- [AI Sentinel npm Package](https://www.npmjs.com/package/ai-sentinel)
- [AI Sentinel Dashboard](https://app.zetro.ai)
- [AI Sentinel Pro API](https://api.zetro.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Interactive setup choices determine Community or Pro configuration; file changes require explicit user confirmation.]

## Skill Version(s):

0.2.2 (source: server release evidence and changelog, released 2026-08-28)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
