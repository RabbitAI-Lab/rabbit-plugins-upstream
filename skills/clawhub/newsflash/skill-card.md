## Description: <br>
Personalized daily news briefings and real-time breaking-news alerts from newsflash.sh, a deduped news event graph where every event carries a corroboration count and confidence score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zatmonkey](https://clawhub.ai/user/zatmonkey) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People who follow news, markets, crypto, or specific topics use this skill to get concise interest-based briefings, ask ad-hoc news questions, and receive breaking-news alerts with corroboration signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: News topics, interests, and alert preferences may be sent to the Newsflash CLI/API and stored locally in newsflash.json. <br>
Mitigation: Use the skill only when sharing those preferences with Newsflash is acceptable, and delete newsflash.json or run the CLI logout flow when local preferences or credentials should no longer be retained. <br>
Risk: Recurring briefings and live alerts can schedule cron work or keep a background stream running. <br>
Mitigation: Enable recurring briefings or live alerts only when ongoing scheduling or streaming is intended, and stop the schedule or stream when it is no longer needed. <br>
Risk: Single-source news events may be unconfirmed. <br>
Mitigation: Keep single-source items out of the main briefing, label them as one-outlet reports, or place them in a watchlist until corroborated. <br>


## Reference(s): <br>
- [Newsflash homepage](https://newsflash.sh) <br>
- [ClawHub skill page](https://clawhub.ai/zatmonkey/skills/newsflash) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown briefing text with inline links, JSON-backed preferences, and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update newsflash.json in the workspace and may run npx newsflash or curl when the user requests briefings, search, login, upgrades, or live alerts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
