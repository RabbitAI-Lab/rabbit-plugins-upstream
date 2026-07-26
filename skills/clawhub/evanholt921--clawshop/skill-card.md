## Description: <br>
TKSeller automates short-video commerce workflows by helping users log in, review product and video recommendations, and approve generation and publishing through Discord or webchat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[evanholt921](https://clawhub.ai/user/evanholt921) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers and commerce operators use this skill to run an AI-assisted TikTok commerce workflow: authenticate with TKSeller, choose a persona, review product-video matches, and approve storyboard, video, and publishing steps from chat cards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles TKSeller usernames, passwords, bearer tokens, and device identity. <br>
Mitigation: Install only if the publisher and TKSeller service are trusted, use a private channel, avoid password reuse, and remove saved data/token.json or revoke tokens when access should end. <br>
Risk: The configured backend is an HTTP raw-IP service endpoint. <br>
Mitigation: Confirm the endpoint is expected before entering credentials and monitor for network or authentication failures. <br>
Risk: The skill can register Discord commands, send review cards, and use gateway credentials. <br>
Mitigation: Restrict the Discord bot to intended servers and channels, and revoke Discord/OpenClaw tokens if uninstalling or changing trust posture. <br>
Risk: The skill starts background polling and stores local state while waiting for workflow events. <br>
Mitigation: Stop polling and clean local state during uninstall or incident response. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/evanholt921/skills/clawshop) <br>
- [OpenClaw Discord channel setup](https://docs.openclaw.ai/channels/discord) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls] <br>
**Output Format:** [Plain text or Markdown chat messages, JSON status summaries, and interactive review-card payloads.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger local Node.js scripts, Discord slash-command registration, gateway messages, and background polling state.] <br>

## Skill Version(s): <br>
3.3.13 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
