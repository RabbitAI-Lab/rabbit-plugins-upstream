## Description: <br>
Converts Figma designs into project-aware mobile UI code for Android, iOS, and Flutter by fetching design data, optionally scanning local project resources, and supporting iterative feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[timeaground](https://clawhub.ai/user/timeaground) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to turn selected Figma frames into mobile layout code for Jetpack Compose, Android XML, SwiftUI, UIKit, or Flutter while reusing project resources when scan access is approved. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Figma personal access token through FIGMA_TOKEN. <br>
Mitigation: Set the token as an environment variable, do not paste it into chat, and rotate or revoke it if exposure is suspected. <br>
Risk: Project scanning reads local project files to reuse colors, strings, images, and components. <br>
Mitigation: Approve scans only for intended project directories and review generated scan reports as local project data. <br>
Risk: Generated UI code and feedback logs may be written into the project. <br>
Mitigation: Review generated files and feedback-log.md before committing or sharing them. <br>
Risk: SVG export may download from Figma-provided asset URLs in addition to api.figma.com. <br>
Mitigation: Allow network access only when needed for the conversion task and review downloaded assets before use. <br>


## Reference(s): <br>
- [figma-to-mobile on ClawHub](https://clawhub.ai/timeaground/skills/figma-to-mobile) <br>
- [Publisher profile](https://clawhub.ai/user/timeaground) <br>
- [Issue tracker](https://github.com/TimeAground/figma-to-mobile/issues) <br>
- [Figma interpretation rules](references/figma-interpretation.md) <br>
- [Generation rules](references/generation-rules.md) <br>
- [Project scan usage](references/scan-usage.md) <br>
- [Jetpack Compose patterns](references/compose-patterns.md) <br>
- [Android XML patterns](references/xml-patterns.md) <br>
- [SwiftUI patterns](references/swiftui-patterns.md) <br>
- [UIKit patterns](references/uikit-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with generated mobile code blocks, file names, shell commands, and concise guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce project scan reports, generated UI code files, and feedback-log.md when the user approves the related local actions.] <br>

## Skill Version(s): <br>
2.2.5 (source: server-resolved ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
