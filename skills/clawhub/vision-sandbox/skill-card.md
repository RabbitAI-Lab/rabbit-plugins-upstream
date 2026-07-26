## Description: <br>
Agentic Vision via Gemini's native Code Execution sandbox. Use for spatial grounding, visual math, and UI auditing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johanesalxd](https://clawhub.ai/user/johanesalxd) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use Vision Sandbox to send selected images and prompts to Gemini for spatial grounding, visual calculations, and UI auditing. The results can guide automated coding workflows that need coordinates, layout checks, or CSS/HTML fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected images, screenshots, prompts, and resulting analysis are sent to Google Gemini under the user's API key. <br>
Mitigation: Use the skill only when the relevant data-handling policy allows that transfer; avoid confidential screenshots, credentials, personal data, and customer information unless approved. <br>
Risk: Model responses may suggest code, CSS, or HTML changes based on visual analysis. <br>
Mitigation: Review suggested changes before applying them to a project. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/johanesalxd/skills/vision-sandbox) <br>
- [Publisher Profile](https://clawhub.ai/user/johanesalxd) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, files, guidance] <br>
**Output Format:** [Markdown and console text with fenced Python code, sandbox output, model responses, and optional generated image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires uv and GEMINI_API_KEY; default model is gemini-3-flash-preview.] <br>

## Skill Version(s): <br>
1.1.0 (source: release metadata and SKILL.md frontmatter; pyproject.toml reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
