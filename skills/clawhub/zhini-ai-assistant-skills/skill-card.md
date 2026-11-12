## Description:

Connects customer profiles and conversation history across supported social, messaging, and web support accounts to AI tools for customer lookup, conversation analysis, segmentation, lead discovery, and user-confirmed messaging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhinikefu](https://clawhub.ai/user/zhinikefu)

### License/Terms of Use:

MIT-0

## Use Case:

Customer service and sales teams use the skill to search customer profiles and conversation history across connected accounts, analyze conversations, identify leads, and prepare follow-up. It can open selected conversations and send messages after the user confirms the recipients and content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customer profiles and conversations may contain sensitive personal or business information.

Mitigation: Query only the accounts and records needed for the user's request, and include only relevant details in the response.

Risk: Bulk outreach could reach unintended customers or send unapproved content.

Mitigation: Show the selected recipients and final message content for explicit user confirmation before creating a sending task.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zhinikefu/skills/zhini-ai-assistant-skills)
- [知你 AI 助手 API Key management](https://ai.zhinikefu.com/api-key/)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured text or Markdown summaries and reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include query scope, evidence identifiers, customer analysis, and per-recipient messaging task status.]

## Skill Version(s):

1.1.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
