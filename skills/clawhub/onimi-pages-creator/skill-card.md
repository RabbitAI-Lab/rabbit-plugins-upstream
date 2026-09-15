## Description:

Create polished standalone HTML pages for Onimi Pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mariohazy](https://clawhub.ai/user/mariohazy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to create polished self-contained HTML pages, including websites, reports, posters, dashboards, demos, and interactive artifacts. The skill keeps creation local and separates page creation from any later publishing workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing from a moving package tag can run a version that has not been reviewed.

Mitigation: Prefer the direct-download path with SHA-256 and size verification, or install an exact reviewed package version.

Risk: Optional update helpers can change local skill files after installation.

Mitigation: Review update notices first and run the manager update command only after explicitly approving the exact target version.

Risk: Users may confuse local page creation with publishing to Onimi Pages.

Mitigation: Keep creation and publishing separate; install the separate publishing skill only when publishing is actually desired.

Risk: Generated pages can include incorrect, invented, or unlabeled sample content.

Mitigation: Preserve user-provided facts, avoid invented claims, label simulations or sample metrics, and review the rendered page before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mariohazy/skills/onimi-pages-creator)
- [Install Onimi Pages Creator](references/installation.md)
- [Standalone page quality](references/page-quality.md)
- [Scenario playbook](references/scenario-playbook.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Self-contained HTML file with concise Markdown guidance and validation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated HTML is expected to embed CSS and JavaScript, avoid external dependencies unless explicitly requested, and pass the bundled standalone HTML validator.]

## Skill Version(s):

0.1.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
