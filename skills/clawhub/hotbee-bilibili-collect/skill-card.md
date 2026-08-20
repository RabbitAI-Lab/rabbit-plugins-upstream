## Description:

Use when a user wants to parse or collect Bilibili video data through HotBee from a bilibili.com or b23.tv URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanye1402-hash](https://clawhub.ai/user/shanye1402-hash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect video data for public Bilibili or b23.tv URLs that they explicitly provide. The skill calls HotBee with a local HOTBEE_API_KEY and returns the collected Bilibili video data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a HotBee API key and third-party HotBee service calls.

Mitigation: Install only if the HotBee service is trusted, keep HOTBEE_API_KEY private, and do not echo credentials in outputs or errors.

Risk: Live collection may consume HotBee quota and should only target public Bilibili links supplied by the user.

Mitigation: Confirm intent before live calls unless already approved, and avoid bypassing login, access controls, rate limits, or platform restrictions.

## Reference(s):

- [Bilibili Collect API](references/api.md)
- [HotBee Skills](https://www.hotbee.cn/skills)
- [ClawHub skill page](https://clawhub.ai/shanye1402-hash/skills/hotbee-bilibili-collect)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and returned video data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires HOTBEE_API_KEY and an explicit public Bilibili or b23.tv URL; live calls may consume HotBee quota.]

## Skill Version(s):

1.0.3 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
