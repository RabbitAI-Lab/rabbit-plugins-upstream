## Description:

AI Guardian helps agents observe and govern local LLM endpoints by inventorying installed and running models, applying model policy, scanning prompts for sensitive content or jailbreak patterns, and auditing route-through usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and administrators use this skill to inspect and govern single-endpoint local LLM runtimes, identify unsanctioned or drifted models, scan prompts before model calls, and review observed local-LLM usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can delete local models and change model allow/deny policies without its own read-only or approval gate.

Mitigation: For observe-only use, expose only scan and read tools or run the skill against an account or runtime that cannot pull, delete, or modify models; require human review before write operations.

Risk: The local ~/.ai-guardian directory can hold audit metadata, usage records, undo data, configuration, and optional encrypted credentials.

Mitigation: Protect the directory and any master password with host-level access controls, and avoid exposing the state directory to untrusted users or processes.

Risk: Installing an unexpected package could give the agent different local administration behavior than intended.

Mitigation: Verify the uv package name and publisher before installation, then confirm the installed CLI matches the expected ai-guardian release.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/ai-guardian)
- [Project Homepage](https://github.com/AIops-tools/AI-Guardian)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local model inventory, policy verdicts, prompt risk bands, audit summaries, and remediation guidance.]

## Skill Version(s):

0.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
