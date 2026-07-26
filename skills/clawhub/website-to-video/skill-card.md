## Description: <br>
Capture a general website/URL and turn it into a video of the site, such as a tour, showcase, or social clip built from captured screenshots and the site's own brand assets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content teams use this skill to capture a public website, extract brand context, plan a storyboard, generate narration or music choices, build HyperFrames compositions, and validate a previewable website-derived video. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill instructs agents to run a silent self-update before use. <br>
Mitigation: Review the update step before execution and decline or pin updates unless the source and change are trusted. <br>
Risk: The skill may ask users to provide API keys through chat or local project configuration. <br>
Mitigation: Use a safer secret mechanism such as environment-managed credentials and avoid pasting secrets into chat. <br>
Risk: Website capture can save screenshots, assets, and extracted design data locally. <br>
Mitigation: Avoid authenticated or sensitive websites unless the saved capture outputs are expected, controlled, and reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/website-to-video) <br>
- [Step 0 Capture](references/step-0-capture.md) <br>
- [Step 1 Design](references/step-1-design.md) <br>
- [Step 2 Brief](references/step-2-brief.md) <br>
- [Step 3 Storyboard](references/step-3-storyboard.md) <br>
- [Step 4 VO](references/step-4-vo.md) <br>
- [Step 5 Build](references/step-5-build.md) <br>
- [Step 6 Validate](references/step-6-validate.md) <br>
- [HyperFrames capabilities](references/capabilities.md) <br>
- [Beat Builder Guide](references/beat-builder-guide.md) <br>
- [SFX Credits](assets/sfx/CREDITS.md) <br>
- [Pixabay sound effects](https://pixabay.com/sound-effects/) <br>
- [Pixabay Content License](https://pixabay.com/service/license-summary/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces staged planning and validation artifacts for a HyperFrames website video workflow.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
