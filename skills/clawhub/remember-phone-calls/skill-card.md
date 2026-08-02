## Description: <br>
Remember Phone Calls helps an agent store and recall phone-call context, including who called, why they called, what was agreed, and follow-up promises, using BlueColumn's API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer support, sales, or operations agents use this skill to recall prior caller context and log outcomes, agreements, and follow-up promises after calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive phone-call details may be stored in BlueColumn's remote memory API. <br>
Mitigation: Define what may be stored before use, obtain required consent, and redact sensitive or regulated information from call summaries. <br>
Risk: The skill evidence does not provide enough privacy, retention, or user-control guidance for stored call details. <br>
Mitigation: Confirm retention, deletion, and access-control behavior with the provider before using the skill for real calls. <br>
Risk: The skill requires a BlueColumn API key. <br>
Mitigation: Keep BLUECOLUMN_API_KEY in a secret manager or environment variable and avoid embedding it in shared prompts, files, or logs. <br>


## Reference(s): <br>
- [BlueColumn API reference](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/remember-phone-calls) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with inline bash curl examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BLUECOLUMN_API_KEY; stores and retrieves summarized phone-call details through BlueColumn's remote memory API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
