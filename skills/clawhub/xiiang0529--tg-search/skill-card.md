## Description: <br>
Searches public Telegram channels and groups by keyword and returns up to 50 matching results as JSON using an authorized Telethon session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiiang0529](https://clawhub.ai/user/xiiang0529) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to search public Telegram channels and groups by keyword from an environment that already has an authorized Telethon session and the local tg_search command installed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a local authorized Telegram search setup and the /usr/local/bin/tg_search command. <br>
Mitigation: Install and use it only in environments where tg_search comes from a trusted source and use of the configured Telethon session is approved. <br>
Risk: Search results are limited to public, searchable Telegram channels and groups, so private or invite-only chats are outside scope. <br>
Mitigation: Treat the output as public-search discovery results and do not rely on it for complete Telegram coverage. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xiiang0529/skills/tg-search) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Text] <br>
**Output Format:** [JSON array or JSON error object] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns public Telegram channel or group matches with type, title, username, and id fields; limit defaults to 10 and is capped at 50.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
