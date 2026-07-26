## Description: <br>
Live sports alerts for Soccer, NFL, NBA, NHL, MLB, F1 and more, with real-time scoring through ESPN and optional search fallbacks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to configure favorite teams, check live scores and schedules, generate match-day cron configurations, and receive sports alerts for supported leagues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scanner marked the release suspicious because the skill can use under-disclosed Brave and Serper search fallbacks and may look for web-search-plus environment credentials. <br>
Mitigation: Review before installing, run without search credentials unless those fallbacks are intended, and prevent access to unrelated .env files or web-search-plus credentials. <br>
Risk: Generated cron jobs and Telegram delivery settings can create recurring notifications or execute alerts outside the user's intended schedule. <br>
Mitigation: Inspect generated cron JSON and delivery settings before creating jobs, and enable only the teams, time windows, and notification channels the user expects. <br>
Risk: Sports scores and schedules depend on ESPN plus optional search providers and can be stale, incomplete, or inconsistent. <br>
Mitigation: Treat outputs as alerts and convenience summaries, and verify critical game status or results against an official source before acting on them. <br>


## Reference(s): <br>
- [ClawHub Sports Ticker listing](https://clawhub.ai/robbyczgw-cla/skills/sports-ticker) <br>
- [ESPN site API base URL](https://site.api.espn.com/apis/site/v2/sports) <br>
- [OpenClaw](https://openclaw.com) <br>
- [Brave Search API endpoint](https://api.search.brave.com/res/v1/web/search) <br>
- [Serper search endpoint](https://google.serper.dev/search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Plain text and Markdown summaries with JSON schedule, score, and cron configuration outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3. Uses ESPN by default and may use Brave or Serper search credentials when those fallbacks are available.] <br>

## Skill Version(s): <br>
3.2.0 (source: frontmatter, package.json, changelog, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
