## Description: <br>
Enables AI agents to store, recall, and search sales objections and follow-ups using BlueColumn persistent memory with a required API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales teams and sales-support agents use this skill to recall objections, follow-up history, and deal notes before interactions, then store updated summaries afterward. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer, deal, or personal sales notes may be sent to an external persistent memory service. <br>
Mitigation: Send only approved, necessary information to BlueColumn and avoid regulated, confidential, or unnecessary personal or customer details unless retention and access controls are understood. <br>
Risk: The BlueColumn API key is required to store and recall sales memory. <br>
Mitigation: Keep the API key in the platform secret store and avoid placing it in prompts, source files, logs, or shared transcripts. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub Sales Memory listing](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/sales-memory) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and sends sales notes to an external persistent memory service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
