## Description:

xAI (x.ai). Use this skill for ANY xAI request -- reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate xAI through an OOMOL-connected account, including chat completion creation and model metadata lookup. It guides the agent to inspect live connector schemas before sending action payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct execution of remote installer scripts without verification.

Mitigation: Prefer an official package manager or release artifact, verify checksums or signatures when available, inspect installer scripts before execution, and avoid administrator or root shells unless clearly required.

Risk: xAI prompts and payloads are routed through OOMOL-connected infrastructure.

Mitigation: Do not submit sensitive content unless that data flow is acceptable for the user and organization.

Risk: The chat completion action is marked as a write action and can send user-provided payloads to xAI.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and inspect the live connector schema before constructing requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-x-ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [xAI homepage](https://x.ai)
- [OOMOL xAI connection page](https://console.oomol.com/app-connections?provider=x_ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
