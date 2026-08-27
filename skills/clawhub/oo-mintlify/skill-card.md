## Description:

Mintlify helps agents read deployment status and trigger production or preview deployments for Mintlify documentation projects through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to check Mintlify deployment status and queue production or branch preview deployments after reviewing the live action schema and payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production and preview deployment actions can change Mintlify deployment state.

Mitigation: Review the live action schema and confirm the exact payload and effect with the user before executing write actions.

Risk: The skill depends on an OOMOL-connected Mintlify account and an authenticated oo CLI session.

Mitigation: Use first-time setup only after auth or connection failures, and avoid handling raw tokens directly.

## Reference(s):

- [Mintlify homepage](https://www.mintlify.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
