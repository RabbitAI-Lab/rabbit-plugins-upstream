## Description:

Pinpoint (pinpointhq.com). Use this skill for ANY Pinpoint request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to read Pinpoint recruiting data through an OOMOL-connected account, including applications, candidates, and jobs by ID or list queries with supported filters and pagination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a correctly installed and authenticated OOMOL oo CLI connection before Pinpoint data can be read.

Mitigation: Review setup and connection status first, and use the documented recovery steps only after an auth, connection, or billing failure occurs.

Risk: Future Pinpoint connector actions could introduce write or destructive behavior even though the current listed actions are reads.

Mitigation: Require explicit user confirmation for any write or destructive action, including the exact target, payload, and expected effect.

Risk: Stale assumptions about connector payloads could lead to failed or incorrect requests.

Mitigation: Inspect the live action schema with `oo connector schema` before constructing each action payload.

## Reference(s):

- [ClawHub Pinpoint skill](https://clawhub.ai/oomol/skills/oo-pinpoint)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Pinpoint homepage](https://www.pinpointhq.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
