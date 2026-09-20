## Description:

Operate Measure through an OOMOL-connected account using the maple_billing connector for customer, product, pricing, subscription, and checkout workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect Measure action schemas and run Measure customer, product, pricing, subscription, and hosted-checkout workflows through OOMOL. It supports read actions directly and requires user confirmation before write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run write actions that create checkout sessions, create customers, or update customer records in Measure.

Mitigation: Confirm the exact payload and intended effect with the user before running actions tagged as write, following the artifact safety guidance.

Risk: A one-time oo CLI install command fetches and executes a remote installer.

Mitigation: Use official OOMOL documentation or verify the installer before running it, as recommended by the security guidance.

Risk: Measure access depends on a connected OOMOL account with valid credentials and billing status.

Mitigation: Only attempt setup or reconnection after an auth, scope, credential, app, or billing error, and direct the user to the relevant OOMOL connection or billing page.

## Reference(s):

- [Measure homepage](https://getmeasure.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-maple-billing)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to fetch live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
