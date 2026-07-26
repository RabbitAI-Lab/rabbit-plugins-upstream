## Description: <br>
Daily briefing that connects your recent reading to your long-term archive. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sameerbajaj](https://clawhub.ai/user/sameerbajaj) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to review a daily or on-demand briefing that connects recent Readwise Reader saves with related items from their long-term reading archive. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Readwise reading history and generated summaries are processed by the configured Gemini CLI and sent through WhatsApp. <br>
Mitigation: Install and run the skill only when that data flow is acceptable for the user's reading history and summary content. <br>
Risk: Briefings may be delivered to the wrong WhatsApp recipient if the target number is misconfigured. <br>
Mitigation: Verify TARGET_NUMBER before manual runs or scheduled delivery. <br>
Risk: Automatic scheduling can create recurring privacy-sensitive delivery. <br>
Mitigation: Enable the cron job only when recurring WhatsApp delivery is intended. <br>
Risk: The Readwise token grants access to reading data. <br>
Mitigation: Store READWISE_TOKEN as a secret and avoid exposing it in logs, shell history, or shared configuration. <br>


## Reference(s): <br>
- [Reader Deep Dive on ClawHub](https://clawhub.ai/sameerbajaj/skills/reader-deep-dive) <br>
- [Readwise access token](https://readwise.io/access_token) <br>
- [Readwise Reader list API endpoint](https://readwise.io/api/v3/list/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [WhatsApp-friendly text briefing with markdown-style emphasis and setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires READWISE_TOKEN and TARGET_NUMBER at runtime; uses curl, jq, gemini CLI, and clawdbot.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
