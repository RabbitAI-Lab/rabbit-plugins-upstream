## Description:

ClassMarker helps agents search and read ClassMarker groups, links, tests, and recent results through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents with an OOMOL-connected ClassMarker account use this skill to inspect live action schemas and retrieve accessible groups, links, tests, and recent result data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests remote installer scripts that may execute unreviewed code.

Mitigation: Review OOMOL's installation path, prefer a pinned or verifiable package, and avoid elevated shells unless that risk is intentionally accepted.

Risk: The skill retrieves live ClassMarker account data through an OOMOL-connected credential.

Mitigation: Use the documented read-only actions for scoped requests and inspect the live action schema before constructing payloads.

## Reference(s):

- [ClassMarker homepage](https://www.classmarker.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub ClassMarker skill page](https://clawhub.ai/oomol/skills/oo-classmarker)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only ClassMarker actions; requires oo CLI authentication and an OOMOL-connected ClassMarker account.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
