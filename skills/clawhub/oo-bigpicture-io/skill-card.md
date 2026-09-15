## Description:

BigPicture.io helps agents search and read company data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up BigPicture.io company profiles by domain name or IPv4/IPv6 address through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance includes download-to-shell installer commands, which can execute remote code locally.

Mitigation: Review OOMOL's official installation guide first and run installer commands only when the source is trusted and the local-code-execution risk is understood.

Risk: Routine lookups send domains or IP addresses through the OOMOL BigPicture.io connector.

Mitigation: Submit only lookup values appropriate for the connected account and the user's data-sharing expectations.

## Reference(s):

- [BigPicture.io homepage](https://bigpicture.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bigpicture-io)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
