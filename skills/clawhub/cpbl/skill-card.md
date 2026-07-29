## Description: <br>
Queries Chinese Professional Baseball League scores, schedules, live games, standings, player statistics, news, and Taiwan baseball history for users asking about CPBL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ichendong](https://clawhub.ai/user/ichendong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer CPBL questions with official-site scripts for live scores, schedules, standings, game results, and player statistics. It can also guide historical or awards lookups when official sources do not cover the requested fact. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes a stealth-browser workflow for a third-party site with anti-bot protections. <br>
Mitigation: Prefer the bundled official-site scripts for ordinary CPBL scores, schedules, standings, and statistics; use the third-party history workflow only with permission and terms review. <br>
Risk: Some sports data is obtained from scraped pages or unofficial endpoints that can change or return partial results. <br>
Mitigation: Check returned data for gaps, state uncertainty to users, and fall back to another referenced source instead of inventing missing values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ichendong/cpbl) <br>
- [API endpoints reference](references/api-endpoints.md) <br>
- [Skill summary](references/summary.md) <br>
- [Test report](references/test-report.md) <br>
- [CPBL official news](https://cpbl.com.tw/news) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON from bundled scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke Python scripts through uv and may use web search for recent CPBL news.] <br>

## Skill Version(s): <br>
1.5.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
