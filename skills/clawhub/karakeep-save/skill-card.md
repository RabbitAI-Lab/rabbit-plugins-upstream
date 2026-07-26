## Description: <br>
Save bookmarks to Karakeep, a self-hosted bookmark manager, when the user wants to save a URL, bookmark a link, or add something to a reading list. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickian](https://clawhub.ai/user/nickian) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and users with a self-hosted Karakeep instance use this skill to save a URL and optional note into their bookmark collection from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user-provided bookmark URLs and optional notes to the configured Karakeep server. <br>
Mitigation: Use a trusted HTTPS KARAKEEP_URL and avoid saving sensitive URLs or notes unless that data is intended to be stored on that server. <br>
Risk: The skill uses a Karakeep API key for authenticated bookmark creation. <br>
Mitigation: Use a revocable API key and rotate or revoke it if the execution environment or saved configuration is exposed. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, text, configuration] <br>
**Output Format:** [Shell command invocation with text status output; the Karakeep API response includes JSON containing the bookmark ID.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires KARAKEEP_URL and KARAKEEP_API_KEY environment variables, plus curl and jq in the execution environment.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
