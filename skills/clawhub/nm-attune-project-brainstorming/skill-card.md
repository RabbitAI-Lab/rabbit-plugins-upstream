## Description: <br>
Guides project ideation via Socratic questioning to produce a validated brief before specification when requirements are unclear. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and product teams use this skill to turn unclear project ideas into a structured project brief with problem definition, constraints, approach comparison, decision rationale, and next steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically pass the full brainstorming context to related skills and review agents. <br>
Mitigation: Use it only with planning context that may be shared with follow-on agents, or run in standalone/skip-review modes when sensitive strategy, legal, security, or product details are involved. <br>
Risk: The skill can write project brief and session-state files during planning. <br>
Mitigation: Review generated files before relying on them, committing them, or using them as inputs to implementation work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-project-brainstorming) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown project brief, JSON session state, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write docs/project-brief.md and .attune/brainstorm-session.json, and may continue into related Attune skills unless bypassed.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
