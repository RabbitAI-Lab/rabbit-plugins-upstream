## Description:

Operate Checkout.com customer data through an OOMOL-connected account by inspecting live connector schemas and running supported customer actions with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Checkout.com customers through an OOMOL-connected account, including create, retrieve, update, and delete customer workflows. It guides agents to inspect live connector schemas before constructing payloads and to request confirmation for write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes executing a remote installer for the oo CLI.

Mitigation: Review or replace the installer with a verified installation method, and avoid running installer commands from an elevated shell unless independently verified.

Risk: Create, update, and delete actions can change or remove Checkout.com customer data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

Risk: Incorrect connector inputs can send unintended customer-management requests.

Mitigation: Fetch the live connector schema before constructing each payload and validate the JSON against that schema.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-checkout-com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Checkout.com homepage](https://www.checkout.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas; write and destructive actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
