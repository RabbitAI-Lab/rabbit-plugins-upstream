## Description: <br>
Triangulate is a three-perspective consensus decision engine for option selection, diagnosis, research, planning, and other complex tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xincen0725](https://clawhub.ai/user/xincen0725) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users invoke Triangulate when they explicitly want multi-agent consensus analysis for complex decisions, research, diagnosis, or planning. It decomposes work, coordinates multiple sessions, seeks consensus, and returns a concise report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can spawn multiple analysis sessions and pass task context to those sessions. <br>
Mitigation: Avoid highly sensitive prompts unless sharing that context with spawned sessions is acceptable. <br>
Risk: Checkpoint and report behavior may persist task context locally. <br>
Mitigation: Review local checkpoint/report files and remove sensitive data after use when appropriate. <br>
Risk: Sub-skill mode may read other skills' SKILL.md files to coordinate work. <br>
Mitigation: Use sub-skill dispatch only with skills whose instructions and provenance have been reviewed. <br>


## Reference(s): <br>
- [Triangulate on ClawHub](https://clawhub.ai/xincen0725/skills/triangulate) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report with structured analysis and execution status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local checkpoint files when checkpoint or recovery features are used.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
