## Description:

Zipcodebase helps agents search postal-code data, list city and state postal codes, calculate distances, match postal-code pairs, and check account status through an OOMOL-connected Zipcodebase account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Zipcodebase postal-code data through their connected OOMOL account for lookups, city and state postal-code lists, radius searches, distance calculations, account status, and credit checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Install the oo CLI only through verified official release steps, verify checksums or signatures where available, and do not let an agent run the installer automatically.

## Reference(s):

- [Zipcodebase homepage](https://zipcodebase.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Zipcodebase skill page](https://clawhub.ai/oomol/skills/oo-zipcodebase)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI and an authenticated OOMOL-connected Zipcodebase account.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
