## Description:

Parses Chinese Douyin data requests and uses HotBee APIs to collect video, comment, creator, fan portrait, and hashtag data from public Douyin links or identifiers provided by the user.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanye1402-hash](https://clawhub.ai/user/shanye1402-hash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn Chinese natural-language Douyin data requests into HotBee CLI/API calls for public video, creator, comment, fan portrait, and hashtag data. It is intended for user-provided public Douyin links or identifiers, with confirmation before key-authenticated calls that may consume HotBee quota.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Key-authenticated HotBee API calls can use HOTBEE_API_KEY and may consume HotBee quota.

Mitigation: Confirm intent before key-authenticated live calls, read the key only from the local environment, and never echo or persist it.

Risk: Public Douyin links or identifiers submitted by the user are sent to a third-party HotBee API.

Mitigation: Only process public Douyin links or identifiers that the user explicitly provides and intends to submit.

Risk: Some Douyin catalog routes are stale and may fail or produce a contract gap.

Mitigation: Use the confirmed executable routes in references/api.md and explain the current contract gap instead of calling stale paths.

## Reference(s):

- [Douyin API reference](references/api.md)
- [HotBee Skills capability directory](https://www.hotbee.cn/skills)
- [HotBee Douyin Collect on ClawHub](https://clawhub.ai/shanye1402-hash/skills/hotbee-douyin-collect)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and API result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require HOTBEE_API_KEY for VIP endpoints; credentials and request query parameters should be redacted from user-facing output.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
