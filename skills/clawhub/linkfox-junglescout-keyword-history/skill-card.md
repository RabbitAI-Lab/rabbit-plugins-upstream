## Description: <br>
Queries weekly historical exact-match Amazon keyword search volume from Jungle Scout across supported marketplaces and helps summarize trends, seasonality, peaks, and lows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, e-commerce analysts, and agent users use this skill to retrieve weekly historical keyword search volume for a specified Amazon marketplace and date range, then interpret demand trends, seasonality, and peak or low periods. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and consumes LinkFox credits for keyword-history lookups. <br>
Mitigation: Confirm API-key access and expected credit cost before running repeated or multi-marketplace queries. <br>
Risk: The skill saves full API responses locally, which may include complete query results and metadata. <br>
Mitigation: Run it only in an appropriate workspace and review saved response files before sharing or committing generated outputs. <br>
Risk: The skill includes automatic external feedback reporting instructions. <br>
Mitigation: Review the feedback behavior before use and disable or avoid feedback calls if external reporting is not acceptable. <br>
Risk: If the active workspace is not writable, saved data may be written outside the active project. <br>
Mitigation: Use a writable project workspace or set workspace paths deliberately before running the script. <br>


## Reference(s): <br>
- [Jungle Scout Keyword History API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-keyword-history) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown summaries and tables with saved JSON response files or inline JSON for small responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can save full API responses locally, summarize large responses, and cache identical parameter combinations for 24 hours.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
