## Description: <br>
AAR Loop helps agents run After Action Reviews after tasks, capture concrete lessons, and maintain markdown lesson files and an index for future sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akdira](https://clawhub.ai/user/akdira) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to review completed sessions, identify what changed from the plan, and preserve concrete lessons or fix plans that future sessions can consult. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Durable lesson files can persist task context, including sensitive details if used during confidential work. <br>
Mitigation: Avoid using the skill during secrets or sensitive-data work, and review lesson content before any write. <br>
Risk: Broad auto-triggering after every task can create persistent guidance that affects future agent behavior. <br>
Mitigation: Narrow or disable automatic triggers and require explicit approval before writing lesson files. <br>
Risk: Fix plans may propose changes to rules or skills that future sessions load. <br>
Mitigation: Require explicit approval and review before applying any fix that changes future-loaded instructions. <br>


## Reference(s): <br>
- [ClawHub AAR Loop skill page](https://clawhub.ai/akdira/skills/aar-loop) <br>
- [Publisher profile](https://clawhub.ai/user/akdira) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and generated markdown lesson files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update LESSONS.md and files under a lessons/ folder when lesson logging is approved.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact SKILL.md frontmatter states 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
