## Description: <br>
WeRead AI Brain analyzes WeRead reading data and notes to generate dashboards, book insights, cross-book connections, and exportable knowledge artifacts using a user-provided WeRead API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yamyeed](https://clawhub.ai/user/yamyeed) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External WeRead users and knowledge-management practitioners use this skill to turn WeRead shelves, reading statistics, highlights, and personal thoughts into dashboards, book analysis, cross-book associations, and Markdown or HTML exports after explicit consent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access private WeRead reading data and notes using a user-provided API key. <br>
Mitigation: Install only when that access is acceptable, review the requested data range before each fetch, and approve only the minimum data needed for the task. <br>
Risk: Generated Markdown or HTML exports may contain private reading notes or analysis. <br>
Mitigation: Review export contents and paths before approval, and store generated reports only in locations appropriate for private reading data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yamyeed/skills/weread-ai-brain) <br>
- [Project homepage](https://github.com/yamyeed/weread-ai-brain) <br>
- [WeRead official API gateway](https://i.weread.qq.com/api/agent/gateway) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, single-file HTML dashboards, Markdown exports, concise guidance, and shell command snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read WeRead data through the official HTTPS gateway and may write local export files only after user confirmation.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
