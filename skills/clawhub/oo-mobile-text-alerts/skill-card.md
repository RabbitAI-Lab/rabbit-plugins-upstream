## Description:

Operates Mobile Text Alerts through an OOMOL-connected account for reading, creating, updating, and deleting subscriber data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Mobile Text Alerts subscribers through an OOMOL-connected account. It supports subscriber lookup, listing, creation, updates, and deletion while using live connector schemas before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change subscriber records.

Mitigation: Confirm the exact payload and expected effect with the user before running create or update actions.

Risk: Delete actions can remove subscriber records.

Mitigation: Confirm the target identifier and get explicit approval before running delete actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mobile-text-alerts)
- [Mobile Text Alerts Homepage](https://mobile-text-alerts.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions are run with --json.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
