## Description: <br>
Finance Memory helps agents store, recall, and search budget and financial context in BlueColumn persistent memory using a BlueColumn API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to remember, store, and retrieve finance notes, budgets, spending summaries, and related financial context across interactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive financial notes, budgets, spending summaries, and inferred financial context may be sent to and persisted by BlueColumn memory. <br>
Mitigation: Use the skill only with explicit user consent, send the minimum necessary or redacted data, and define retention and deletion expectations before use. <br>
Risk: The skill depends on a BlueColumn API key and an external service endpoint for storing and recalling financial context. <br>
Mitigation: Keep the API key in the platform secret store, avoid exposing it in prompts or logs, and review external-service suitability before deployment. <br>


## Reference(s): <br>
- [BlueColumn API Docs](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/finance-memory) <br>
- [Publisher profile](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and sends finance-related text to an external persistent memory service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
