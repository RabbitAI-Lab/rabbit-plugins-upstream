## Description:

AppGrowing ad creative analysis assistant that helps users explore ad strategies and generate creative inspiration through AppGrowing's YouCloud API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcloud](https://clawhub.ai/user/youcloud)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing teams use this skill to analyze AppGrowing ad creative data, explore campaign strategies, and generate creative concepts or scripts. It requires an AppGrowing/YouCloud API key with appropriate product access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expose an API key by pasting it into chat.

Mitigation: Prefer configuring YOUCLOUD_API_KEY as an environment variable; rotate the key if it is pasted into chat.

Risk: User prompts and analysis requests are sent to the AppGrowing/YouCloud service.

Mitigation: Install and use the skill only if the publisher and service are trusted, and avoid sending sensitive or confidential campaign data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youcloud/skills/agclaw)
- [AppGrowing homepage](https://appgrowing.cn/)
- [AppGrowing YouCloud API endpoint](https://aichat-appgrowing-cn.youcloud.com/aichat/ag/claw)
- [Usage examples](references/example.md)
- [Material detail URL template](https://appgrowing-cn.youcloud.com/material/{{ID}})

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with optional command snippets and material links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires YOUCLOUD_API_KEY and relays AppGrowing API responses to the user.]

## Skill Version(s):

1.1.2 (source: server release metadata; artifact frontmatter is 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
