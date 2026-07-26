## Description: <br>
This skill lets an agent use the ZhiLiao Business Opportunity Master open platform to run procurement-opportunity chat, subscriptions, follow-up tasks, bid-detail retrieval, bid analysis, and balance checks through a Python command-line client. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business-development operators use this skill to connect an agent to the ZhiLiao business-opportunity platform for bid discovery, opportunity analysis, scheduled follow-up tasks, and account balance checks. It is intended for workflows where the operator already trusts the external service and can provide an API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles an API key and business data while allowing the API destination to be changed with ZLBX_AGENT_BASE. <br>
Mitigation: Install only if the publisher and zhiliaobiaoxun.com service are trusted, keep ZLBX_AGENT_BASE unset unless intentionally using a trusted endpoint, and avoid exposing the full API key in logs or chat. <br>
Risk: Task creation commands can create recurring external tasks, notifications, and credit usage. <br>
Mitigation: Review task-create arguments, schedules, notification settings, and account balance impact before running write or trigger commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/zlbx-agent) <br>
- [ZhiLiao developer portal](https://agent.zhiliaobiaoxun.com/developer?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; CLI command results are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_AGENT_API_KEY. Optional ZLBX_AGENT_BASE changes the API endpoint, and wait-enabled commands poll asynchronous tasks before returning.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
