## Description:

Parses or collects Bilibili video data through HotBee from an explicitly provided bilibili.com or b23.tv URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanye1402-hash](https://clawhub.ai/user/shanye1402-hash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect video data for a public Bilibili URL they explicitly provide, with calls routed through HotBee.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live HotBee calls may consume quota and send the provided Bilibili URL to an external HotBee endpoint.

Mitigation: Confirm user intent before live calls unless already approved, use a scoped HotBee API key when available, and run only on Bilibili URLs intentionally provided by the user.

Risk: The skill relies on trusting the HotBee service and a GitHub-hosted CLI package.

Mitigation: Confirm trust in the HotBee service and CLI package before installing or running, and never echo HOTBEE_API_KEY in output or errors.

## Reference(s):

- [Bilibili Collect API](references/api.md)
- [HotBee Skills](https://www.hotbee.cn/skills)
- [ClawHub Skill Page](https://clawhub.ai/shanye1402-hash/skills/hotbee-bilibili-collect)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with shell commands and API-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses HOTBEE_API_KEY from the local environment and should redact signed query parameters from errors.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
