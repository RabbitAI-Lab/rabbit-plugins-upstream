## Description: <br>
Transforms project briefs into testable specifications with user stories and acceptance criteria. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and project teams use this skill after brainstorming to turn briefs and business requirements into testable specifications with scope boundaries, user stories, acceptance criteria, and validation strategy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically continue from specification into planning after saving docs/specification.md. <br>
Mitigation: Use the --standalone option or explicitly ask the agent to stop after the specification when planning should not begin automatically. <br>
Risk: Generated specifications may contain incomplete or incorrect requirements if the project brief is ambiguous. <br>
Mitigation: Review the generated specification, acceptance criteria, and scope boundaries before using them for implementation planning. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-project-specification) <br>
- [Attune homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown specification guidance and checkpoint text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May continue into planning unless the user requests standalone specification work or stops after the specification.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
