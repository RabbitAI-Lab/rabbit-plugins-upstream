## Description: <br>
生成、筛选或解读上市公司违规案例周报，只使用聚源违规案例库及其关联表，并按 LatestInfoPublDate（公告日期/发布时间）选取连续 7 个自然日。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zoeluli7459-dev](https://clawhub.ai/user/zoeluli7459-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and analysts use this skill to generate seven-day listed-company violation reports from the Juyuan violation-case database, including company summaries, violation matters, penalties, legal basis, and deliverable Word, JSON, or Markdown output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts a local weigui MCP service and can be selected automatically for matching violation-report requests. <br>
Mitigation: Install only where access to that local database service is expected, and review implicit invocation behavior before deployment. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/zoeluli7459-dev/skills/weekly-report-companies-violations) <br>
- [违规案例周报字段参考](artifact/references/schema.md) <br>
- [董小屿违规案例库](https://www.dxy-aiagent.com/website/weigui) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON, or generated Word documents, with shell commands for deterministic Word rendering when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a seven-calendar-day reporting window and preserves internal coverage, quality, and missing-field signals in machine data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
