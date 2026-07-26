## Description: <br>
Schedule and manage social media posts through a Postiz API, including multi-platform scheduling, media upload, thread creation, deduplication checks, and post management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolmanns](https://clawhub.ai/user/coolmanns) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and social media managers use this skill to create, schedule, validate, list, update, and delete Postiz-managed social posts across supported channels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes hardcoded Postiz credentials, a specific Postiz host, and fixed social-account integration IDs. <br>
Mitigation: Rotate the exposed password, revoke existing sessions, remove hardcoded credentials, and make the host, account, and integration IDs user-configurable before use. <br>
Risk: The helper scripts can create, schedule, publish, update, delete, and query social media posts on connected accounts. <br>
Mitigation: Use only accounts you control, review generated post content and target channels before execution, and run deduplication checks before publishing. <br>
Risk: Session cookies are persisted to a shared temporary path. <br>
Mitigation: Store cookies in a user-private secure location, avoid persistent cookies where possible, and revoke sessions after setup or testing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolmanns/skills/postiz-ext) <br>
- [Publisher profile](https://clawhub.ai/user/coolmanns) <br>
- [Configured Postiz dashboard](https://postiz.home.mykuhlmann.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and Python helper scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May perform live Postiz API calls when helper scripts or generated commands are run; outputs can include validation messages, post records, media IDs, and scheduling status.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
