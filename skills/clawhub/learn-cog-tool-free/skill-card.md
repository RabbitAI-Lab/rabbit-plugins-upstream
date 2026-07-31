## Description: <br>
A free cognitive learning skill that helps agents plan spaced repetition, active recall, knowledge graph building, cognitive load analysis, and structured learning outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to structure personal learning workflows, generate review plans or flashcards, analyze cognitive load, and return structured learning results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad local command and file capabilities for a loosely scoped learning workflow. <br>
Mitigation: Run it in a controlled workspace and approve command execution and file changes case by case. <br>
Risk: The optional callback URL can send results to a network endpoint. <br>
Mitigation: Use callback URLs only for trusted endpoints and avoid sending sensitive learning content or local paths. <br>
Risk: The security verdict is suspicious because the requested authority is broader than the documented workflow needs. <br>
Mitigation: Review the generated plan and any proposed commands before deployment or repeated use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/learn-cog-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON, YAML, Python, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local read, command execution, and file-writing actions; users should approve actions case by case.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
