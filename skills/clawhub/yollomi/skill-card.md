## Description: <br>
An AI image and video generator skill for OpenClaw that supports text-to-image, image-to-image, text-to-video, and image-to-video workflows through the Yollomi API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anichikage](https://clawhub.ai/user/anichikage) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent to generate or edit images and videos with Yollomi-supported models, list available models, and route generation requests through a unified API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, image URLs, and image or video inputs are sent to Yollomi or to the configured YOLLOMI_BASE_URL. <br>
Mitigation: Use approved content only, avoid sensitive inputs unless the destination is authorized, and keep YOLLOMI_BASE_URL pointed at a trusted host. <br>
Risk: YOLLOMI_API_KEY is required for generation requests. <br>
Mitigation: Store the key as a private environment variable or secret and do not commit it to skill files, prompts, logs, or shared configuration. <br>
Risk: Large image batches or video generations may consume meaningful model credits. <br>
Mitigation: Check model costs with yollomi.listModels or the model reference and start with small requests before running larger jobs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/anichikage/skills/yollomi) <br>
- [Publisher Profile](https://clawhub.ai/user/anichikage) <br>
- [Yollomi API Host](https://yollomi.com) <br>
- [Models Reference](artifact/models-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, API calls, Guidance] <br>
**Output Format:** [JSON API responses with image URLs, video URLs, model lists, and remaining-credit metadata, usually summarized for the agent as text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires YOLLOMI_API_KEY for generation; YOLLOMI_BASE_URL can override the default Yollomi host.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
