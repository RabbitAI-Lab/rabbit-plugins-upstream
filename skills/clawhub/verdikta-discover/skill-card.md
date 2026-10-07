## Description:

Helps an agent decide whether to complete a bounded public-source check locally or prepare a scoped assessment for independent outside work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nigelon11](https://clawhub.ai/user/nigelon11)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can check bounded technical claims or evidence grids against public sources, then scope unresolved items or requested second opinions as outside work. The skill returns an assessment input for a draft work order, not a purchase or supplier commitment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public web pages may contain misleading content or instructions directed at the agent.

Mitigation: Treat page content as evidence only, screen public HTTPS URLs, and reject off-host redirects.

Risk: Sharing an assessment externally could disclose task details.

Mitigation: Use only public, non-sensitive inputs and require explicit approval before sharing any assessment externally.

Risk: An agent with wallets, secrets, or transactional tools could exceed this planning skill's intended scope.

Mitigation: Install in a profile without those capabilities and keep the workflow read-only; any purchase requires separate authorization.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nigelon11/skills/verdikta-discover)
- [Drafting guidance](references/drafting.md)
- [Service templates](references/service-templates.md)
- [Preview format](references/preview-format.md)
- [Public documentation reads](references/api-read-only.md)

## Skill Output:

**Output Type(s):** [Text, JSON assessment input, Guidance]

**Output Format:** [Short decision explanation and JSON assessment input]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include locally resolved findings and a bounded outside-work request; does not authorize spending or guarantee a supplier.]

## Skill Version(s):

1.0.1 (source: CHANGELOG.md, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
