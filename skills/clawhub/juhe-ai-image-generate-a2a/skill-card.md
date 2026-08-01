## Description: <br>
Generates images from user prompts through Juhe's paid AI image service, using an A2M/HTTP 402 payment flow with Alipay and saving generated images locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to request paid AI image generation from a text prompt, choose a supported aspect ratio, complete payment through Alipay, and receive the generated image on the user's device. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill initiates a paid image-generation workflow. <br>
Mitigation: Require clear user confirmation before collecting parameters or starting the payment flow, and show payment details before Alipay confirmation. <br>
Risk: Image prompts are sent in plaintext to Juhe for generation. <br>
Mitigation: Warn users not to include personal, sensitive, or confidential information in prompts before request submission. <br>
Risk: Successful use depends on Alipay authentication and payment skills being installed and enabled. <br>
Mitigation: Check the required Alipay skills before use and stop with setup guidance when they are missing or disabled. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-ai-image-generate-a2a) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Files] <br>
**Output Format:** [Markdown workflow guidance with a JSON request body, shell command example, payment handoff instructions, and generated image file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a prompt up to 800 characters and an optional size value from 1 to 5; paid requests are completed through Alipay before the final image is available.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
