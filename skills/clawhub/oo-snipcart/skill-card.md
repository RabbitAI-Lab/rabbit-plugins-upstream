## Description:

Snipcart helps agents use the OOMOL Snipcart connector to retrieve customers and orders and list completed orders through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to answer Snipcart account questions by inspecting connector schemas and running oo CLI actions for customer and order lookup or listing through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Snipcart customer and order data through the user's connected OOMOL account.

Mitigation: Approve setup and connector actions only when the requested Snipcart operation is understood, and review payloads carefully before any create, update, or delete action is run.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-snipcart)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Snipcart Homepage](https://snipcart.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from the Snipcart connector.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
