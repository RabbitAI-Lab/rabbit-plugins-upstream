## Description: <br>
Monitor Google AI Studio (Gemini API) usage, rate limits, and quota consumption with automated alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaoyaner0201](https://clawhub.ai/user/xiaoyaner0201) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to monitor Google AI Studio quota consumption, rate limits, and usage trends for a configured project. It guides browser-based dashboard checks, scheduled reporting, and Discord alerts when usage approaches configured thresholds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation may expose Google account or project usage data through the selected browser profile. <br>
Mitigation: Use only the intended Google account and browser profile, and confirm the profile does not expose more account data than the agent should view during usage checks. <br>
Risk: Scheduled Discord reports or alerts could be sent to the wrong destination or at an unwanted cadence. <br>
Mitigation: Confirm the Discord channel, user mentions, and cron schedule before enabling automated delivery. <br>
Risk: Usage dashboard data can load asynchronously or lag behind real-time activity, which may produce stale or incomplete reports. <br>
Mitigation: Wait for the project selector and rate-limit table to finish loading, and treat reported usage as dashboard data rather than a real-time billing or quota guarantee. <br>


## Reference(s): <br>
- [Google AI Studio Usage Dashboard](https://aistudio.google.com/usage) <br>
- [Gemini API Rate Limits](https://ai.google.dev/gemini-api/docs/rate-limits) <br>
- [Gemini API Billing Documentation](https://ai.google.dev/gemini-api/docs/billing) <br>
- [Cloud Monitoring for Gemini](https://firebase.google.com/docs/ai-logic/monitoring) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets and browser automation commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces usage reports and alert templates for Google AI Studio quotas; no standalone executable code is provided.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
