## Description: <br>
Daily morning reflection workflow with task sync to Obsidian, Apple Reminders, and Linear. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[marcbickel](https://clawhub.ai/user/marcbickel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and productivity-focused users use this skill to run a daily morning planning workflow, capture reflections in Obsidian, sync tasks to Apple Reminders, and summarize urgent Linear issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Morning reflections and task descriptions can contain sensitive personal or work information. <br>
Mitigation: Review the parsed Obsidian note and reminder changes before relying on or sharing them. <br>
Risk: Free-form tasks may be ambiguous and could create or update the wrong reminder. <br>
Mitigation: Check created and updated Apple Reminders after each run, especially when commitments are phrased informally. <br>
Risk: Linear summaries reflect the issues the agent can access and may include work information. <br>
Mitigation: Limit the agent's Linear access to appropriate teams and review the final summary before distribution. <br>


## Reference(s): <br>
- [Morning Manifesto on ClawHub](https://clawhub.ai/marcbickel/skills/morning-manifesto) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown and text summaries with structured task and issue lists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update Obsidian notes and Apple Reminders, and may query Linear issues available to the agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
