## Description:

BigCommerce lets agents read, create, update, and delete BigCommerce catalog product data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ecommerce operators use this skill to manage BigCommerce catalog products through the OOMOL oo CLI, including listing and retrieving products as well as creating, updating, and deleting products when approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run remote installer scripts on the user's machine.

Mitigation: Install the oo CLI through a trusted package source when possible, or download and inspect the installer before executing it.

Risk: Create, update, and delete actions can change or remove BigCommerce catalog product data.

Mitigation: Review the exact action, target, and JSON payload with the user before write actions, and require explicit approval before destructive deletions.

## Reference(s):

- [ClawHub BigCommerce Skill](https://clawhub.ai/oomol/skills/oo-big-commerce)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [BigCommerce](https://www.bigcommerce.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON command payloads, schema inspection commands, and confirmation guidance for write or destructive actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
