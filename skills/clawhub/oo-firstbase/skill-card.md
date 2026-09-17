## Description:

Firstbase connector helper for searching and reading Firstbase data through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with an OOMOL-connected Firstbase account use this skill to inspect live Firstbase action schemas and retrieve catalog SKUs, inventory items, brands, and categories through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include curl-to-bash and PowerShell installer commands for the oo CLI.

Mitigation: Verify the oo CLI installer through a trusted, documented channel and avoid running installer commands from an elevated shell unless the source has been reviewed and trusted.

Risk: The skill depends on an authenticated OOMOL-connected Firstbase account and live connector schemas.

Mitigation: Run schema inspection before building payloads and use setup or reconnection steps only after an auth, connection, scope, or billing error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-firstbase)
- [Firstbase homepage](https://www.firstbase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns oo CLI JSON responses when actions are run.]

## Skill Version(s):

1.0.3 (source: evidence release.version and artifact metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
