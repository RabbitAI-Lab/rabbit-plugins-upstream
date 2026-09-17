## Description:

Forem lets agents read, create, and update Forem data through an OOMOL-connected account and the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill to have an agent inspect Forem action schemas, read Forem content, and create or update articles through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute code in the local environment.

Mitigation: Review the oo CLI installation path first, prefer a pinned, signed, or checksum-verified OOMOL installer, and run remote installer commands only when the source is trusted.

Risk: Forem write actions can change article content in the connected account.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running create or update actions.

## Reference(s):

- [ClawHub Forem skill](https://clawhub.ai/oomol/skills/oo-forem)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Forem homepage](https://www.forem.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, API Calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo connector schema checks before constructing requests and returns JSON responses from connector runs.]

## Skill Version(s):

1.0.2 (source: server release metadata, skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
