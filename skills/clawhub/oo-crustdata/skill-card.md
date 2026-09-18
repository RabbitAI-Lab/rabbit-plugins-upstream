## Description:

Crustdata (crustdata.com). Use this skill for Crustdata company search and read workflows through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Crustdata through an OOMOL-connected account for company autocomplete, identification, enrichment, and filtered search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code without verification.

Mitigation: Prefer manually reviewed, version-pinned, checksum-verified OOMOL CLI installation instructions and avoid elevated privileges during installation.

Risk: Crustdata actions use connected account credentials, so incorrect payloads could query unintended company data.

Mitigation: Inspect the live action schema before building payloads and confirm any action marked write or destructive before execution.

## Reference(s):

- [Crustdata homepage](https://crustdata.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-crustdata)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Crustdata action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
