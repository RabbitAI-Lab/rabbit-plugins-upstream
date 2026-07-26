## Description: <br>
Aoment Image Video helps agents use Aoment AI services for text-to-image, image-to-image, image recognition, video generation, HD image repair, quota checks, and API key registration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[regalzzz](https://clawhub.ai/user/regalzzz) <br>

### License/Terms of Use: <br>
Aoment AI custom terms <br>


## Use Case: <br>
Developers and agents use this skill to call Aoment AI media services for generating and editing images, generating videos, recognizing image content, repairing or upscaling images, checking quota, and registering an Agent API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, images, videos, audio, and recognition inputs are sent to Aoment services. <br>
Mitigation: Use only data intended for Aoment, avoid sensitive media and internal or private URLs, and store the Agent API key securely. <br>
Risk: The HD repair workflow can fetch a supplied web URL from the user's machine and upload the result to Aoment. <br>
Mitigation: Prefer local files or trusted public URLs, and review supplied URLs before running HD repair. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/regalzzz/aoment-image-video) <br>
- [Aoment website](https://www.aoment.com) <br>
- [Aoment skill package download](https://www.aoment.com/downloads/aoment-image-video-skill.zip) <br>
- [Aoment Discord community](https://discord.gg/3BMzRd7bJx) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [JSON responses and Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an Aoment Agent API key; generated media results are returned as URLs, and video-seedance-2 requires whitelist access.] <br>

## Skill Version(s): <br>
1.6.0 (source: evidence.release.version and SKILL.md Current Version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
