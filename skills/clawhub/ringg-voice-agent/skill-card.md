## Description: <br>
Integrates Ringg AI voice agents with OpenClaw so agents can make and manage phone calls, launch campaigns, retrieve call status, history, analytics, and transcripts, manage assistants, and configure Ringg as a voice provider. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[siddharthpilani](https://clawhub.ai/user/siddharthpilani) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to connect OpenClaw agents to Ringg AI for outbound calls, campaign launches, call monitoring, analytics retrieval, transcript access, assistant management, and webhook-based call events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place real outbound calls and launch campaigns without enough documented confirmation, consent, or opt-out safeguards. <br>
Mitigation: Require explicit approval before every call or campaign, preview recipients and campaign size, and confirm lawful consent and opt-out handling before execution. <br>
Risk: The skill can retrieve call history, analytics, and transcripts that may contain sensitive customer or business information. <br>
Mitigation: Restrict transcript and history access, use the least-privileged Ringg key available, and limit access to authorized operators. <br>
Risk: Webhook handling is documented without sufficient operational safeguards for authenticity and replay protection. <br>
Mitigation: Use HTTPS, verify signing secrets, check replay windows, and maintain a cleanup process for stale webhook endpoints. <br>


## Reference(s): <br>
- [Ringg AI API Reference](references/api_reference.md) <br>
- [Ringg AI](https://www.ringg.ai) <br>
- [Ringg AI API Docs](https://docs.ringg.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May result in live Ringg API requests when executed by an agent with valid Ringg credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
