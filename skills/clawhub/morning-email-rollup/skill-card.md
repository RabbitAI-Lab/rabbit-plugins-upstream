## Description: <br>
Daily morning rollup of important emails and calendar events at 8am with AI-generated summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[am-will](https://clawhub.ai/user/am-will) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Employees and individual users use this skill to receive a daily Telegram rollup of important or starred Gmail messages and today's Google Calendar events, with Gemini-generated email summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow handles private Gmail message bodies and calendar event titles, including Gemini summarization and delivery through the configured messaging channel. <br>
Mitigation: Install only after reviewing the Gmail query, Google account, MAX_EMAILS value, messaging channel, and cron schedule for the data you are comfortable processing. <br>
Risk: Email bodies are sent to Gemini for summarization. <br>
Mitigation: Confirm Gemini use is acceptable for the mailbox content before enabling automation, or disable Gemini and rely on the local fallback summary behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/am-will/skills/morning-email-rollup) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown-formatted rollup text with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads Gmail and Calendar data through gog, summarizes email bodies with Gemini, sends the rollup through the configured messaging channel, and logs runs under $HOME/clawd.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
