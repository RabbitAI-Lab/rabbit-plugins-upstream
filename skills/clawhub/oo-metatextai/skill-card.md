## Description:

MetatextAI (metatext.ai). Use this skill for ANY MetatextAI request - reading, creating, and updating data. Whenever a task involves MetatextAI, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect MetatextAI action schemas, evaluate chat transcripts against configured guardrails, manage guardrail policies, and run red-team test scans through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Use a verified package or pinned oo CLI release where possible, and review installer commands before execution.

Risk: The skill can create MetatextAI guardrail policies and perform other state-changing actions.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub MetatextAI Skill](https://clawhub.ai/oomol/skills/oo-metatextai)
- [MetatextAI Homepage](https://metatext.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
