## Description:

DialMyCalls helps agents inspect account details and manage DialMyCalls contacts and contact groups through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with connected DialMyCalls accounts use this skill to read account, contact, and group data and to create, update, or delete DialMyCalls contacts and groups with user confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute arbitrary code if followed.

Mitigation: Review the installer path before installing and prefer a verified, versioned oo CLI source with checksum or signature validation.

Risk: Write and destructive DialMyCalls actions can create, update, or delete contacts and groups.

Mitigation: Approve these actions only after checking the exact target, payload, and expected effect with the user.

## Reference(s):

- [DialMyCalls homepage](https://www.dialmycalls.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [DialMyCalls ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dialmycalls)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI DialMyCalls connector and may return JSON data from DialMyCalls actions.]

## Skill Version(s):

1.0.2 (source: server evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
