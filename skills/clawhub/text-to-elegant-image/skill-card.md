## Description: <br>
Turns Markdown or plain text into self-contained HTML and renders high-resolution PNG long images, share posters, or cover cards with built-in visual styles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI-agent users use this skill to convert Markdown or plain text into polished local PNG share images, long cards, posters, and covers. The skill helps agents choose among 18 visual styles, generate HTML/CSS, check for emoji rendering issues, and export the final image with headless Chrome. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup workflow may run npm install in the skill directory. <br>
Mitigation: Review setup.sh and package.json before use; install dependencies in a controlled environment and pin puppeteer-core if required. <br>
Risk: The renderer accepts HTTP(S) inputs and can browse arbitrary URLs with headless Chrome. <br>
Mitigation: Restrict export_image.js to local HTML files unless remote URL screenshots are intentionally needed, and apply normal network controls for the execution environment. <br>
Risk: Generated HTML may load public web fonts during rendering. <br>
Mitigation: Use system-font fallbacks or allowlist intended font domains when rendering sensitive content. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/songhonglei/skills/text-to-elegant-image) <br>
- [README](README.md) <br>
- [Skill Workflow](SKILL.md) <br>
- [Changelog](CHANGELOG.md) <br>
- [Base Style Reference](resources/styles/_BASE.md) <br>
- [Visualization Components](resources/components.css) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with HTML/CSS/JavaScript snippets, shell commands, and local PNG file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create temporary HTML files and local PNG outputs; uses headless Chrome for rendering.] <br>

## Skill Version(s): <br>
1.2.0 (source: package.json, CHANGELOG, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
