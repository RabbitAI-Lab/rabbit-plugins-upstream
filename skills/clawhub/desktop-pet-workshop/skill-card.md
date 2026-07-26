## Description: <br>
Transforms uploaded photos into stylized interactive desktop pets with subject extraction, cute character adaptation, multiple animated actions, interaction rules, and platform-specific Electron installers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haixuma](https://clawhub.ai/user/haixuma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn a clear source photo into desktop pet assets, action documentation, interaction configuration, and a ready-to-install desktop application for Windows or macOS. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The build flow installs Electron dependencies from the network and packages an installable desktop application. <br>
Mitigation: Require explicit user confirmation before dependency installation or build execution, review and pin Electron dependencies, use a lockfile, and update the Electron runtime before release. <br>
Risk: Generated installers run local desktop application code and should not be treated as image-only output. <br>
Mitigation: Build in a controlled environment, inspect generated assets and configuration before packaging, and distribute only reviewed installer artifacts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haixuma/skills/desktop-pet-workshop) <br>
- [Project homepage](https://github.com/HaixuMa/desktop-pet-workshop) <br>
- [Default actions reference](references/default_actions.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance, JSON configuration, generated image assets, and Electron installer files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Windows .exe or macOS .dmg installers when the required local Node.js and platform build environment are available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
