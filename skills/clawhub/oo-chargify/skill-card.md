## Description:

Maxio Advanced Billing helps agents search and read Maxio customer, product, and subscription data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to retrieve Maxio Advanced Billing customers, products, and subscriptions through documented OOMOL connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read billing records that may include sensitive customer, product, or subscription information.

Mitigation: Limit requests and outputs to the user's stated task, and avoid storing or sharing returned billing data outside the active workflow.

Risk: First-time setup may ask the user to install the oo CLI, sign in, connect Maxio, or resolve billing issues.

Mitigation: Run setup only after a matching command failure, review any install or login prompts, and use the documented connection and billing URLs only when needed.

Risk: A future or undocumented Maxio task could change billing data even though this artifact documents only get and list actions.

Mitigation: Require separate explicit user approval for any task that would create, update, delete, or otherwise mutate Maxio billing data.

## Reference(s):

- [Maxio Advanced Billing homepage](https://www.maxio.com/product/advanced-billing)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The artifact documents read-only get and list actions for Maxio customers, products, and subscriptions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
