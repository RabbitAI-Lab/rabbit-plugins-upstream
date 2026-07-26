## Description: <br>
Free image and video generation via the Agnes AI API, including text-to-image, image-to-image, text-to-video, and image-to-video workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[start-ten](https://clawhub.ai/user/start-ten) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to call Agnes AI for image and video generation tasks from text prompts or source media. It provides setup guidance and curl examples for creating image generations, video tasks, and polling video results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, images, videos, and related metadata are sent to Agnes AI. <br>
Mitigation: Use the skill only for data that is appropriate to share with Agnes AI, and review the provider's privacy and retention terms before submitting sensitive or regulated content. <br>
Risk: The skill requires an AGNES_API_KEY for authenticated API calls. <br>
Mitigation: Store the key in the environment, avoid embedding it in prompts or committed files, and rotate it if it may have been exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/start-ten/skills/agnes-ai) <br>
- [Agnes AI API documentation](https://agnes-ai.com/doc) <br>
- [Agnes AI platform](https://platform.agnes-ai.com) <br>
- [Agnes AI homepage](https://agnes-ai.com) <br>
- [Agnes AI Hermes plugins GitHub repository](https://github.com/Start-Ten/agnes-ai-hermes-plugins) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AGNES_API_KEY and sends prompts or media to the Agnes AI API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
