## Description: <br>
Fetches and parses CCTV News Broadcast (Xinwen Lianbo) highlights for a specified date. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, journalists, and developers use this skill to retrieve date-specific CCTV News Broadcast highlights and convert them into structured news items or summaries for information collection and analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command execution and describes broad scraping, file handling, and automation beyond date-based CCTV news retrieval. <br>
Mitigation: Grant exec or broad file access only with clear command allowlists, source limits, and user approval boundaries. <br>
Risk: Configuration examples refer to API key handling, which can expose credentials if copied into files, prompts, or logs. <br>
Mitigation: Use environment variables or platform-managed secrets, avoid hardcoding credentials, and redact keys from logs and outputs. <br>
Risk: Fetched news content may be incomplete, stale, source-limited, or unsuitable for downstream publication without review. <br>
Mitigation: Review retrieved items against the intended source and apply content, copyright, and accuracy checks before redistribution or decision use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cctv-news-fetcher) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured news items, summaries, configuration guidance, and troubleshooting steps.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
