## Description: <br>
Create Gemini Omni voice resources, character resources, and Flash Preview or multimodal text-to-video tasks through RunAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create or manage Gemini Omni audio voices, character resources, and video generation tasks through RunAPI. It guides one-off CLI use and SDK-based application integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, uploaded inputs, and generated assets may be sent to an external RunAPI provider. <br>
Mitigation: Use this skill only for intended RunAPI Gemini Omni work and review data handling requirements before sending sensitive content. <br>
Risk: RUNAPI_API_KEY or saved CLI authentication could be exposed or stored in an unsafe location. <br>
Mitigation: Prefer environment-managed credentials or vetted saved CLI config, and review local credential storage before use. <br>
Risk: RunAPI-generated file URLs are temporary and may expire before downstream systems retrieve them. <br>
Mitigation: Download generated media and store it in durable storage within the documented seven-day window. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-gemini-omni) <br>
- [RunAPI Gemini Omni Homepage](https://runapi.ai/models/gemini-omni) <br>
- [RunAPI Gemini Omni Documentation](https://runapi.ai/models/gemini-omni.md) <br>
- [Gemini Omni Flash Preview](https://runapi.ai/models/gemini-omni/flash-preview.md) <br>
- [RunAPI Google Provider](https://runapi.ai/providers/google.md) <br>
- [RunAPI Model Catalog](https://runapi.ai/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with shell and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to generate or manage audio, character, image, video, and related media assets through RunAPI.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
