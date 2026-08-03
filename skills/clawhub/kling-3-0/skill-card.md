## Description: <br>
This skill helps agents prepare and run Kling 3.0 text-to-video and image-to-video generations on RunComfy across Standard, Pro, and 4K tiers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and creative teams use this skill to generate short cinematic videos from text prompts or public image URLs through RunComfy-hosted Kling 3.0 endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RunComfy video generations can cost money and may produce large output files. <br>
Mitigation: Confirm tier, duration, audio setting, and output directory before running a generation. <br>
Risk: Prompts, public image URLs, and RunComfy authentication tokens are involved in normal use. <br>
Mitigation: Use only prompts and image URLs suitable for RunComfy processing, and protect RUNCOMFY_TOKEN or the local RunComfy token file. <br>
Risk: Image-to-video modes require publicly fetchable HTTPS image URLs. <br>
Mitigation: Use source images that are intentionally shareable and verify URL accessibility before generation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/kling-3-0) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction) <br>
- [RunComfy Kling 3.0 model page](https://www.runcomfy.com/models/kling/kling-3.0) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce RunComfy CLI invocations, input settings, and output-directory guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
