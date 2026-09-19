## Description:

currencyapi (currencyapi.com). Use this skill for currencyapi requests that search, read, convert, or retrieve exchange-rate data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate currencyapi through an OOMOL-connected account, including currency conversion, latest and historical exchange rates, supported-currency metadata, and account quota status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that can execute mutable code without verification.

Mitigation: Do not let an agent run curl-to-bash or Invoke-Expression installer commands automatically; review the installation source and prefer official, versioned, signed, or checksum-verified installation instructions.

Risk: Authentication or connection recovery steps could be triggered unnecessarily.

Mitigation: Only use first-time setup or connection flows after an oo CLI command fails with a matching authentication, connection, or missing-scope error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-currencyapi)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [currencyapi homepage](https://currencyapi.com)
- [currencyapi icon](https://static.oomol.com/logo/third-party/currencyapi.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can include oo CLI commands, connector schema inspection steps, JSON request payloads, and summarized currencyapi results.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
