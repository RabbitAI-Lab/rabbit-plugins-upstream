## Description: <br>
Automatically helps users generate PPT presentations from requirements such as length, scenario, tone, role, and supplied files including documents and images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[skeyjia6](https://clawhub.ai/user/skeyjia6) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to prepare presentation outlines, select an AIPPT template, and request a generated PPT preview link from the AIPPT service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated presentation content is sent to a third-party AIPPT service. <br>
Mitigation: Use only data approved for that provider, and avoid confidential, regulated, or proprietary documents unless the provider is authorized for that use. <br>
Risk: AIPPT_ACCESS_TOKEN can grant access to the external service if exposed. <br>
Mitigation: Keep the token out of prompts, source control, logs, screenshots, and shared generated artifacts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/skeyjia6/aippt) <br>
- [AIPPT website](https://www.jcppt.com/) <br>
- [AIPPT template list API](https://ppt-api.7niuai.com/ppt/tpl/list) <br>
- [AIPPT generate PPT API](https://ppt-api.7niuai.com/openclaw/generate_ppt_by_content) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, API calls, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated PPT preview links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and AIPPT_ACCESS_TOKEN.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
