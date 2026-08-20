## Description:

Collects content data for a user-supplied public Xiaohongshu/Rednote note URL through HotBee's verified note-content capability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanye1402-hash](https://clawhub.ai/user/shanye1402-hash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to parse public Xiaohongshu/Rednote note URLs and return verified note-content data through HotBee. The skill is scoped to explicitly supplied public note URLs and requires a local HOTBEE_API_KEY.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may consume HotBee quota or process a Rednote note URL the user is not allowed to submit.

Mitigation: Confirm intent before live calls and use only public Rednote note URLs that the user is allowed to process.

Risk: The HotBee API key could be exposed through prompts, shared logs, or copied error messages.

Mitigation: Read HOTBEE_API_KEY from the local environment only, never echo it, and redact signed query parameters from errors.

Risk: Users may expect broader Rednote collection such as profile or search endpoints.

Mitigation: Limit behavior to verified note-content parsing and do not invent unsupported profile, account, or search endpoints.

## Reference(s):

- [Rednote Collect API](references/api.md)
- [HotBee Skills](https://www.hotbee.cn/skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform a HotBee API-backed collection call when the user confirms intent; returns data for public Rednote note URLs only.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
