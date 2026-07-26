## Description: <br>
Use when someone wants to swap a person, outfit, or product inside existing footage while keeping the camera move and audio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use this skill to prepare Pruna video replacement requests that swap people, clothing, or products in source footage while preserving camera motion, audio, and unrequested scene elements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Source videos, reference images, prompts, and generated file URLs are sent to Pruna's external API. <br>
Mitigation: Use the skill only with media that may be shared with Pruna and review Pruna's retention and deletion terms before processing sensitive footage. <br>
Risk: Video replacement can involve identity, likeness, clothing, product, or other consent-sensitive media changes. <br>
Mitigation: Confirm rights and consent for the source video and all reference images before making replacement requests. <br>
Risk: The optional disable_safety_checker field may reduce automated safety controls. <br>
Mitigation: Leave safety checks enabled unless a reviewed policy exception applies. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-replace) <br>
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files) <br>
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with curl commands, JSON request bodies, and prompt guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides the agent to collect a source video URL, one to four reference image URLs, replacement intent, optional resolution and frame-rate settings, and an instruction prompt before calling Pruna.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
