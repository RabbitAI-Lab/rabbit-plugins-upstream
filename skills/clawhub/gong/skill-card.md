## Description: <br>
Gong helps an agent search Gong calls, transcripts, users, meeting data, and conversation analytics through the Gong API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jdrhyne](https://clawhub.ai/user/jdrhyne) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and sales or revenue operations teams use this skill to let an agent retrieve Gong users, calls, transcripts, call details, and activity statistics with user-supplied Gong credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive Gong call recordings, transcripts, users, and activity data when credentials are supplied. <br>
Mitigation: Use a dedicated least-privilege Gong API key and avoid sharing raw transcripts or activity data in insecure channels. <br>
Risk: Misconfigured credentials or base URL could expose requests to the wrong endpoint or broaden access beyond the intended Gong account. <br>
Mitigation: Restrict permissions on ~/.config/gong/credentials.json and confirm the configured base_url is the official Gong API domain for the account. <br>


## Reference(s): <br>
- [ClawHub Gong skill listing](https://clawhub.ai/jdrhyne/skills/gong) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash and JSON examples; helper commands return JSON or text from Gong API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Gong credentials JSON file and may return sensitive call, transcript, user, and activity data.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
