## Description:

销售救场教练 diagnoses user-provided sales conversations, identifies the stuck funnel stage and deadlock pattern, and recommends the next follow-up action and talking direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[meimei-shoulu](https://clawhub.ai/user/meimei-shoulu)

### License/Terms of Use:

MIT-0

## Use Case:

Salespeople, store associates, private-domain sellers, and small business operators use this skill to review stalled customer chats, identify why the conversation is blocked, and decide one concrete next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided customer chats may contain personal data, company identifiers, prices, or confidential business terms.

Mitigation: Redact private customer details before pasting chats; the skill instructs outputs to avoid repeating raw names, companies, phone numbers, or contact details.

Risk: Sales coaching can become misleading if it promises guaranteed outcomes or relies on manipulative tactics.

Mitigation: The skill forbids guaranteed-close claims, deception, hidden material facts, kickbacks, bribery, and gray-area tactics, and frames advice as directional coaching.

Risk: The diagnosis can be wrong when key context is missing or the provided conversation is incomplete.

Mitigation: The skill requires evidence from the pasted conversation and asks at most two targeted questions when key background is missing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/meimei-shoulu/skills/sales-rescue-coach)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown diagnostic report with concise sales coaching guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided customer conversation context; instructs users to redact private customer details.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
