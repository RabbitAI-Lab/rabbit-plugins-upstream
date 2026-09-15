## Description:

Logo.dev lets agents search brand records, fetch structured brand metadata, and build logo image URLs through the OOMOL Logo.dev connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs to query Logo.dev brand data or generate logo image URLs by domain, name, ticker, ISIN, or crypto symbol.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute unreviewed code.

Mitigation: Prefer an official versioned installer or package-manager path with checksum or signature verification, and review the installer source and trust path before running it.

Risk: The workflow depends on the OOMOL oo CLI and an OOMOL-connected Logo.dev account.

Mitigation: Install only if the oo CLI dependency and credential delegation model are acceptable for the deployment environment.

## Reference(s):

- [Logo.dev homepage](https://logo.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-logo-dev)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with bash command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns Logo.dev action results through oo CLI JSON output.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
