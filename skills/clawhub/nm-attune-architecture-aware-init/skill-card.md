## Description: <br>
Selects architecture paradigm via research before scaffolding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill when starting a project whose architecture is undecided. It gathers project context, supports current-pattern research, selects an architecture paradigm, adapts scaffolding guidance, and records the decision in an ADR. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Architecture recommendations can be a poor fit if the project context or research synthesis is incomplete. <br>
Mitigation: Review the selected paradigm, rationale, trade-offs, and ADR before relying on the recommendation. <br>
Risk: Following scaffolding or script examples can create files in an unintended location. <br>
Mitigation: Use a fresh or intended output directory and inspect generated changes before keeping them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-architecture-aware-init) <br>
- [Attune homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with code blocks, shell command examples, and project scaffolding or ADR content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use online research and the declared night-market.archetypes:architecture-paradigms configuration for guided paradigm selection.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
