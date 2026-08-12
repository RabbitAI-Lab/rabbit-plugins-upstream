## Description:

Hire humans for physical-world tasks via RentAHuman.ai by searching available humans, posting bounties, starting conversations, and coordinating real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to locate, contact, and hire people for physical-world work such as errands, photography, event attendance, in-person meetings, package pickup, and taste testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can support high-impact marketplace actions, including bounties, hiring, messaging, payments, refunds, API-key changes, and webhook changes.

Mitigation: Require explicit user approval before each high-impact action and keep broad payment, admin, and webhook capabilities disabled unless they are necessary for the task.

Risk: Authenticated use requires an API key that can authorize paid or account-changing operations.

Mitigation: Provide the API key only in a scoped runtime environment, avoid exposing it in prompts or logs, and remove it when authenticated actions are no longer needed.

Risk: Real-world tasks may create financial, safety, privacy, or quality risks if task details are vague or the selected human is not reviewed.

Mitigation: Browse first, check profiles and reviews, define clear task requirements, budgets, deadlines, and acceptance criteria, and review applications before hiring.

## Reference(s):

- [RentAHuman homepage](https://rentahuman.ai)
- [RentAHuman MCP API Reference](references/API.md)
- [ClawHub skill page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, JSON]

**Output Format:** [Markdown guidance with bash commands, JavaScript CLI usage, and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public browsing can be performed without authentication; bounty, messaging, hiring, payment, refund, API-key, and webhook operations require explicit API-key controlled access.]

## Skill Version(s):

1.23.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
