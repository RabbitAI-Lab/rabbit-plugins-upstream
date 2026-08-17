## Description:

Tianyancha (tianyancha.com). Use this skill for ANY Tianyancha request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent search Tianyancha and retrieve company intelligence through an OOMOL-connected account. It supports company records, relationships, risks, judicial information, intellectual property, tenders, and identity verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can query Tianyancha through the user's OOMOL account and may expose account usage, billing, or connected-service access to agent-initiated requests.

Mitigation: Install only when Tianyancha access through OOMOL is intended, and review the OOMOL CLI and connection setup before using fallback install or login steps.

Risk: Future connector actions marked write or destructive could change or remove data if run without user confirmation.

Mitigation: Require explicit confirmation of the exact payload and effect before running any connector action marked write or destructive.

## Reference(s):

- [Tianyancha homepage](https://www.tianyancha.com/data)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Skill release page](https://clawhub.ai/oomol/skills/oo-tianyancha)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live connector schema inspection steps and JSON action payloads.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
