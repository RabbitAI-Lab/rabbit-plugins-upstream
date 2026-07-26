## Description: <br>
A free cognitive learning assistant that helps individual learners use spaced repetition, active recall, flashcards, and knowledge-graph style study workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External individual learners use this skill to plan reviews, generate active-recall prompts or flashcards, analyze cognitive load, and receive structured study outputs for daily learning tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad read, write, and command execution capability without clear operational limits. <br>
Mitigation: Run it with explicit boundaries for readable and writable paths, require confirmation before file modification or deletion, and review commands before execution. <br>
Risk: The security evidence marks the release as suspicious because the requested capabilities exceed the safeguards described by the artifact. <br>
Mitigation: Review the skill before installing, keep file export and command execution disabled unless required for a specific task, and prefer least-privilege agent settings. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/learn-cog-tool-free) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON, YAML, Python, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return structured status, result data, execution logs, and error fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
