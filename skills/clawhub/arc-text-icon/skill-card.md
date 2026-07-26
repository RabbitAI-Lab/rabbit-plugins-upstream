## Description: <br>
Generate upper-arc Chinese text icons for packaging, seals, badges, banners, or outer labels with configurable text, font, color, stroke, curvature, size, and background. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[blizzard-bj](https://clawhub.ai/user/blizzard-bj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Designers, developers, and agent users use this skill to create curved text PNG assets for packaging labels, seals, badges, banners, and similar visual materials. It helps choose parameters, run a local renderer, and verify that the generated image is visible and correctly spaced. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes PNG files to paths supplied by the user. <br>
Mitigation: Keep output paths in normal project or downloads directories and review filenames before running the renderer. <br>
Risk: Geometry or parameter issues can produce blank, poorly spaced, or hard-to-see images. <br>
Mitigation: Use the bundled self-check diagnostics and inspect the white-background preview before delivering the image. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/blizzard-bj/skills/arc-text-icon) <br>
- [Parameter tuning guide](references/params.md) <br>
- [Available CJK fonts](assets/sample_fonts.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Files] <br>
**Output Format:** [Markdown guidance with bash commands and generated PNG files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The renderer writes a main PNG plus a white-background preview PNG and reports self-check diagnostics.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and artifact changelog, released 2026-07-14) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
