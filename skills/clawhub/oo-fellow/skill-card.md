## Description:

Fellow (fellow.app). Use this skill for Fellow requests that read, create, update, or delete data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Fellow through the oo CLI, including reading meeting notes and action items and updating or archiving action items when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes an unverified remote installer command for the oo CLI.

Mitigation: Install only after independently verifying the official oo CLI installation path, and avoid running pipe-to-shell installers without that verification.

Risk: The skill can complete, archive, or otherwise change Fellow data.

Mitigation: Confirm the exact target, payload, and intended effect before running write or destructive actions.

Risk: The skill depends on OOMOL account connection and server-side credential handling.

Mitigation: Use it only when the user trusts the OOMOL oo CLI and the connected Fellow/OOMOL account relationship.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-fellow)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Fellow Homepage](https://fellow.app)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include Fellow data and execution metadata when actions run.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
