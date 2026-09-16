## Description:

EmailListVerify helps agents operate EmailListVerify through an OOMOL-connected account for email verification, disposable-domain checks, credit lookup, and batch email-list workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to verify individual email addresses, inspect disposable domains, manage EmailListVerify batch list jobs, and check account credits through the oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include internet installer scripts that could execute unverified code.

Mitigation: Prefer official installation documentation, inspect downloaded scripts, verify publisher or checksum information where available, and avoid elevated privileges unless required.

Risk: Write and destructive EmailListVerify actions can modify or delete account data.

Mitigation: Fetch the live action schema before building payloads and obtain explicit user confirmation for write or destructive actions.

## Reference(s):

- [EmailListVerify homepage](https://emaillistverify.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-emaillistverify)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
