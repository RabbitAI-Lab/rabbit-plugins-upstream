## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams turn proactive-agent workflow needs into practical plans, checklists, artifacts, analysis, implementation support, and verification notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to convert proactive workflow requests into concise work plans, reusable checklists, implementation artifacts, analysis, code changes, or decision support. It emphasizes local-hardware-friendly methods and validates outputs against the user's stated success criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked too often because its trigger terms are broad. <br>
Mitigation: Prefer explicit invocation by skill name when using it, and confirm the user's goal before producing artifacts for ambiguous requests. <br>
Risk: Workflow outputs may include incorrect or incomplete plans, code changes, or guidance if the user's constraints are missing. <br>
Mitigation: Ask only for missing information that materially changes the result, make assumptions visible, and validate the output against the stated success criteria. <br>


## Reference(s): <br>
- [ClawHub Skill Release Page](https://clawhub.ai/kyro-ma/skills/work-productivity-proactive-agent-workflow-helper-120606) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Popular ClawHub Skill Demand: Proactive Agent](https://clawhub.ai/skills/proactive-agent) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, configuration snippets, checklists, and concise verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are tailored to the user's immediate request and should expose assumptions, limits, required inputs, remaining risks, and follow-up work when relevant.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
