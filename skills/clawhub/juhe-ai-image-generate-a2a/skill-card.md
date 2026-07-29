## Description: <br>
This skill helps agents request paid Juhe AI image generation from a text prompt, obtain payment through the Alipay A2M/HTTP 402 flow, and save generated images locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users ask an agent to generate images from text prompts in supported aspect ratios, while the agent discloses the paid Juhe service, obtains explicit consent, and hands payment confirmation to the Alipay skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User prompts are sent to Juhe for image generation. <br>
Mitigation: Tell users not to include private personal details in prompts before proceeding. <br>
Risk: The skill initiates a paid image-generation flow through Alipay-related skills. <br>
Mitigation: Require explicit user confirmation before collecting parameters or proceeding with payment. <br>
Risk: Generated image files may be saved locally. <br>
Mitigation: Make users aware that generated files can be stored on their device and should be handled according to their local data practices. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-ai-image-generate-a2a) <br>
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Files] <br>
**Output Format:** [Markdown/text guidance with JSON request payloads and generated image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a prompt of up to 800 characters, an optional size code from 1 to 5, explicit user payment consent, and Alipay payment-skill handoff for HTTP 402 responses.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
