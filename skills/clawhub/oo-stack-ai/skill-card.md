## Description:

Operates StackAI through an OOMOL-connected account using the StackAI connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect StackAI action schemas, run deployed StackAI flows with JSON variables, and fetch metadata for prior StackAI runs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run StackAI flows through broad oo CLI authority.

Mitigation: Confirm the target flow, payload, and expected side effects before executing a flow.

Risk: The first-time setup guidance includes remote installer commands.

Mitigation: Prefer a verifiable package or reviewed installer for the oo CLI before installation.

Risk: Connector permissions may be broader than the immediate StackAI task requires.

Mitigation: Review requested oo CLI scopes and keep connector permissions limited to the intended workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-stack-ai)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [StackAI Homepage](https://www.stack-ai.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
