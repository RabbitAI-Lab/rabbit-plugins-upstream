## Description: <br>
A lightweight Grok Imagine automation skill for generating one image from a natural-language prompt and saving it locally through browser and desktop automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to automate single-image generation in Grok Imagine for personal creative images, social media visuals, and quick concept validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may cause the skill to run for unrelated automation requests. <br>
Mitigation: Invoke it only for explicit Grok image-generation and local-save tasks, and review the planned browser and desktop actions before execution. <br>
Risk: Desktop-control steps may interact with the wrong page, window, menu, or save location. <br>
Mitigation: Keep the browser focused on the intended Grok Imagine page, confirm the visible target before clicks or keyboard actions, and verify the saved file path afterward. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/grok-image-tool-free) <br>
- [Grok Imagine](https://grok.com/imagine) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown instructions with inline code examples and JSON-style status output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May control a browser and desktop session and save generated image files locally, typically under ~/Downloads/.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
