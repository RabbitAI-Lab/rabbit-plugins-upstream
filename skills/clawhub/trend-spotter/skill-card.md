## Description: <br>
Trend Spotter helps agents produce ranked social and cultural trend reports with brand-fit scores, trend lifecycle calls, cultural timing, and go/skip recommendations for campaign planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, influencer, and social strategy teams use this skill to decide which trends, hashtags, formats, and cultural moments are worth acting on for a brand or industry. The skill produces a ranked trend report with timing windows, brand-fit scoring, watch and avoid lists, and concrete campaign recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trend reports and selected conclusions may be saved into project memory. <br>
Mitigation: Review or delete memory/influencer/trend-spotter reports and memory/hot-cache entries if brand plans, audience assumptions, or recommendations should not be retained. <br>
Risk: Trend recommendations can be incomplete or time-sensitive when based on single-source or estimated signals. <br>
Mitigation: Treat single-source signals as estimated and corroborate important recommendations with multiple sources before committing campaign spend. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/trend-spotter) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Trend Spotter templates](references/templates.md) <br>
- [Keyless multi-source trend scout](references/trend-scout-recipe.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown trend reports with tables and optional shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write trend reports to memory/influencer/trend-spotter and promote durable conclusions to memory/hot-cache when local memory is available.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
