## Description: <br>
Generate AI videos via Pixmind API (text-to-video and image-to-video). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fuyunzhishang](https://clawhub.ai/user/fuyunzhishang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate text-to-video or image-to-video clips through Pixmind, then poll generation tasks for video and cover URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video prompts, generation settings, and reference image URLs are sent to Pixmind. <br>
Mitigation: Avoid submitting sensitive or private content unless Pixmind's terms and retention practices are acceptable for the intended use. <br>
Risk: Invalid model, duration, aspect-ratio, or resolution combinations can fail generation requests. <br>
Mitigation: Use the validated model table and documented constraints before sending requests, especially Seedance resolution, Veo aspect ratios, and Sora duration values. <br>


## Reference(s): <br>
- [ClawHub Pixmind Video listing](https://clawhub.ai/fuyunzhishang/skills/pixmind-video) <br>
- [Pixmind homepage](https://www.pixmind.io) <br>
- [Pixmind API keys](https://www.pixmind.io/api-keys) <br>
- [Pixmind video generation endpoint](https://aihub-admin.aimix.pro/open-api/v1/video/generate) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, API calls, guidance] <br>
**Output Format:** [Markdown with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns task IDs and generated video or cover URLs when Pixmind tasks complete; requires PIXMIND_API_KEY.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
