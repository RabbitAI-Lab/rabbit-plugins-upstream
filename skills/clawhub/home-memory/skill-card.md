## Description: <br>
Enables agents to store, recall, and search household context using BlueColumn persistent memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and home-management agents use this skill to remember household tasks, maintenance reminders, and context across interactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Household context may be sent to and retained by an external BlueColumn memory service. <br>
Mitigation: Get user approval before storing context, and avoid storing access codes, security details, identity data, financial information, or private contacts unless retention and deletion expectations are clear. <br>
Risk: The evidence does not describe clear retention, limits, or deletion guidance for stored household summaries. <br>
Mitigation: Define retention and deletion practices before using the skill for sensitive or long-lived household data. <br>
Risk: The skill requires a BlueColumn API key. <br>
Mitigation: Use a platform secret store for the key and avoid exposing it in prompts, logs, or shared files. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown instructions with inline bash examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and may send household context to an external memory service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
