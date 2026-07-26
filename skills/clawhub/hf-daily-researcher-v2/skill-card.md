## Description: <br>
HF Daily Researcher V2 helps agents search HuggingFace Daily Papers and arXiv, coordinate light scans or deep research, and produce Markdown research reports with analysis and quality checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tomfoxxxx](https://clawhub.ai/user/tomfoxxxx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and researchers use this skill to track recent AI papers, perform deeper literature reviews, and generate structured research reports. It is intended for agents that can search web sources, coordinate sub-agents, manage local configuration, and save Markdown reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read local OpenClaw profile and memory files to infer research interests and may store that context in configuration, history, and report files. <br>
Mitigation: Prefer manual research-topic configuration, review generated config/history/report files, and avoid running it against profiles containing sensitive research context. <br>
Risk: The skill can spawn sub-agents for reading, analysis, writing, and checking, which may produce incomplete or misleading research summaries if intermediate outputs are truncated or weakly verified. <br>
Mitigation: Review the generated report against source papers, keep the checker step enabled, and manually inspect high-priority papers before relying on conclusions. <br>
Risk: The skill has an external Feishu report path when cloud upload is configured. <br>
Mitigation: Keep cloud upload disabled unless the destination and report contents have been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tomfoxxxx/skills/hf-daily-researcher-v2) <br>
- [Publisher profile](https://clawhub.ai/user/tomfoxxxx) <br>
- [arXiv API query endpoint](https://export.arxiv.org/api/query?search_query={query}&max_results=50) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with JSON configuration and occasional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save local report, history, and temporary analysis files; Feishu upload is optional when configured.] <br>

## Skill Version(s): <br>
4.1.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
