## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create local-friendly Gog-style Google Workspace productivity workflows, checklists, analyses, code changes, and decision support for fixing bugs, hardening setup and safety, improving reliability, or creating adjacent skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn Google Workspace and Gog-style productivity requests into practical workflows, templates, checklists, analysis, code changes, or decision support. It is intended for local-friendly planning and implementation support around Gmail, Calendar, Drive, Contacts, CLI workflows, setup hardening, reliability, and related productivity automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Google and productivity triggers may lead an agent toward sensitive Gmail, Calendar, Drive, Contacts, or workspace data. <br>
Mitigation: Use the skill as planning and checklist guidance, and require explicit user confirmation before any agent reads, changes, or exports sensitive workspace data. <br>
Risk: Workflow or code suggestions can be incorrect or incomplete for a user's specific Google Workspace setup. <br>
Mitigation: Validate outputs against the stated success criteria, surface assumptions and limits, and review changes before deployment. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper-060415) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Gog ClawHub skill demand signal](https://clawhub.ai/skills/gog) <br>
- [Google Workspace storage demand signal](https://news.ycombinator.com/item?id=48969253) <br>
- [Local notes workflow demand signal](https://news.ycombinator.com/item?id=48968447) <br>
- [OpenTelemetry reliability issue demand signal](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/708) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, templates, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should include visible assumptions, validation notes, and remaining risks or next steps when helpful.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
