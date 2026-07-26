## Description: <br>
Flomo Send helps agents configure a flomo webhook and send text notes, links, and tagged memo content to a user's flomo inbox. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qiantao1001](https://clawhub.ai/user/qiantao1001) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to capture thoughts, links, clipboard text, and tagged notes into flomo from an agent workflow or shell command. It is most useful for quick personal knowledge capture where the user has a flomo PRO webhook configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Notes passed to this skill are sent over the network to flomo using a user-configured webhook. <br>
Mitigation: Use it only for content appropriate for flomo and avoid sending secrets or highly sensitive clipboard contents. <br>
Risk: The flomo webhook token grants access to send content into the user's flomo account if exposed. <br>
Mitigation: Prefer the local .env configuration option, keep the token private, and avoid storing it in shared shell profiles. <br>
Risk: Documentation contains a mismatch around URL Scheme behavior while the script performs webhook-only delivery. <br>
Mitigation: Rely on the webhook configuration path and verify the configured FLOMO_WEBHOOK_URL or FLOMO_WEBHOOK_TOKEN before use. <br>


## Reference(s): <br>
- [Flomo API Reference](references/api.md) <br>
- [flomo incoming webhook settings](https://flomoapp.com/mine?source=incoming_webhook) <br>
- [flomo official API help](https://help.flomoapp.com/advance/api.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Sends text content up to 5000 characters through a user-configured flomo webhook; requires flomo PRO, curl, Python 3, and network access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
