## Description:

Use this skill to evaluate text or structured JSON with TypeSafe AI and list available TypeSafe AI models through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run TypeSafe AI evaluations and discover available models from an OOMOL-connected account without handling raw TypeSafe AI credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute changing network code without integrity checks.

Mitigation: Review the oo CLI installation path first, prefer official documentation or a verified package-manager installation, and do not allow an agent to run curl-to-bash or irm-to-iex setup automatically.

Risk: Evaluation requests send user-provided content to TypeSafe AI through OOMOL and may use the connected OOMOL account.

Mitigation: Confirm the account, connection, and data sensitivity before running evaluations, especially when prompts or structured JSON contain private or regulated information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-typesafe-ai)
- [TypeSafe AI homepage](https://typesafe.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schema inspection before action execution; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
