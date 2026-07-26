## Description: <br>
Aggregates and filters technology, military, and social news from public domestic and international sources, then organizes results into a structured Markdown briefing for personal news review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External individual users and developers use this skill to ask an agent to collect public news from configured categories, filter duplicate or low-quality results, and produce a short Markdown briefing for situational awareness. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may contact public news sites and reveal news-source access patterns through network traffic. <br>
Mitigation: Run it in an environment with appropriate network and privacy controls for public web access. <br>
Risk: Setup or execution may require visible Python or pip commands. <br>
Mitigation: Review proposed commands before execution and install dependencies only from approved package sources. <br>
Risk: Broad trigger wording could cause automatic selection for tasks outside news aggregation. <br>
Mitigation: Review and narrow trigger conditions if the agent environment relies on automatic skill selection. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/hot-news-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown briefing with categorized news items and optional shell commands for setup or execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require network access to public news sites and local Python dependencies.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
