## Description: <br>
Twitter Trend Radar helps agents find early product, tool, game, and SEO opportunity signals from X/Twitter by using the local bird CLI to search launch-signal tweets with links, extract domains, check RDAP domain age, score opportunities, and output Markdown or JSON reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kevin-free](https://clawhub.ai/user/kevin-free) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and product researchers use this skill to scan public X/Twitter launch signals for early product, AI app, browser game, and SEO/GEO opportunities. It helps prioritize candidates for manual validation and landing-page ideation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on the external bird CLI and may use the user's browser X/Twitter session for searches. <br>
Mitigation: Confirm bird configuration before use, keep operation read-only, and avoid accounts where rate limiting or blocking would be unacceptable. <br>
Risk: X/Twitter searches and RDAP lookups can vary by account, location, endpoint behavior, and rate limits. <br>
Mitigation: Use conservative query volume, rely on cached results when appropriate, and manually verify high-scoring opportunities before acting on them. <br>
Risk: Local caches and reports can contain tweet data, linked domains, and sensitive research topics. <br>
Mitigation: Store reports in an appropriate workspace and review or clear cache and report files when the research topic is sensitive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kevin-free/skills/twitter-trend-radar) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON reports, with shell command examples and follow-up guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may be printed to stdout or written to a user-specified local file; local cache files may be created under the configured cache directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
