## Description: <br>
Create and edit Tally forms via API for surveys, feedback forms, and questionnaires, including common question types and a rating workaround. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yujesyoga](https://clawhub.ai/user/yujesyoga) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operations teams use this skill to build, inspect, update, and back up Tally forms programmatically. It is intended for workflows that create surveys, feedback forms, questionnaires, and related form submissions through the Tally API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a local Tally API key that can list, read, and update forms and may access submissions. <br>
Mitigation: Use a dedicated least-privilege API key, store it securely, and install the skill only where Tally access is intended. <br>
Risk: Incorrect form IDs or JSON payloads can modify the wrong form or damage an existing form structure. <br>
Mitigation: Confirm form IDs and payloads before update requests, back up forms before changes, and verify results after each update. <br>
Risk: Downloaded submissions and backup files can contain sensitive response data. <br>
Mitigation: Treat exported submissions and backup files as sensitive data and delete or protect temporary copies after use. <br>


## Reference(s): <br>
- [Tally forms API endpoint](https://api.tally.so/forms) <br>
- [ClawHub skill page](https://clawhub.ai/yujesyoga/skills/tally) <br>
- [Publisher profile](https://clawhub.ai/user/yujesyoga) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON examples and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Tally block structures, API endpoint patterns, update commands, and safe-update practices.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
