## Description: <br>
Give AI agents persistent coaching memory for tracking goals, progress, notes, and recall through BlueColumn. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to store, recall, and update coaching context so an AI coach can track user goals and progress across interactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Coaching goals, progress notes, risks, and summaries may be sent to an external persistent memory service. <br>
Mitigation: Use explicit user consent, avoid storing highly sensitive personal information, and define retention and deletion workflows before production use. <br>
Risk: A BlueColumn API key is required to call the memory endpoints. <br>
Mitigation: Store the key in a platform secret store and use a dedicated scoped key for this skill. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/coaching-memory) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and sends coaching text, queries, titles, and tags to BlueColumn endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
