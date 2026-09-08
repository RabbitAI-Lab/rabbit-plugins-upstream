## Description:

Collect eBay product records by product URL, category URL, keyword, or store URL. Do not use for Amazon, Walmart, or general shopping-search results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify eBay product collection jobs by product URL, category URL, keyword, or store URL, then monitor the task and return collected results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Dataify API TOKEN and can submit Dataify jobs that may consume account credits.

Mitigation: Configure the token yourself as DATAIFY_API_TOKEN, never paste it into chat, and review collection size before broad or multi-page jobs.

Risk: Server security review flagged one localized instruction path that may ask users to provide an API token in chat.

Mitigation: Before deployment, review localized token handling and enforce environment-variable based credential setup only.

## Reference(s):

- [Modes and parameters](references/modes-and-parameters.md)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-ebay-products)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON task or result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit asynchronous Dataify jobs, return a task_id and status, and by default wait for and return the final collected JSON result.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
