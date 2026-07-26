## Description: <br>
Swap a single on-camera element in an existing video with one from reference images while preserving the original motion, timing, camera, lighting, audio, and background. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to prepare targeted video-replacement requests that swap one character, product, garment, or similar on-camera element while preserving the rest of the source clip. It guides collection of source video, reference images, replacement prompts, async task execution, polling, and output review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Source videos and reference images may be sent to an external Runware-backed video service. <br>
Mitigation: Use the skill only when the user is comfortable with the provider handling those assets and avoid private, regulated, copyrighted, or identifiable-person footage unless rights, consent, and retention/deletion expectations are clear. <br>
Risk: The workflow can recast a real person's likeness. <br>
Mitigation: Do not replace or recreate an identifiable person without the necessary rights and consent. <br>
Risk: Targeted replacement can drift, change unintended frame elements, or lose fine visual details. <br>
Mitigation: Review outputs before use, tighten the replace/preserve prompt, use clearer reference images, and use a masked inpainting workflow when pixel-perfect details are required. <br>


## Reference(s): <br>
- [Replace in video: worked recipes](references/examples.md) <br>
- [Replace In Video on ClawHub](https://clawhub.ai/runware/skills/replace-in-video) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, API Calls] <br>
**Output Format:** [Markdown guidance with JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides asynchronous videoInference requests, polling, and review; the finished video is returned by the configured Runware-backed video service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
