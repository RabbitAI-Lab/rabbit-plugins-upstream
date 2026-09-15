## Description:

This skill helps an agent operate AbuseIPDB through an OOMOL-connected account using the oo CLI for blacklist lookup, IP reputation checks, CIDR block inspection, and report retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security analysts, and external agents use this skill to query AbuseIPDB reputation data through an authenticated OOMOL connector without directly handling raw AbuseIPDB API tokens. It supports blacklist retrieval, single-IP checks, CIDR block inspection, and report listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes mutable remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Use a signed or package-manager installation path when available, or download and verify the installer before execution.

Risk: Write-tagged connector actions can affect AbuseIPDB state or account-side behavior if run with an incorrect payload.

Mitigation: Inspect the live connector schema before building payloads and confirm the exact action, payload, and expected effect before running write-tagged actions.

## Reference(s):

- [ClawHub AbuseIPDB skill page](https://clawhub.ai/oomol/skills/oo-abuseipdb)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [AbuseIPDB homepage](https://www.abuseipdb.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
