## Description:

Stream Estate (stream.estate) helps agents search, list, and retrieve Stream Estate property and location data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Stream Estate property inventory, retrieve property records by UUID, list cities, search locations, and find similar listings through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes an unverified internet installer that can run code on the user's machine.

Mitigation: Review the setup path before installing; prefer a trusted package manager or download-and-verify process, and do not let an agent automatically run the remote installer unless the user accepts the local code-execution risk.

Risk: Authentication, connection, or billing setup may be required before Stream Estate connector actions can run.

Mitigation: Run setup steps only after a matching command failure and avoid proactively launching login or connection flows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-stream-estate)
- [Stream Estate Homepage](https://stream.estate)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; listed Stream Estate actions are read-only in the artifact.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
