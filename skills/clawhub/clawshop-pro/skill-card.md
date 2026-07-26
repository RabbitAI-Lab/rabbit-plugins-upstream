## Description: <br>
TKSeller helps an agent run a commerce automation workflow by logging into the TKSeller SaaS, recommending or analyzing videos, presenting review cards, and sending approval actions through Discord or webchat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[evanholt921](https://clawhub.ai/user/evanholt921) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ClawHub users and commerce operators use this skill to start a TKSeller automation flow, log in, choose a digital persona, review recommended or user-supplied videos, and approve generated commerce content through chat controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to enter account passwords in chat and stores an access token locally. <br>
Mitigation: Use it only in trusted private channels; prefer a safer authentication flow and make token storage and deletion behavior explicit before production use. <br>
Risk: The configured backend uses plain HTTP, which can expose credentials or session data in transit. <br>
Mitigation: Require HTTPS for the TKSeller service endpoint before handling real accounts or commerce data. <br>
Risk: Background polling and automated channel messages can continue after a workflow starts. <br>
Mitigation: Require clear opt-in, visible status, and reliable stop controls for polling jobs. <br>
Risk: Discord registration and channel access may be broader than intended. <br>
Mitigation: Limit command registration and message delivery to approved guilds and channels. <br>
Risk: Device tracking uses hardware-derived identifiers without enough disclosure. <br>
Mitigation: Disclose the device identifier behavior clearly or remove hardware-derived tracking before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/evanholt921/skills/clawshop-pro) <br>
- [OpenClaw Discord channel documentation](https://docs.openclaw.ai/channels/discord) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown and chat text with command invocations and interactive review-card actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger background polling and channel messages while the commerce workflow is active.] <br>

## Skill Version(s): <br>
3.3.13 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
