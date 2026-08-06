## Description:

Guides agents through briefing, HTML slide generation, validation, preview, and conversion into PowerPoint files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cqcmj74](https://clawhub.ai/user/cqcmj74)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to turn presentation requests into validated HTML slide decks and editable PowerPoint outputs. It is suited for workflows that need guided presentation planning, reusable slide assets, local validation, and PPTX conversion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates local slide files, preview images, caches, and PPTX output in the active workspace.

Mitigation: Use it only in a workspace where those outputs are expected, and review generated files before sharing or committing them.

Risk: First-time setup may download third-party npm packages and Playwright Chromium.

Mitigation: Run setup only in approved environments, and review or pin dependencies when organizational policy requires it.

Risk: Remote or untrusted image and media URLs can introduce network exposure or unreliable external dependencies.

Mitigation: Prefer vetted local assets for private decks and use remote media only when the source is approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cqcmj74/skills/html-slides-to-pptx)
- [HTML Conversion Specification](reference/html-spec.md)
- [Design Principles](reference/design-principles.md)
- [Interview Guide](reference/interview-guide.md)
- [Behavior Baseline](reference/behavior-baseline.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance plus HTML, CSS, JSON, shell commands, preview assets, and PPTX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires node and npm; optional setup may install Playwright Chromium; writes slide directories, previews, caches, and PPTX output in the workspace.]

## Skill Version(s):

2.0.0 (source: SKILL.md frontmatter, scripts/package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
