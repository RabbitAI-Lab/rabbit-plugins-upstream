## Description: <br>
Scheduled WhatsApp briefing for content founders. Runs every Monday at 8 AM. Reads your content calendar file and sends a weekly brief. Covers what is due, what shipped last week, and one suggested focus area. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[desgnpulse](https://clawhub.ai/user/desgnpulse) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content founders use this skill to schedule a weekly OpenClaw brief that summarizes upcoming content work, recent shipped work, and one suggested priority. The skill is aimed at content businesses using TikTok, newsletters, YouTube, or similar channels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled autonomous WhatsApp messages may include sensitive details from recent session logs. <br>
Mitigation: Review whether session logs contain private prompts, customer data, credentials, or sensitive business notes before installing; prefer calendar-derived content only or require preview and approval before messages use session-log information. <br>
Risk: The release evidence flags an inaccurate read-only permission claim because the skill sends WhatsApp messages. <br>
Mitigation: Treat WhatsApp sending as external output and review the messaging scope, recipient, and approval settings before enabling the cron job. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/desgnpulse/skills/weekly-content-brief) <br>
- [TZ Database Time Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with shell command blocks and a short WhatsApp message brief] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scheduled weekly output; runtime brief is intended to fit in one WhatsApp message.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
