## Description: <br>
Generate text-to-video with Wan 2.7 on RunComfy, including guidance for multi-reference conditioning, audio-driven lip-sync, prompt expansion, model routing, and RunComfy CLI invocation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to prepare Wan 2.7 text-to-video requests through the RunComfy CLI, choose suitable parameters, and understand when Wan 2.7 is preferable to adjacent video models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, audio URLs, and referenced media are sent to RunComfy's hosted model service. <br>
Mitigation: Use only content approved for RunComfy processing and avoid submitting sensitive prompts or media unless the deployment policy allows it. <br>
Risk: RunComfy API tokens can grant access to the user's account if exposed. <br>
Mitigation: Keep tokens private, prefer RUNCOMFY_TOKEN in CI or containers, and avoid committing local token files. <br>
Risk: External media URLs used for video generation may contain untrusted or inappropriate content. <br>
Mitigation: Review media sources before use and treat third-party URLs as untrusted inputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/wan-2-7) <br>
- [RunComfy homepage](https://www.runcomfy.com) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=wan-2-7) <br>
- [Wan 2.7 text-to-video model page](https://www.runcomfy.com/models/wan-ai/wan-2-7/text-to-video?utm_source=clawhub&utm_medium=skill&utm_campaign=wan-2-7) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=wan-2-7) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides RunComfy CLI requests for hosted video generation; generated video files are produced by RunComfy.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
