## Description: <br>
Save web pages and memos to Cubox using the Open API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liam8](https://clawhub.ai/user/liam8) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to save selected web pages and memo text into Cubox with optional titles, descriptions, tags, and target folders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Cubox API URL is a credential that can save content to the user's account. <br>
Mitigation: Store CUBOX_API_URL privately, avoid sharing it, and verify that it points to the intended Cubox API endpoint before use. <br>
Risk: URLs and memo text sent through this skill are stored in Cubox. <br>
Mitigation: Avoid sending confidential content unless the user is comfortable storing that content in Cubox. <br>
Risk: API calls count against Cubox Premium daily usage limits. <br>
Mitigation: Use the skill only for selected saves and monitor usage against the documented daily API limit. <br>


## Reference(s): <br>
- [Cubox API Help](https://help.cubox.pro/save/89d3/) <br>
- [Cubox](https://cubox.pro) <br>
- [ClawHub Skill Page](https://clawhub.ai/liam8/skills/cubox) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Command-line execution guidance with JSON API responses from Cubox] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Cubox Premium account and a CUBOX_API_URL environment variable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
