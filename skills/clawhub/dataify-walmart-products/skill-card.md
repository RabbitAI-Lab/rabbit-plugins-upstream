## Description:

Collect Walmart product records by URL, category URL, SKU, or keyword. Do not use for Amazon, eBay, or general shopping-search results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Walmart product collection jobs through Dataify Builder, monitor the asynchronous task, and return collected results. It supports product URL, category URL, SKU, and keyword collection modes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a saved Dataify API TOKEN for third-party Walmart data-collection tasks, which may consume account credits.

Mitigation: Use it only when you intend to send Walmart targets to Dataify, keep DATAIFY_API_TOKEN configured locally outside chat, and confirm multi-page or high-volume scopes before execution.

Risk: Credential exposure is possible if a user pastes a Dataify token into a conversation.

Mitigation: Do not paste the token into chat; configure DATAIFY_API_TOKEN outside the conversation and verify only that it is present, not its value.

Risk: Collection requests send Walmart URLs, SKUs, keywords, and related task parameters to Dataify.

Mitigation: Confirm that the collection targets and any resulting data transfer to Dataify are acceptable before running the task.

## Reference(s):

- [Modes and Parameters](references/modes-and-parameters.md)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-walmart-products)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task or result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May wait for asynchronous Dataify task completion; large JSON result payloads may be summarized while preserving access to raw results.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
