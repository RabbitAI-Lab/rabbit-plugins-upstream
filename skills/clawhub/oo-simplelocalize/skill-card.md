## Description:

SimpleLocalize (simplelocalize.io). Use this skill for ANY SimpleLocalize request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and localization teams use this skill to inspect and manage a connected SimpleLocalize project through OOMOL, including project details, languages, translation keys, and translations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write and delete actions against the user's connected SimpleLocalize project.

Mitigation: Review and explicitly confirm payloads before approving write or destructive actions, especially language deletion and translation updates.

Risk: The skill acts through an OOMOL-connected account and can affect data available to that account.

Mitigation: Install it only when SimpleLocalize project management through OOMOL is intended, and keep connection scope and credential status current.

## Reference(s):

- [SimpleLocalize homepage](https://simplelocalize.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-simplelocalize)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
