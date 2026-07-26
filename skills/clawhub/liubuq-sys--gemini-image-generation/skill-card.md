## Description: <br>
Generate or edit images with Gemini using the Google GenAI SDK for OpenClaw skill workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liubuq-sys](https://clawhub.ai/user/liubuq-sys) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to generate new images from text prompts or edit workspace images with Gemini, then save the resulting image files for use in agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected source images are sent to the configured Gemini or custom endpoint. <br>
Mitigation: Use only approved providers and avoid confidential, regulated, or private images unless that provider use is approved. <br>
Risk: Generated images are written to workspace output paths. <br>
Mitigation: Choose explicit output paths to reduce the chance of unwanted file overwrites. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liubuq-sys/skills/gemini-image-generation) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Shell commands, Configuration] <br>
**Output Format:** [Saved image files with TEXT, IMAGE, MEDIA, and JSON summary lines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GEMINI_API_KEY and GEMINI_MODEL_ID; optional GEMINI_BASE_URL, aspect ratio, image size, source images, and output path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
