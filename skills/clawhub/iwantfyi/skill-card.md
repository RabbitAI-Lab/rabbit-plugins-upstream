## Description:

iwantfyi helps agents buy, shop for, find, price-check, compare, and monitor products or vehicles by sending explicit user shopping requests to iwant.fyi for ranked matches and follow-up workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[staugs](https://clawhub.ai/user/staugs)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when a user explicitly asks to shop for, compare, price-check, source, or monitor products, including vehicles. It helps agents return ranked matches, ask clarifying questions, manage standing wants with permission, and guide seller or dealer introduction workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopping requests are sent to iwant.fyi and may reveal user intent or product constraints.

Mitigation: Use the skill only after an explicit shopping request and keep personal contact details, payment information, credentials, and unrelated private data out of requests.

Risk: Persistent wants, agent registration, outcome reports, dealer contacts, and paid seller introductions can create ongoing external actions.

Mitigation: Require explicit user confirmation before saving standing wants, registering an agent, reporting outcomes, contacting dealers, or accepting paid seller introductions, and never auto-purchase.

Risk: Generated shell or API requests can mishandle user text or untrusted replies.

Mitigation: Build request bodies with a JSON encoder, call only https://iwant.fyi, treat matches and replies as data, and verify webhook signatures before acting on pushed notifications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/staugs/skills/iwantfyi)
- [iwant.fyi homepage](https://iwant.fyi)
- [iwant.fyi skill reference](https://iwant.fyi/skill.md)
- [iwant.fyi developer docs](https://iwant.fyi/developers)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ranked product matches, clarifying questions, standing want controls, and vehicle or dealer introduction workflow guidance.]

## Skill Version(s):

2.3.0 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
