## Description: <br>
NewsToday produces bilingual daily news briefings with curated top stories, Hero Story summaries, financial impact ratings, topic tracking, and optional scheduled or breaking-news alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiajiaoy](https://clawhub.ai/user/jiajiaoy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use NewsToday to generate on-demand or scheduled news briefings from RSS, web search, and hot-list sources, with topic preferences and bilingual Chinese or English output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled news push can create recurring notifications after a user enables it. <br>
Mitigation: Confirm the user wants recurring morning, evening, or breaking alerts before enabling push, and use the provided off command to disable it. <br>
Risk: Personalization stores news preferences in the agent-managed memory profile. <br>
Mitigation: Tell users where preferences are stored and remove the NewsToday profile block when they want that state deleted. <br>
Risk: News briefings and breaking alerts depend on external news sources and may omit, lag, or misstate developing events. <br>
Mitigation: Label sources, cross-check important or disputed claims, and present contested topics without taking a position. <br>


## Reference(s): <br>
- [NewsToday ClawHub page](https://clawhub.ai/jiajiaoy/skills/newstoday) <br>
- [README](README.md) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown briefings and CLI-generated prompts with optional notification configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Bilingual Chinese/English output; optional user preference profile block and runtime-managed push schedule.] <br>

## Skill Version(s): <br>
2.4.0 (source: server release, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
