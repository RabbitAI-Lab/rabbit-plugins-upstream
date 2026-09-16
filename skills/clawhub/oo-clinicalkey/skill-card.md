## Description:

ClinicalKey helps agents operate ClinicalKey through an OOMOL-connected account for COUNTER 5.1 service status, usage reports, report listing, and member or site listing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve ClinicalKey COUNTER 5.1 data through an OOMOL-connected ClinicalKey account without handling raw credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that run downloaded scripts directly in a shell.

Mitigation: Review the oo CLI installation source before installing, and prefer an official package manager or a version-pinned installer with checksum or signature verification.

## Reference(s):

- [ClinicalKey homepage](https://www.clinicalkey.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clinicalkey)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include connector data and an execution identifier under meta.executionId.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
