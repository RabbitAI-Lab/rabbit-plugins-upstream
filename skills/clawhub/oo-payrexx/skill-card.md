## Description:

Payrexx lets agents read and create Payrexx payment data through an OOMOL-connected account using the `payrexx` connector and `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Payrexx gateways, transactions, and payment providers, and to create payment gateways after confirming write-action payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path asks users to execute remote installer scripts directly.

Mitigation: Install only after trusting OOMOL's CLI distribution path; prefer reviewing the installer or using a signed package or pinned release when available.

Risk: Creating a payment gateway changes Payrexx state.

Mitigation: Confirm the exact write-action payload and intended effect with the user before running the action.

## Reference(s):

- [Payrexx homepage](https://payrexx.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions can change Payrexx state and should be run only after confirming the exact payload and effect with the user.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
