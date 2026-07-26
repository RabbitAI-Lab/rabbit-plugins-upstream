## Description: <br>
On-screen agent alert: topmost message card + pulsating screen borders via Nameplate. Use before password-manager auth prompts or whenever blocked on the human. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill on macOS to request human attention before blocking prompts, approvals, or other situations where the agent needs input from the human. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill invokes a local Nameplate app and displays alert text visibly on screen. <br>
Mitigation: Install only when the local Nameplate app is trusted, keep alert text concise, and avoid including secrets or sensitive data in messages. <br>


## Reference(s): <br>
- [Nameplate Attention on ClawHub](https://clawhub.ai/steipete/skills/nameplate-attention) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the local Nameplate app; alerts default to 10 seconds, allow a maximum duration of 120 seconds, and drop requests older than 2 minutes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
