## Description:

TaxJar (taxjar.com). Use this skill for ANY TaxJar request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate TaxJar through an OOMOL-connected account, including calculating sales tax, retrieving rates, validating VAT numbers, and managing customers, order transactions, refund transactions, tax categories, and nexus regions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create, update, refund, and delete actions can change or remove TaxJar records.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive TaxJar actions.

Risk: The one-time CLI install step runs a remote installer.

Mitigation: Use the install step only when the oo CLI is missing, and review or trust OOMOL's official install path before executing it.

Risk: Incorrect connector payloads can produce wrong tax, customer, order, or refund changes.

Mitigation: Inspect the live action schema with oo connector schema before constructing JSON payloads.

## Reference(s):

- [ClawHub TaxJar skill page](https://clawhub.ai/oomol/skills/oo-taxjar)
- [TaxJar homepage](https://www.taxjar.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON when actions run with --json.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
