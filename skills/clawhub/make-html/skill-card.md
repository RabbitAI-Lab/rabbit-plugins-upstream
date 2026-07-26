## Description: <br>
Make Html guides agents to produce substantial deliverables as self-contained, validated HTML artifacts with purposeful layout, visual hierarchy, interaction, and optional hosted sharing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fuller-stack-dev](https://clawhub.ai/user/fuller-stack-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and technical writers use this skill to turn plans, reviews, reports, diagrams, dashboards, decks, prototypes, and editors into readable browser-native artifacts instead of long Markdown responses. It is intended for substantial human-facing deliverables that benefit from structure, styling, validation, or sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional hosted sharing path uploads a finished HTML artifact to an unlisted GitHub Gist that anyone with the link can view. <br>
Mitigation: Publish only after the user asks for or confirms hosted sharing, and review the artifact for secrets, credentials, customer data, personal data, internal material, hidden metadata, and source excerpts before upload. <br>


## Reference(s): <br>
- [Make HTML skill definition](SKILL.md) <br>
- [Recognition](references/recognition.md) <br>
- [Artifact Patterns](references/artifact-patterns.md) <br>
- [Interaction Patterns](references/interaction-patterns.md) <br>
- [Visual Quality](references/visual-quality.md) <br>
- [Validation](references/validation.md) <br>
- [Sharing HTML Artifacts](references/sharing.md) <br>
- [Source Style](references/source-style.md) <br>
- [Custom Themes](references/custom-themes.md) <br>
- [Example Layout Catalog](references/example-layout-catalog.md) <br>
- [Pagedrop](https://pagedrop.ai) <br>
- [Pagedrop GitHub repository](https://github.com/Martian-Engineering/pagedrop) <br>


## Skill Output: <br>
**Output Type(s):** [code, shell commands, guidance] <br>
**Output Format:** [Self-contained HTML files with inline CSS and optional JavaScript, plus brief Markdown status messages or hosted-share URLs when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Artifacts are designed for offline local use by default; hosted sharing is optional and uses an authenticated GitHub CLI to create an unlisted Gist only after user approval.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
