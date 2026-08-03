## Description: <br>
Builds and sharpens project domain models by maintaining shared vocabulary in CONTEXT.md and recording qualifying architecture decisions as ADRs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to keep project terminology precise, align code and documentation language, and decide when architecture decisions merit ADR records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs agents to make persistent repository documentation changes and git commits without an explicit approval gate. <br>
Mitigation: Use it only in repositories where agent-made documentation edits are acceptable, and require the agent to show proposed CONTEXT.md or ADR changes and ask before writing files or committing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/domain-modeling) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with proposed repository documentation changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or create CONTEXT.md and ADR files when project terminology or decision records need to be captured.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
