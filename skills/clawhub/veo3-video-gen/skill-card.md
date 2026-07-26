## Description: <br>
Generate and stitch short videos via Google Veo 3.x using the Gemini API (google-genai). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluelyw](https://clawhub.ai/user/bluelyw) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, creators, and marketing teams use this skill to generate short MP4 clips from text prompts and optionally stitch multiple Veo segments for longer ads, UGC-style clips, or product demos. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, segment prompts, base-style text, and optional reference or last-frame images are sent to Google Gemini/Veo. <br>
Mitigation: Use this skill only with content approved for Google Gemini/Veo processing and avoid submitting sensitive prompts or images. <br>
Risk: Gemini API usage can consume quota or incur billing, especially when generating multiple segments. <br>
Mitigation: Use a restricted Gemini API key, monitor quota and billing, and keep segment counts aligned with the intended output length. <br>
Risk: The configured output filename can overwrite existing files. <br>
Mitigation: Choose output paths deliberately and avoid reusing filenames for assets that must be preserved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bluelyw/skills/veo3-video-gen) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with shell command examples and generated MP4 media files from the bundled script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Gemini API key; optional reference images, segment prompts, last-frame continuity, and ffmpeg-based stitching can affect generated output.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
