## Description:

Shippo (goshippo.com). Use this skill for Shippo requests involving reading, creating, and updating account data through an OOMOL-connected Shippo account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Shippo via the OOMOL `oo` CLI, including inspecting action schemas, creating and retrieving address or parcel objects, listing account objects, validating addresses, and checking tracking status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructs users or agents to run remote installer scripts directly from OOMOL URLs.

Mitigation: Review OOMOL's official CLI installation path before installation and prefer a pinned or verifiable installer where possible.

Risk: Write actions can create Shippo address and parcel objects in the connected account.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub Shippo skill page](https://clawhub.ai/oomol/skills/oo-shippo)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Shippo homepage](https://goshippo.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when commands are run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
