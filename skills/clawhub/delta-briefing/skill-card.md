## Description: <br>
Delta Briefing helps an agent make recurring reports delta-aware by leading with what changed since the previous edition and preserving a state record for the next run. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external stakeholders, and developers use this skill to create recurring briefs that highlight material changes, resolved items, and unchanged items worth watching. It also produces a compact state record that the next run can diff against. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: State records can retain sensitive source details if stored in an unsuitable location. <br>
Mitigation: Decide the state-record location before use and avoid saving sensitive source details unless that location fits the audience and retention needs. <br>
Risk: Recurring briefs can mislead readers if the generated brief and the saved state record diverge. <br>
Mitigation: Review the brief and state record together so the next run diffs against a record that matches the current edition. <br>


## Reference(s): <br>
- [Delta Briefing ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/delta-briefing) <br>
- [Delta Briefing homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/delta-briefing.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json] <br>
**Output Format:** [Markdown brief with an embedded JSON state record] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a concise nothing-changed format when no material delta exists.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
