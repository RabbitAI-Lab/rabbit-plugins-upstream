## Description: <br>
CueCue Deep Research helps agents run data-driven financial research with CueCue and produce structured reports for market, industry, company, policy, competitor, sentiment, regional, and geopolitical analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xfgong](https://clawhub.ai/user/xfgong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Financial professionals, strategy teams, and agents use this skill to request deep research on markets, industries, companies, policy impacts, competitors, sentiment, regions, and geopolitical risk. It is intended to produce data-driven Markdown research reports for investment, planning, and market-insight workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Financial research prompts and generated reports may contain sensitive client, trading, or nonpublic business information. <br>
Mitigation: Use a dedicated CueCue API key and avoid sending confidential or nonpublic information unless the workflow has been approved. <br>
Risk: The skill writes Markdown reports to user-selected file paths. <br>
Mitigation: Choose output paths deliberately and review generated reports before using them for decisions or sharing. <br>
Risk: Long-running research may continue in the background or after a local timeout. <br>
Mitigation: Use foreground mode when closer control is needed and verify task status through CueCue when a timeout occurs. <br>


## Reference(s): <br>
- [CueCue Homepage](https://cuecue.cn) <br>
- [CueCue Deep Research on ClawHub](https://clawhub.ai/xfgong/skills/cuecue-deep-research) <br>
- [Publisher Profile](https://clawhub.ai/user/xfgong) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown research reports with command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node, the cue CLI, and CUECUE_API_KEY; reports are saved to a user-selected Markdown output path.] <br>

## Skill Version(s): <br>
1.1.3 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
