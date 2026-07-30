## Description: <br>
seedance helps an agent generate AI videos from text, reference images, or first and last frames using the doubao-seedance-2.0 model. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiangsier-xyz](https://clawhub.ai/user/jiangsier-xyz) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to turn natural-language video requests, optional images, and generation settings into a confirmed video-generation run that returns the resulting video URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can bootstrap a runtime environment by downloading installer code and installing dependencies before use. <br>
Mitigation: Review the wrapper before installation, prefer a prebuilt locked environment with pinned dependencies, and avoid get-pip fallback in restricted environments. <br>
Risk: Prompts, images, and generated media requests may be sent to Volcengine/Ark and Alibaba OSS when the skill is used. <br>
Mitigation: Use only prompts and images approved for those services, and avoid sending confidential or regulated content unless that is allowed by your environment. <br>
Risk: The skill depends on live API and OSS credentials that may be stored in a local .env file. <br>
Mitigation: Store credentials according to local secret-management policy, avoid committing .env files, and rotate keys if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiangsier-xyz/skills/seedance) <br>
- [Volcengine Ark video generation documentation](https://docs.volcengine.com/docs/82379/2298881) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated video URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns the final video URL and optionally a saved MP4 path.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
