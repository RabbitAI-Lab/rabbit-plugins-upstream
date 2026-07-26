## Description: <br>
Use the Gemini API for Nano Banana image generation, Veo video workflows, Gemini TTS speech generation, and image, video, and audio understanding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xsir0](https://clawhub.ai/user/xsir0) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to choose Gemini media capabilities and adapt Node.js or REST templates for multimodal generation, understanding, transcription, and narration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected media may be sent to Google services, including meeting recordings or regulated data. <br>
Mitigation: Confirm rights and policy approval before upload, and avoid sending regulated or sensitive media unless the deployment is authorized for that data. <br>
Risk: The skill uses GEMINI_API_KEY for API access. <br>
Mitigation: Store GEMINI_API_KEY outside source control, rotate it if exposed, and monitor quota and billing impact. <br>
Risk: Example commands write fixed local output filenames such as out.png and out.mp4. <br>
Mitigation: Change output paths or add overwrite checks when existing local files must be preserved. <br>
Risk: Generated media and API limits may require operational controls such as retries, timeouts, and review. <br>
Mitigation: Use timeouts, backoff, failure fallbacks, prompt and output review, and prompt updates when model names or limits change. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xsir0/skills/google-gemini-media) <br>
- [Gemini generateContent API endpoint used by examples](https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Node.js, REST, and shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes model-selection guidance, media input and output handling patterns, polling examples, and environment variable setup for GEMINI_API_KEY.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
