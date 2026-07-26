## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create practical workflows, checklists, analyses, code changes, or decision support for weather-style productivity workflows on ClawHub. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, AI-agent users, skill authors, maintainers, and teams use this skill to turn weather-style workflow demand into concrete local-friendly plans, templates, checklists, analysis, code changes, or implementation support. It emphasizes clarifying goals, producing actionable artifacts, and validating outputs against the user's success criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on unrelated prompts containing broad terms such as api, key, or bug fix. <br>
Mitigation: Prefer explicit invocation and narrow the trigger terms before deployment when implicit activation could create confusion. <br>
Risk: Workflow guidance may be incomplete or mismatched if the user's goal, inputs, or success criteria are ambiguous. <br>
Mitigation: Restate assumptions, ask only for materially missing information, and validate the final artifact against the stated success criteria. <br>


## Reference(s): <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-weather-current-workflow-helper-005353) <br>
- [Popular ClawHub Weather Skill Demand](https://clawhub.ai/skills/weather) <br>
- [API Key Input Focus Issue](https://github.com/unicef/adt-studio/issues/510) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, templates, and checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only workflow helper; no bundled code execution, persistence, credential access, or hidden data movement.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
