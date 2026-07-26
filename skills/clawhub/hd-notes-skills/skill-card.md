## Description: <br>
话袋笔记 Skill helps agents create, update, search, and retrieve personal notes through the Huadai OpenAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[monkeydb](https://clawhub.ai/user/monkeydb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to connect an agent to Huadai notes, configure an API key, save new notes, search existing notes, and update a selected note after confirming its unique_id. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Note content, search queries, and the Huadai API key may be sent to Huadai or to an environment-overridden API URL. <br>
Mitigation: Install only if that data sharing is acceptable, and verify HUADAI_BASE_URL is unset or exactly https://openapi.ihuadai.cn/open/api/v1 before use. <br>
Risk: Write operations can create or update personal notes. <br>
Mitigation: Confirm the target unique_id before updates and rely on code=200 before treating a save or update as complete. <br>
Risk: Highly sensitive material saved through the skill is handled by the Huadai service. <br>
Mitigation: Avoid storing secrets or highly sensitive notes unless the user trusts the service and its data handling. <br>


## Reference(s): <br>
- [API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/monkeydb/hd-notes-skills) <br>
- [ClawHub Release Page](https://clawhub.ai/monkeydb/skills/hd-notes-skills) <br>
- [Source Repository](https://github.com/monkeyDB/hd-notes-skills) <br>
- [Huadai OpenAPI Base URL](https://openapi.ihuadai.cn/open/api/v1) <br>
- [Huadai Open Platform](https://ihuadai.cn/desktop/openai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API calls] <br>
**Output Format:** [Markdown or plain text with optional shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires HUADAI_API_KEY for Huadai OpenAPI requests.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
