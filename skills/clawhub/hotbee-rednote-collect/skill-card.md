## Description:

Parses a user-provided Xiaohongshu/Rednote note URL through HotBee's verified xhs_note_content endpoint and returns supported note content data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanye1402-hash](https://clawhub.ai/user/shanye1402-hash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect supported content data from a specific public Rednote note URL they provide. Live calls should be confirmed because they may consume HotBee quota.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live calls send the target public Rednote note URL and the HotBee API key to the HotBee service and may consume quota.

Mitigation: Confirm user intent before live calls, read HOTBEE_API_KEY only from the local environment, and never echo the key.

Risk: Using the skill outside its verified scope could bypass platform restrictions or collect sensitive personal information.

Mitigation: Process only explicitly supplied public note URLs, do not bypass access controls or rate limits, and do not invent unsupported account, profile, or search endpoints.

## Reference(s):

- [Rednote Collect API](references/api.md)
- [HotBee Skills](https://www.hotbee.cn/skills)
- [ClawHub Skill Page](https://clawhub.ai/shanye1402-hash/skills/hotbee-rednote-collect)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and returned note content data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses HOTBEE_API_KEY from the local environment and redacts signed query parameters from errors.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
