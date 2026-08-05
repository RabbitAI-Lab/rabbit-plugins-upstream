## Description: <br>
Converts Markdown or plain text into high-resolution long-form images, share cards, and posters using local HTML rendering and 18 built-in visual styles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to turn local Markdown or plain-text content into polished PNG images for reports, posters, social sharing, and visual summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install puppeteer-core and launch local Chrome to render HTML into PNG files. <br>
Mitigation: Use the disclosed setup path, pin dependencies in controlled environments, and review generated HTML and output paths before rendering. <br>
Risk: Some visual styles load Google Fonts, which may make outbound font requests during rendering. <br>
Mitigation: Vendor fonts or disable remote font links in restricted environments; the artifact includes system-font fallbacks. <br>
Risk: Chrome is launched with certificate checks disabled for the rendering session. <br>
Mitigation: Keep rendering limited to local HTML files and remove the certificate-bypass flag once the local trust store is fixed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/text-to-elegant-image) <br>
- [README](README.md) <br>
- [Verification and rendering options](docs/VERIFICATION.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with HTML, CSS, shell commands, and local PNG file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local HTML and PNG image artifacts; supports long-image and fixed-height poster or cover layouts.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence and changelog, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
