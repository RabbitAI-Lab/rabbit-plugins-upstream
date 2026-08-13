## Description:

Converts Figma design links into mobile UI code for Compose, Android XML, SwiftUI, UIKit, and Flutter using the Figma REST API, optional project resource scanning, multi-frame comparison, and feedback-log corrections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[timeaground](https://clawhub.ai/user/timeaground)

### License/Terms of Use:

MIT

## Use Case:

Developers and mobile engineers use this skill to turn selected Figma frames into platform-idiomatic mobile UI code while reusing project resources when a local scan is approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Figma personal access token through the FIGMA_TOKEN environment variable.

Mitigation: Set the token as an environment variable, do not paste it into chat, and rotate it if it is exposed.

Risk: Approved project scans read local mobile project files to find colors, strings, images, and components.

Mitigation: Review the scan path before approving a scan and inspect generated scan-report.json before sharing it.

Risk: Feedback logging may store before-and-after snippets that contain sensitive product details.

Mitigation: Create feedback-log.md only after consent and avoid logging sensitive snippets unless local storage is acceptable.

Risk: Generated UI code may not exactly match design intent or project conventions.

Mitigation: Review, test, and adapt generated files in the target Android, iOS, or Flutter project before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/timeaground/skills/figma-to-mobile)
- [Publisher profile](https://clawhub.ai/user/timeaground)
- [Figma REST API endpoint](https://api.figma.com)
- [Figma community demo design](https://www.figma.com/community/file/1169726503071187057/)
- [Figma node interpretation rules](references/figma-interpretation.md)
- [Code generation rules](references/generation-rules.md)
- [Project scan usage guide](references/scan-usage.md)
- [Error handling](references/error-handling.md)
- [Feedback log format](references/feedback-log.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown conversation output with generated mobile source code files, shell command snippets, JSON scan reports, and setup guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce scan-report.json after approved project scanning and feedback-log.md after user consent.]

## Skill Version(s):

2.3.0 (source: SKILL.md frontmatter, CHANGELOG, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
