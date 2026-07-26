## Description: <br>
Firehose monitors the web in real time by letting users create Lucene rules on taps and consume matching crawled pages through an SSE stream. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tysg](https://clawhub.ai/user/tysg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to work with Firehose API tasks, including tap management, rule authoring, query validation, and consuming live match streams. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Firehose credentials for tap, rule, and streaming operations. <br>
Mitigation: Prefer the tap token for rule and stream work, and provide the management key only when creating or managing taps. <br>
Risk: Tap and rule deletion are permanent and can immediately stop matches or revoke access. <br>
Mitigation: Review delete actions carefully and use pause for temporary tap stops when appropriate. <br>


## Reference(s): <br>
- [Firehose](https://firehose.com) <br>
- [Firehose Introduction](https://docs.firehose.com/get-started/introduction.md) <br>
- [Firehose Authentication](https://docs.firehose.com/get-started/authentication.md) <br>
- [Stream Overview](https://docs.firehose.com/stream/overview.md) <br>
- [Rules and Query Syntax](https://docs.firehose.com/stream/rules.md) <br>
- [Streaming SSE](https://docs.firehose.com/stream/streaming.md) <br>
- [Management-Key Endpoints](https://docs.firehose.com/api-reference/management-key-endpoints.md) <br>
- [Tap-Token Endpoints](https://docs.firehose.com/api-reference/tap-token-endpoints.md) <br>
- [Errors and Limits](https://docs.firehose.com/api-reference/errors-and-limits.md) <br>
- [ClawHub Skill Release](https://clawhub.ai/tysg/skills/firehose-api) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline bash commands and API endpoint examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl plus FIREHOSE_TAP_TOKEN for rule and stream work; FIREHOSE_MANAGEMENT_KEY is needed for tap management.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
