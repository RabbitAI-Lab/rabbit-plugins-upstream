## Description:

PostGrid Verify (postgrid.com) helps agents search, parse, verify, standardize, and read US and Canadian address data through an OOMOL-connected PostGrid Verify account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate PostGrid Verify through OOMOL for address autocomplete, city or province lookup from postal codes, freeform address parsing, and US or Canadian address verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup and command guidance can create local execution risk if users install or run the oo CLI from an untrusted path.

Mitigation: Install only through trusted, version-pinned OOMOL instructions and prefer signature or checksum verification when available.

Risk: Interpolating address data directly into shell strings can create command construction risk.

Mitigation: Use a JSON file or a safe process-argument API for connector payloads instead of manually interpolating address data into shell commands.

Risk: The security verdict is suspicious and indicates setup commands should be reviewed before installation.

Mitigation: Review the skill setup steps and generated commands before deployment, and limit execution to the documented `oo` connector commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-postgrid-verify)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [PostGrid Verify homepage](https://www.postgrid.com/address-verification/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include PostGrid Verify connector data and execution metadata returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
