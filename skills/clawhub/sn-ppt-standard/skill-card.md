## Description:

Standard and fast PPT pipeline for generating polished presentations through staged planning, style selection, asset generation, HTML slide creation, and PPTX or PDF export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and presentation-building agents use this skill to turn a deck request and prepared task metadata into a complete presentation workflow with research-aware standard mode or rapid draft fast mode. It produces slide content, visual assets, HTML pages, and a user-selected PPTX or PDF deliverable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses local API keys and configurable model or gateway endpoints.

Mitigation: Use trusted endpoint configuration, keep gateway keys narrowly scoped, and rotate keys if the skill was run with an untrusted configured gateway URL.

Risk: Generated slide HTML or source documents can influence image URLs that are fetched during export.

Mitigation: Run in a constrained workspace, avoid untrusted slide HTML or source documents, and review image sources before export.

Risk: The export path can install npm and Playwright/Chromium dependencies at runtime.

Mitigation: Prefer preinstalled and audited export dependencies, or review dependency installation before execution.

Risk: A local workbench server may expose previews or companion interactions.

Mitigation: Bind the workbench to localhost or trusted forwarded URLs and avoid exposing API keys or gateway configuration to untrusted users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-ppt-standard)
- [HTML generation constraints](artifact/references/html_constraints.md)
- [Style catalog](artifact/references/style_catalog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated presentation files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces staged JSON artifacts, HTML slide pages, image assets, and a final PPTX or PDF when export dependencies are available.]

## Skill Version(s):

2026.9.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
