## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ningzimu](https://clawhub.ai/user/ningzimu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, educators, and business users use this skill to turn source material into visually consistent image-based presentation decks when editable slide objects are not required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CLI/API fallback can mishandle credentials.

Mitigation: Prefer the built-in image backend when available; when fallback is needed, use a dedicated low-privilege API key and avoid passing real keys directly in command lines.

Risk: AtlasCloud or untrusted compatible endpoints may be unsafe until polling URL validation is fixed.

Mitigation: Avoid AtlasCloud and untrusted compatible endpoints, or restrict use to endpoints that have been reviewed and approved.

Risk: The shared runtime has broad, persistent dependency behavior under ~/.codex-ppt-skill.

Mitigation: Run the skill in an isolated workspace and review or clean persistent runtime files as part of deployment hygiene.

## Reference(s):

- [Codex PPT ClawHub listing](https://clawhub.ai/ningzimu/skills/codex-ppt)
- [Codex PPT homepage](https://github.com/ningzimu/codex-ppt-skill)
- [Backend selection](docs/backend-selection.md)
- [Workflow gates and progress](docs/workflow-gates-and-progress.md)
- [Slide generation and subagents](docs/slide-generation-and-subagents.md)
- [Project assembly and reporting](docs/project-assembly-and-reporting.md)
- [User-supplied assets](docs/user-supplied-assets.md)
- [Style library](docs/style-library.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, JSON state files, shell commands, generated slide images, and PPTX deck output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final decks are image-based; individual text boxes, charts, and shapes are not separately editable.]

## Skill Version(s):

0.6.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
