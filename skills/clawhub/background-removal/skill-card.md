## Description: <br>
Remove backgrounds from images with BiRefNet via the inference.sh CLI for product photos, portraits, e-commerce assets, transparent PNGs, and photo editing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, designers, marketers, and e-commerce operators use this skill to run inference.sh image tools for background removal, transparent PNG cutouts, and related image editing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The quick start pipes the inference.sh installer directly to sh. <br>
Mitigation: Inspect the install script or use the documented manual install and checksum verification path before installing. <br>
Risk: Some examples extend beyond background removal into image generation or background replacement. <br>
Mitigation: Use the skill only for user-directed image work and review prompts before running image generation or editing commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/okaris/skills/background-removal) <br>
- [inference.sh](https://inference.sh) <br>
- [Running Apps](https://inference.sh/docs/apps/running) <br>
- [Image Generation Example](https://inference.sh/docs/examples/image-generation) <br>
- [Apps Overview](https://inference.sh/docs/apps/overview) <br>
- [inference.sh CLI checksums](https://dist.inference.sh/cli/checksums.txt) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance, configuration] <br>
**Output Format:** [Markdown with bash commands and JSON CLI inputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The referenced inference.sh app output is a PNG with a transparent background.] <br>

## Skill Version(s): <br>
0.1.5 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
