## Description:

SamCart (samcart.com). Use this skill for ANY SamCart request: searching and reading customer, order, product, and subscription data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and business operators use this skill to retrieve SamCart customers, orders, products, and subscriptions through the OOMOL connector without handling raw SamCart API tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner flagged remote installer execution during first-time setup.

Mitigation: Review the installer source, prefer a verified installation method, and only install the OOMOL CLI when it is needed for the task.

Risk: The skill can access SamCart business and customer data through OOMOL-connected credentials.

Mitigation: Use an OOMOL/SamCart connection with appropriate access, and treat connector responses as sensitive business data.

Risk: Authority boundaries may be ambiguous if live connector schemas expose actions beyond the documented read actions.

Mitigation: Inspect the live connector schema before execution and require explicit user approval for any write or destructive action.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/oomol/skills/oo-samcart)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [SamCart Homepage](https://www.samcart.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data payload and meta.executionId when actions run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
