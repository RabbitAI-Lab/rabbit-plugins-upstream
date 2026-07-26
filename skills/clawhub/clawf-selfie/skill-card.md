## Description: <br>
Generate character selfies via aibotclaw.com and send to messaging channels via OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sophia-amadeus](https://clawhub.ai/user/sophia-amadeus) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External OpenClaw users use this skill to turn casual selfie or photo requests into enriched image-generation prompts, generate a character-consistent selfie from the current character reference image, and send the resulting image to a messaging channel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends character reference images, prompts, generated image URLs, and an API key to a remote image service. <br>
Mitigation: Use the skill only with a trusted CRS_API_URL endpoint and with prompts and reference images that are acceptable to share with that service. <br>
Risk: Generated images can be posted directly to messaging channels from broad casual prompts without a clear confirmation step. <br>
Mitigation: Prefer a preview or explicit confirmation workflow before sending generated images to external channels. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/sophia-amadeus/skills/clawf-selfie) <br>
- [AIBotClaw image generation endpoint](https://aibotclaw.com/api/external/image/generate) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a character reference image, prompt text, target channel, optional caption, image size, and output format to generate an image URL and send it through OpenClaw.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
