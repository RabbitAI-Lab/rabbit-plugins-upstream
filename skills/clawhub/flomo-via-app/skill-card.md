## Description: <br>
Sends selected text notes and tags to a user's Flomo inbox through the Flomo webhook API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qiantao1001](https://clawhub.ai/user/qiantao1001) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Users and agents use this skill to capture notes, links, clipboard text, and tagged thoughts into Flomo from shell-based workflows. It is useful for quick personal knowledge capture when a Flomo PRO webhook token is configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected notes are sent to Flomo over the network and may contain sensitive content. <br>
Mitigation: Review note content before sending and only submit information intended for the user's Flomo account. <br>
Risk: A Flomo webhook URL or token is a secret that may be stored locally. <br>
Mitigation: Prefer the local .env configuration with restricted permissions and avoid committing or sharing the token. <br>
Risk: Older documentation mentions URL scheme behavior while the current script is webhook-only. <br>
Mitigation: Configure FLOMO_WEBHOOK_URL or FLOMO_WEBHOOK_TOKEN and rely on the current webhook-based script behavior. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/qiantao1001/skills/flomo-via-app) <br>
- [Flomo API Reference](references/api.md) <br>
- [Flomo Incoming Webhook Settings](https://flomoapp.com/mine?source=incoming_webhook) <br>
- [Flomo Official API Documentation](https://help.flomoapp.com/advance/api.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with bash command examples and plain-text note payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Sends at most 5000 characters per note; tag text is appended to content before submission.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
