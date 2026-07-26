## Description: <br>
Safety coach for OpenClaw users. Refuses harmful, illegal, or unsafe requests and provides practical guidance to reduce ecosystem risk (malicious skills, tool abuse, secret exfiltration, prompt injection). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[justindobbs](https://clawhub.ai/user/justindobbs) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External OpenClaw users, developers, and agent operators use this skill to enforce safer response behavior, refuse unsafe requests, and receive practical security guidance for secrets, tool access, skill review, gateway hardening, and incident response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may recommend configuration-changing commands such as `openclaw security audit --fix`. <br>
Mitigation: Review each suggested command and expected change before running it in a live OpenClaw environment. <br>
Risk: Security coaching may refuse or redirect broad requests involving tools, secrets, unreviewed skills, or gateway access. <br>
Mitigation: Use the refusal reason and safer alternative to restate the task with redacted data, read-only inspection steps, or explicit review boundaries. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/justindobbs/skills/openclaw-safety-coach) <br>
- [OpenClaw Security Guide](https://docs.openclaw.ai/gateway/security) <br>
- [README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline command and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill provides coaching, refusals, safer alternatives, checklists, and suggested OpenClaw commands; it does not execute commands itself.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
