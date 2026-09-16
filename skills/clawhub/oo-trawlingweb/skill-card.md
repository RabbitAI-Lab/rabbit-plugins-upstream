## Description:

TrawlingWeb helps agents search indexed news and blog publications through the TrawlingWeb News API using the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query TrawlingWeb for indexed news and blog results through an OOMOL-connected account. It guides schema inspection, connector execution, and recovery from setup, authentication, connection, scope, credit, or credential issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance can lead agents to run unverified remote installer scripts without version pinning or checksum checks.

Mitigation: Review the installer source first, prefer a verified and versioned OOMOL installation method, and avoid piping downloaded scripts directly into a shell unless the source is independently trusted.

## Reference(s):

- [TrawlingWeb homepage](https://trawlingweb.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trawlingweb)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
