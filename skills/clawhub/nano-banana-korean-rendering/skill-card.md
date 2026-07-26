## Description: <br>
Generates AI images with accurately pre-rendered non-Latin text, including Korean, Japanese, Chinese, Thai, and other scripts, by combining Canvas text rendering with Gemini image generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wonyoung-huh](https://clawhub.ai/user/wonyoung-huh) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creators use this skill to detect non-Latin text in image prompts, extract text and styling, pre-render that text to PNG with Canvas, and pass the result to Gemini for final image generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup installs npm dependencies and may download font files from external sources. <br>
Mitigation: Review the dependency list and run setup in an environment appropriate for external package and font downloads. <br>
Risk: Gemini analysis and image generation can send prompts plus selected rendered or reference images to Google's Gemini service. <br>
Mitigation: Use a limited Gemini API key and avoid sensitive text or private images unless those uploads are intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wonyoung-huh/skills/nano-banana-korean-rendering) <br>
- [Google Fonts Noto](https://fonts.google.com/noto) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance] <br>
**Output Format:** [Markdown instructions with shell command examples; CLI commands emit JSON status data and PNG image files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GEMINI_API_KEY for Gemini analysis and image generation; Canvas-only rendering can produce local PNG output without image generation.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release evidence; artifact package.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
