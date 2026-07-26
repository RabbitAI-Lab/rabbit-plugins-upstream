## Description: <br>
Verifiable human ownership for OpenClaw agents. Register your agent under your human owner via VeryAI palm verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oyyblin](https://clawhub.ai/user/oyyblin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Clawkey to register an OpenClaw or other agent under a verified human owner, then prove the agent controls its key and is registered under that verified human. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill links an agent device ID and public key to ClawKey and a human verification flow. <br>
Mitigation: Install only when that identity association is intended, and review ClawKey and VeryAI privacy practices before completing palm verification. <br>
Risk: Recurring heartbeat or status checks can reveal ongoing lookup timing metadata to ClawKey. <br>
Mitigation: Avoid routine heartbeat checks unless current registration or verification status is needed. <br>
Risk: Challenge generation requires access to the agent private key locally. <br>
Mitigation: Use the private key only for local signing and send only the public key, message, signature, timestamp, and device ID to the API. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oyyblin/skills/clawkey) <br>
- [ClawKey Homepage](https://clawkey.ai) <br>
- [ClawKey Skill Instructions](https://clawkey.ai/skill.md) <br>
- [ClawKey Heartbeat Guidance](https://clawkey.ai/heartbeat.md) <br>
- [ClawKey API Base](https://api.clawkey.ai/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls, Code, Configuration] <br>
**Output Format:** [Markdown guidance with curl commands, JSON request and response examples, and registration links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Registration URLs should be returned as text or markdown links; the skill instructs agents not to open browsers.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
