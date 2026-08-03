## Description: <br>
Use when someone wants to swap a person, outfit, or product inside existing footage while keeping the camera move and audio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative production agents use this skill to prepare Pruna API requests that replace a person, outfit, or product in an existing video while preserving the source scene, camera motion, and audio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User videos, reference images, and replacement instructions are uploaded to Pruna's external API. <br>
Mitigation: Use only media appropriate for external processing and avoid submitting sensitive content unless the user accepts that data flow. <br>
Risk: Video replacement can process identifiable people, outfits, or products. <br>
Mitigation: Use media the user has rights and consent to process, and confirm the requested swap before making a paid API call. <br>
Risk: The workflow requires a PRUNA_API_KEY. <br>
Mitigation: Keep the API key private, pass it through environment variables, and do not paste it into prompts, logs, or generated artifacts. <br>
Risk: The skill exposes a disable_safety_checker option. <br>
Mitigation: Leave safety checks enabled unless there is a clear, policy-compliant reason to disable them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/pruna-ai/skills/p-video-replace) <br>
- [Pruna Files API](https://api.pruna.ai/v1/files) <br>
- [Pruna Predictions API](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown with inline curl commands and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRUNA_API_KEY and user-provided source video plus 1 to 4 reference image URLs.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
