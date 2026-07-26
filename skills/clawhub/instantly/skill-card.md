## Description: <br>
Instantly API integration with managed OAuth for managing cold email campaigns, leads, sending accounts, email workflows, and analytics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Instantly through Maton's managed API gateway, including managing campaigns, leads, sending accounts, email workflows, and analytics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Approved write actions can create, modify, delete, send, reply to, or forward business email and lead data in the connected Instantly workspace. <br>
Mitigation: Confirm the target connection, resource, recipient or campaign, and intended effect with the user before any write request. <br>
Risk: Using the wrong Instantly connection can apply actions to the wrong account or workspace. <br>
Mitigation: When multiple connections exist, require the intended connection and include the documented Maton-Connection header. <br>
Risk: The Maton API key grants access to connected Instantly resources. <br>
Mitigation: Keep MATON_API_KEY in the environment only, do not print it in outputs, and install the skill only when the user intends Maton-mediated Instantly access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/instantly) <br>
- [Maton homepage](https://maton.ai) <br>
- [API Gateway skill](https://clawhub.ai/byungkyu/api-gateway) <br>
- [Instantly API V2 documentation](https://developer.instantly.ai/api-reference) <br>
- [Instantly API introduction](https://developer.instantly.ai/) <br>
- [Instantly Help Center](https://help.instantly.ai/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python, JavaScript, HTTP, and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, a MATON_API_KEY environment variable, and user approval before write operations.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
