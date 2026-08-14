## Description:

Printify (printify.com). Use this skill for Printify requests: reading, creating, and updating data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to work with Printify shops, products, and orders through an authenticated OOMOL connector. It guides agents to inspect live action schemas before running connector commands and to confirm actions that may change Printify state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Printify shop, product, and order information through a connected OOMOL account, including potentially sensitive customer or business data in order records.

Mitigation: Confirm the user's intent before retrieving order details, limit requests to the needed shop or order scope, and avoid exposing customer or business data unnecessarily.

Risk: Some connector actions may change Printify state.

Mitigation: Inspect the live action schema first and get explicit user confirmation for any action tagged as write or destructive before running it.

## Reference(s):

- [ClawHub Printify skill listing](https://clawhub.ai/oomol/skills/oo-printify)
- [Printify homepage](https://printify.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
