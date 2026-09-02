## Description:

Zylvie (zylvie.com) connector for reading, creating, updating, and deleting Zylvie data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Zylvie through the OOMOL oo CLI, including user lookup, coupon and product management, license key workflows, and subscription verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and destructive actions can change, delete, archive, redeem, or refund Zylvie business data.

Mitigation: Require explicit user approval of the target, payload, and expected effect before running any write or destructive action.

Risk: A payload built from stale assumptions can send incorrect fields to the connector.

Mitigation: Inspect the live action schema with the oo CLI before constructing payloads.

Risk: Missing or expired OOMOL/Zylvie connection state can interrupt execution.

Mitigation: Run first-time setup or reconnection steps only after an action fails with the matching authentication, connection, scope, or billing error.

## Reference(s):

- [ClawHub Zylvie Skill](https://clawhub.ai/oomol/skills/oo-zylvie)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Zylvie Homepage](https://zylvie.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions can be run directly; write and destructive actions require user confirmation of the exact payload and effect.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
