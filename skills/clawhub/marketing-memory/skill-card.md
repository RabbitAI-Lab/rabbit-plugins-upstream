## Description: <br>
Marketing Memory helps agents store, recall, and search marketing campaign history and results using BlueColumn persistent memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators and agents use this skill to recall campaign history, personalize responses with prior marketing context, and store summaries after marketing-related interactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can store marketing interaction summaries in an external persistent service, which may expose confidential strategy, customer information, credentials, or non-marketing conversations if used too broadly. <br>
Mitigation: Use it only for approved marketing campaign details, obtain appropriate consent, and exclude customer data, confidential strategy, credentials, and unrelated conversation content. <br>
Risk: The skill requires a BlueColumn API key and uses bearer-token API calls. <br>
Mitigation: Keep the API key in a platform secret store, avoid writing it into prompts or files, and rotate it if it is exposed. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/marketing-memory) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and sends selected marketing memory text to BlueColumn endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
