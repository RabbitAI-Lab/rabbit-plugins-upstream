## Description:

Luma provides guidance for reading Luma calendar, event, guest, and profile data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live Luma connector schemas and run read actions for calendars, events, guests, and the current user profile through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup asks users to run remote installer scripts for the oo CLI.

Mitigation: Install the CLI through a verified package where possible, or manually download and inspect a pinned installer with a published checksum or signature before running it.

Risk: The connector can read Luma calendar, event, guest, and profile data from a connected account.

Mitigation: Connect only approved accounts and scopes, and avoid exposing returned calendar, event, guest, or profile data beyond the intended task.

Risk: Tagged write or destructive actions, if present in live connector schemas, could change or remove Luma data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running any action tagged write or destructive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-luma)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Luma homepage](https://lu.ma)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell command snippets and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
