## Description:

Reverse Contact (reversecontact.com). Use this skill for ANY Reverse Contact request - searching and reading data. Whenever a task involves Reverse Contact, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query Reverse Contact through an OOMOL-connected account, inspect live connector schemas, and run company or person enrichment actions with JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the OOMOL connector path for Reverse Contact and may require CLI installation, account connection, or billing readiness before use.

Mitigation: Install only when intending to use OOMOL for Reverse Contact, review account connection and billing status before retrying failed actions, and avoid repeating first-time setup steps unless an error indicates they are needed.

Risk: Future connector actions could change state or remove data if write or destructive actions are added later.

Mitigation: Confirm exact payloads and expected effects with the user before running any action tagged write or destructive.

## Reference(s):

- [Reverse Contact homepage](https://www.reversecontact.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-reversecontact)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields when actions run successfully.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
