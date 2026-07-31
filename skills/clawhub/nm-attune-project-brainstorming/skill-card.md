## Description: <br>
Guides project ideation via Socratic questioning to produce a validated brief. Use before specification when requirements are unclear. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product teams, and project stakeholders use this skill before specification to clarify the problem, constraints, approaches, risks, and decision rationale for a new project. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Brainstorming context may include private business plans, internal constraints, or sensitive stakeholder details that are passed into other skills or subagents. <br>
Mitigation: Review sensitive inputs before use and choose standalone or stop-after-brainstorming options when only a project brief is needed. <br>
Risk: The workflow can edit planning files and continue into downstream specification work without a clear approval gate. <br>
Mitigation: Inspect generated files before allowing downstream specification work, and require human review for project briefs that will drive implementation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-project-brainstorming) <br>
- [Attune plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>
- [Spec Review Loop module](artifact/modules/spec-review-loop.md) <br>
- [Deferred Capture module](artifact/modules/deferred-capture.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown project brief with structured sections, comparison matrices, and occasional inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create planning files such as docs/project-brief.md and .attune/brainstorm-session.json, then continue into review or specification steps unless the user chooses a standalone or stop-after-brainstorming path.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
