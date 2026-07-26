## Description: <br>
Bridge to external vertical agents (Google ADK, VeADK, etc.) for specialized tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sqsge](https://clawhub.ai/user/sqsge) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to forward domain-specific tasks to a configured external agent over HTTP, such as financial analysis, enterprise knowledge lookup, legal review, or custom backend workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries sent through this skill are shared with the configured remote service. <br>
Mitigation: Install it only for remote agents you control or trust, and avoid sending sensitive data unless the remote service is approved for that data. <br>
Risk: A misconfigured or untrusted REMOTE_AGENT_URL can route prompts and responses to the wrong service. <br>
Mitigation: Verify REMOTE_AGENT_URL before use and prefer controlled, trusted endpoints. <br>
Risk: Long-lived or overly broad bearer tokens can expand impact if exposed. <br>
Mitigation: Use a scoped, revocable REMOTE_AGENT_KEY when authentication is needed. <br>
Risk: Disabling TLS verification can expose traffic to interception in normal use. <br>
Mitigation: Avoid --insecure except in controlled testing with non-sensitive data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sqsge/skills/clawhub-skill-remote-agent) <br>
- [Google ADK documentation](https://google.github.io/adk-docs/) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON or text returned by the remote agent endpoint] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REMOTE_AGENT_URL; REMOTE_AGENT_KEY is optional for bearer-token authentication.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
