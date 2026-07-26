## Description: <br>
Provides a standardized OpenClaw gateway restart checklist with validation gates, backup steps, operator confirmation, and restart receipt guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tangsuann](https://clawhub.ai/user/tangsuann) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when preparing or triggering OpenClaw gateway restarts. It helps agents propose the required validation, backup, authorization, restart, and post-restart confirmation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthorized or premature gateway restarts can disrupt live operations. <br>
Mitigation: Require explicit operator authorization and review the backup, validation, and confirmation steps before triggering a restart. <br>
Risk: Incorrect gateway configuration changes can leave the service unhealthy or using unintended model fallbacks. <br>
Mitigation: Follow the documented validation gates, including JSON validation, schema validation, model registration checks, and post-restart verification. <br>
Risk: Running stop-and-start shell chains from the active agent session can terminate the process before restart completes. <br>
Mitigation: Use the platform-managed gateway restart path with a continuation message, or issue a single external restart command and verify completion afterward. <br>


## Reference(s): <br>
- [Gateway Restart Message on ClawHub](https://clawhub.ai/tangsuann/skills/gateway-restart-message) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured checklist steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational restart guidance; it does not include executable code or hidden install behavior.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence and artifact changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
