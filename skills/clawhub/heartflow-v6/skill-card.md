## Description: <br>
HeartFlow is an AI cognition engine that analyzes inputs through body-sense, self-sense, judgment, memory, and self-correction workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mark-heartflow](https://clawhub.ai/user/mark-heartflow) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use HeartFlow to add cognitive analysis, memory search, emotion and psychology analysis, reasoning checks, and decision routing to an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can keep local long-term memory of conversations and inferred profile data. <br>
Mitigation: Use it only when local memory persistence is acceptable, avoid secrets or regulated data, and set HEARTFLOW_MEMORY=off when persistence is not wanted. <br>
Risk: Code execution, external service, or daemon features can increase operational risk when enabled. <br>
Mitigation: Enable those capabilities only with explicit intent after reviewing the configured storage paths, execution controls, and service settings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mark-heartflow/skills/heartflow-v6) <br>
- [GitHub repository referenced by artifact](https://github.com/yun520-1/mark-heartflow-skill.git) <br>
- [npm package referenced by artifact](https://www.npmjs.com/package/@yun520-1/heartflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, text analysis, JSON-like status output, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include memory, reasoning, emotion, psychology, and status outputs depending on the invoked HeartFlow tool or CLI command.] <br>

## Skill Version(s): <br>
6.0.0 (source: release evidence, frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
