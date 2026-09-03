## Description:

AppGrowing intelligent ad creative analysis assistant with Strategy Exploration (chat_mode=6) and Inspiration (chat_mode=10) modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcloud](https://clawhub.ai/user/youcloud)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing teams use this skill to analyze AppGrowing ad creative data, explore advertising strategy, and generate creative inspiration through the disclosed AppGrowing API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send prompts and an AppGrowing API key to a disclosed external API.

Mitigation: Review before installing, configure YOUCLOUD_API_KEY as an environment variable, and avoid pasting API keys into chat.

Risk: Broad trigger phrases can activate external API calls unintentionally.

Mitigation: Use explicit commands such as /ag, /agclaw, or /ag-inspire and review activation behavior before deployment.

## Reference(s):

- [AppGrowing homepage](https://appgrowing.cn/)
- [agclaw ClawHub skill page](https://clawhub.ai/youcloud/skills/agclaw)
- [Publisher profile](https://clawhub.ai/user/youcloud)
- [Usage examples](references/example.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis text with optional shell command and API configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call an external AppGrowing API using YOUCLOUD_API_KEY and return the API-provided markdown output.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
