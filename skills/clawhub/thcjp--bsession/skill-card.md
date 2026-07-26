## Description: <br>
Bsession helps agents set up browser automation sessions to fetch website information, perform page interactions, and return structured results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users can use this skill to run browser automation for explicit target websites, including one-shot data extraction, page interaction, persistent sessions, and structured result collection. It is not intended for tasks that require complex human judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad shell execution and persistent web automation authority. <br>
Mitigation: Review before installing and require confirmation before shell commands, logins, persistent sessions, scraping, or anti-bot bypass activity. <br>
Risk: Browser automation may expose credentials, sensitive pages, session data, or screenshots. <br>
Mitigation: Use only with explicit target sites and actions, and avoid credentials or sensitive pages unless the data handling path is understood. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bsession) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, configuration, shell commands] <br>
**Output Format:** [Markdown guidance with shell commands and structured JSON results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include execution logs, extracted page data, status metadata, and screenshots when browser actions are performed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
