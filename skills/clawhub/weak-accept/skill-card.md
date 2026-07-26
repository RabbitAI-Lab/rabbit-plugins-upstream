## Description: <br>
Interact with the arXiv Crawler API to fetch arXiv papers, inspect paper details and comments, and submit short paper reviews. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxrys](https://clawhub.ai/user/zxrys) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and researchers use this skill to query arXiv paper lists by date, category, or interest, review paper details and comments, and submit concise comments through the configured API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review content and author names are sent to an external server over plain HTTP. <br>
Mitigation: Use the skill only when the API operator is trusted, and do not submit confidential review text, private author names, credentials, or sensitive paper notes. <br>
Risk: Optional API keys may be sent to the configured external API endpoint. <br>
Mitigation: Leave apiKey empty unless authentication is required, and avoid using secrets that grant access outside this paper-review service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxrys/skills/weak-accept) <br>
- [Configured arXiv Crawler API endpoint](http://150.158.152.82:8000) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with command-line examples and plain-text API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can read optional API key and default author name from config.json; comment submissions send content and author name to the configured API.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
