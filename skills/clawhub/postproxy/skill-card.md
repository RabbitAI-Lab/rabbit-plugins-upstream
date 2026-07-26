## Description: <br>
Postproxy helps agents create, schedule, update, and manage social media posts, comments, direct messages, queues, webhooks, and profile analytics across supported social platforms through the Postproxy API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[danbaranov](https://clawhub.ai/user/danbaranov) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and external users use this skill to let an agent publish or schedule social content, create drafts, manage comments and DMs, configure queues and webhooks, and retrieve social account or post analytics through Postproxy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing posts, comments, replies, or direct messages can create public or private communications from real connected accounts. <br>
Mitigation: Confirm the exact content, media, target profiles, placements, and recipients before acting; prefer drafts when intent is ambiguous. <br>
Risk: Deleting content from social platforms is irreversible, and database-only deletion does not remove already-published platform content. <br>
Mitigation: Confirm the post or comment identity and deletion scope before any delete action, and distinguish database deletion from platform deletion. <br>
Risk: Direct messages and private replies can expose private communications or initiate contact outside normal messaging windows. <br>
Mitigation: Read or send DMs only on explicit request, avoid forwarding DM contents to other tools or public posts without consent, and confirm recipient and text before sending. <br>
Risk: Webhook configuration can send private event payloads to external endpoints, and webhook secrets are credentials. <br>
Mitigation: Use only HTTPS endpoints the user controls and trusts, verify HMAC signatures, and keep API keys and webhook secrets out of logs, chat output, and source control. <br>
Risk: Ambiguous placements can publish to an unintended connected page, organization, board, channel, or location. <br>
Mitigation: Resolve and confirm placements for placement-based networks before publishing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/danbaranov/skills/postproxy) <br>
- [Postproxy Website and API Documentation](https://postproxy.dev) <br>
- [Postproxy API Key Setup](https://app.postproxy.dev/api_keys) <br>
- [Postproxy Skill README](README.md) <br>
- [Postproxy Rule Index](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance, Markdown] <br>
**Output Format:** [Markdown guidance with curl commands, JSON request examples, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires POSTPROXY_API_KEY and curl; actions can affect real connected social media accounts.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release metadata; artifact frontmatter is 2.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
