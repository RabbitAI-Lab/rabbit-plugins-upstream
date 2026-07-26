## Description: <br>
Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenleiyanquan](https://clawhub.ai/user/chenleiyanquan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering agents use this skill to handle code review feedback with technical verification before making changes. It guides the agent to clarify unclear feedback, evaluate reviewer suggestions against the codebase, push back when technically warranted, and implement verified fixes one item at a time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may lead an agent to inspect local project files while verifying review feedback. <br>
Mitigation: Use it only in repositories where the agent is authorized to read the project files needed for code review. <br>
Risk: The skill may suggest GitHub review-thread replies or gh api commands that could post or modify repository discussion content. <br>
Mitigation: Review any GitHub command or drafted reply before allowing the agent to publish it. <br>
Risk: The skill intentionally encourages skeptical, terse review handling, which may be unsuitable for some collaboration norms. <br>
Mitigation: Install it only when technical verification and concise review responses match the team's expected workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chenleiyanquan/skills/receiving-code-review) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with concise review replies, code-change summaries, and inline commands when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce GitHub review-thread reply guidance and commands when the agent is working in a repository review workflow.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
