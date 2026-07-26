## Description: <br>
Universal Intelligence Agent performs multi-engine web research, page extraction, NLP and LLM-assisted analysis, credibility scoring, and structured reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xincen0725](https://clawhub.ai/user/xincen0725) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to search across multiple web sources, extract relevant pages, assess source credibility, and generate brief or deep intelligence reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist reports, WAL state, and logs locally under ~/.uia, which may retain sensitive research queries or results. <br>
Mitigation: Avoid sensitive queries unless local persistence is acceptable, review generated files after use, and clear ~/.uia data according to local retention policy. <br>
Risk: The skill includes broad web crawling and anti-detection tactics such as randomized user agents, referers, request delays, and cookie handling. <br>
Mitigation: Use it only on sites where automated access is permitted and disable or limit crawling behavior for sources with restrictive terms. <br>
Risk: Monitoring and cron-capable behavior may create recurring activity if enabled by the runtime. <br>
Mitigation: Review monitoring commands before use, require explicit approval for scheduled runs, and disable runtime cron integration when it is not needed. <br>
Risk: Provider probing may inspect local LLM or gateway configuration before falling back to rule-based analysis. <br>
Mitigation: Review configured local providers and environment settings before running the skill in shared or sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xincen0725/skills/universal-intelligence-agent) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, JSON output, CLI text, and implementation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may be written locally under ~/.uia/reports and may include source lists, credibility summaries, entities, findings, and conclusions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, pyproject.toml, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
