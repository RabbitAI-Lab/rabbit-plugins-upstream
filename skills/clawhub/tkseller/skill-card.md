## Description: <br>
TKSeller automates short-video commerce workflows by helping users log in, request TikTok video recommendations or analysis, review generated cards, and approve storyboard, video, and publishing steps through Discord or webchat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[evanholt921](https://clawhub.ai/user/evanholt921) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, ecommerce operators, and developers use this skill to coordinate a TikTok commerce workflow from recommendation through review, video generation, and publication approval. It is intended for users who can provide TKSeller account credentials and manage Discord or webchat-based review actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles TKSeller usernames, passwords, device binding data, local OpenClaw channel tokens, and chat bot administration. <br>
Mitigation: Install only when the publisher and backend are trusted; use a dedicated low-privilege TKSeller account and non-production Discord or Feishu credentials where possible. <br>
Risk: The security summary flags insecure transport and weak disclosure around backend and external service setup. <br>
Mitigation: Review the configured service endpoint and channel setup before use, and avoid sending production credentials until the transport and operational model are acceptable. <br>
Risk: The skill may keep a local polling process running and cache media or workflow state locally. <br>
Mitigation: Monitor and stop the polling process when work is complete, and periodically review or remove local cached state and media files. <br>


## Reference(s): <br>
- [TKSeller ClawHub skill page](https://clawhub.ai/evanholt921/skills/tkseller) <br>
- [OpenClaw Discord channel documentation](https://docs.openclaw.ai/channels/discord) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with shell command invocations and interactive review-card content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger background polling, local state files, media caching, and outbound API calls to the TKSeller service and configured chat channels.] <br>

## Skill Version(s): <br>
3.4.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
