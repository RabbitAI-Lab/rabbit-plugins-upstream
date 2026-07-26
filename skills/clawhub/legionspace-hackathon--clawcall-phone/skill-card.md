## Description: <br>
Give this agent a real phone number to receive user calls, call the user back when tasks complete, run scheduled calls, or call third parties on the user's behalf. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to connect an agent to phone calls through ClawCall, including inbound calls, callbacks, scheduled calls, and third-party call workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can handle real phone calls, call content, and recordings. <br>
Mitigation: Enable it only after confirming caller authorization, consent expectations, and retention rules for calls and recordings. <br>
Risk: The skill may use local profile, task, cron, and memory context in phone responses. <br>
Mitigation: Disable broad local-context injection unless needed and review what local files or OpenClaw data can be included before live use. <br>
Risk: Listener or agent endpoints could route call content to an untrusted destination if misconfigured. <br>
Mitigation: Restrict listener and agent URLs to trusted local or HTTPS endpoints before starting the bridge and listener. <br>


## Reference(s): <br>
- [Clawcall Phone on ClawHub](https://clawhub.ai/legionspace-hackathon/skills/clawcall-phone) <br>
- [Publisher profile](https://clawhub.ai/user/legionspace-hackathon) <br>
- [ClawCall setup reference](references/setup.md) <br>
- [ClawCall service](https://api.clawcall.online) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Spoken phone replies are generated as short text responses for live calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
