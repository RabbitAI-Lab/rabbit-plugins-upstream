## Description:

Operate Semrush through an OOMOL-connected account to search and read SEO data such as domain overview metrics, organic keywords, and organic competitors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO analysts, and other external users use this skill to retrieve Semrush domain overview, organic keyword, and organic competitor data through the OOMOL Semrush connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include one-line remote installer commands for the oo CLI.

Mitigation: Review the installer delivery path before execution; prefer a verified, versioned, package-manager, checksum, or manually inspected install method.

Risk: Connector calls depend on live Semrush action schemas and an active OOMOL-connected Semrush account.

Mitigation: Inspect the live action schema before constructing payloads and use first-time setup only after auth, connection, scope, expiration, or billing errors.

Risk: Future connector actions tagged as write or destructive could alter Semrush state.

Mitigation: Confirm the exact payload and effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Semrush Skill](https://clawhub.ai/oomol/skills/oo-semrush)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Semrush Homepage](https://www.semrush.com/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Semrush connector data and an execution id under meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
