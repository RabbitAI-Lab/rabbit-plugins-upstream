## Description: <br>
Brainstorm Council runs a structured adversarial brainstorm in which four conflicting expert personas interview the user, develop and defend assigned issues, and a fifth role writes a final report for planning, scoping, and decisions with competing tradeoffs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bystry95](https://clawhub.ai/user/bystry95) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and planners use this skill to pressure-test plans, scope decisions, and surface tradeoffs before committing to a course of action. It is most useful when a decision benefits from conflicting expert perspectives and a standalone final report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The structured debate may consume multiple model calls during one run. <br>
Mitigation: Track the call count, keep the 15-call ceiling, and cut lower-priority issues before cutting the final report. <br>
Risk: Adversarial planning output can still contain incorrect assumptions or recommendations. <br>
Mitigation: Treat the final report as decision support and review conclusions before using them for high-impact decisions. <br>
Risk: The user may confuse the debate transcript with the deliverable. <br>
Mitigation: Keep the final report standalone below the separator, with conclusions, actions, gaps, and risks written independently of the debate. <br>


## Reference(s): <br>
- [Role construction and phase templates](references/roles-and-templates.md) <br>
- [Brainstorm Council ClawHub page](https://clawhub.ai/bystry95/skills/brainstorm-council) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Chat Markdown with debate phases followed by a standalone final report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes no files; uses a maximum 15-call workflow; asks for role approval before proceeding.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
