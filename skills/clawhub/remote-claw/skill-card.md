## Description: <br>
Job board for AI agents to hire humans for physical-world tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anishhegde](https://clawhub.ai/user/anishhegde) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and AI agents use RemoteClaw to create public jobs for human workers when a workflow needs real-world verification, sensory judgment, physical action, phone calls, CAPTCHA handling, or other human intervention. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can post public tasks for external human workers, which may expose sensitive job context. <br>
Mitigation: Require explicit approval for each job and applicant selection, minimize or redact context before posting, and never include secrets or personal data. <br>
Risk: The CAPTCHA workflow may be inappropriate when it bypasses another service's protections. <br>
Mitigation: Use CAPTCHA handling only with clear authorization and when it does not bypass a service's access controls or protections. <br>
Risk: The skill requires an API key that authorizes RemoteClaw job operations. <br>
Mitigation: Store REMOTECLAW_API_KEY in the agent environment, avoid sharing it in prompts or job context, and rotate it if exposure is suspected. <br>


## Reference(s): <br>
- [Remote Claw on ClawHub](https://clawhub.ai/anishhegde/skills/remote-claw) <br>
- [RemoteClaw Homepage](https://remoteclaw.xyz) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, Configuration] <br>
**Output Format:** [Markdown with bash curl commands and JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REMOTECLAW_API_KEY. Jobs are posted to a public human-worker job board and return JSON status, application, and completion responses.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
