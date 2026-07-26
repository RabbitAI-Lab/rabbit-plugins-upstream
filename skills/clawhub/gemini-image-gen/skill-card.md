## Description: <br>
Generate and edit images via Google Gemini API, including Gemini native generation, Imagen 3 generation, style presets, batch generation, and HTML gallery output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iisweetheartii](https://clawhub.ai/user/iisweetheartii) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and creative agents use this skill to generate, edit, and batch-produce images through Google's Gemini and Imagen services. It supports prompt-based image creation, image edits, style presets, and gallery files for reviewing generated outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected edit images are sent to Google's Gemini/Imagen service using the user's API key. <br>
Mitigation: Use only prompts and images approved for external processing; avoid confidential or sensitive material. <br>
Risk: Heartbeat guidance suggests optional social posting, avatar changes, and memory saving. <br>
Mitigation: Require explicit approval for the destination, content, account, and retention rules before posting, changing avatars, or saving outputs. <br>
Risk: The --edit option reads a local image path and sends that image for remote processing. <br>
Mitigation: Pass only intended image files to --edit and avoid confidential files or non-image paths. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iisweetheartii/skills/gemini-image-gen) <br>
- [Google AI Studio API key setup](https://aistudio.google.com/apikey) <br>
- [Gemini API endpoint used by the skill](https://generativelanguage.googleapis.com/v1beta) <br>
- [OpenClaw](https://openclaw.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated image files, prompts.json, and an HTML gallery when the script is run.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and GEMINI_API_KEY; sends prompts and selected edit images to Google's Gemini/Imagen service.] <br>

## Skill Version(s): <br>
1.3.1 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
