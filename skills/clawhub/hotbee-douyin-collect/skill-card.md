## Description:

Use when a user wants to parse or collect verified Douyin video, comment, creator, fan portrait, or hashtag data through HotBee APIs using Chinese natural-language instructions and Douyin links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanye1402-hash](https://clawhub.ai/user/shanye1402-hash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn Chinese Douyin analytics requests and explicit public Douyin links or identifiers into HotBee API calls for video, comment, creator, fan portrait, and hashtag data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Key-authenticated HotBee calls may consume account quota.

Mitigation: Confirm user intent before live VIP calls unless the user already approved the spend.

Risk: Audience analytics such as fan-profile data may create privacy obligations.

Mitigation: Use only public or authorized links and identifiers, and handle fan-profile or audience outputs according to applicable privacy requirements.

Risk: Secrets or request query parameters could be exposed in output or errors.

Mitigation: Read HOTBEE_API_KEY only from the local environment, never echo or persist it, and redact request query parameters from errors.

Risk: Some catalog routes were observed as stale and may return incorrect failures.

Mitigation: Use the confirmed routes in references/api.md and explain the contract gap instead of calling stale paths by default.

## Reference(s):

- [Douyin API](references/api.md)
- [HotBee Skills](https://www.hotbee.cn/skills)
- [HotBee Douyin API base](https://www.smsz.xyz/prod-api)
- [ClawHub skill page](https://clawhub.ai/shanye1402-hash/skills/hotbee-douyin-collect)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with inline shell commands and API result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require HOTBEE_API_KEY for VIP endpoints; free endpoints can run without a key.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
