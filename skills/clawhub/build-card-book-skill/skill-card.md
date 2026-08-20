## Description:

Generates a single-file HTML flip-card toolbook from structured book or topic content JSON using bundled templates, a build script, a self-check script, and an optional prompt reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-acheng](https://clawhub.ai/user/ai-acheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content creators, and agents use this skill to convert a book or topic into a responsive, browser-openable card book with a cover, how-to page, index, themed cards, and back matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated pages load a default Unsplash cover image unless it is replaced or removed, which can disclose normal web request metadata to the image host.

Mitigation: Replace the default cover image with an approved local or hosted asset, or remove the remote image before publishing sensitive or private card books.

Risk: The footer template includes placeholder public-account and keyword call-to-action text that may be inappropriate for the final audience.

Mitigation: Review, replace, or delete the promotional footer block before release.

Risk: The card-book format can include book quotations or paraphrases that may be inaccurate if the input content is not reviewed.

Mitigation: Check quoted text and source attributions against authoritative editions before distributing the generated HTML.

## Reference(s):

- [Strict Prompt Reference](artifact/references/prompt.md)
- [ClawHub Skill Page](https://clawhub.ai/ai-acheng/skills/build-card-book-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated single-file HTML code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated HTML is intended to be opened locally in a browser and checked with the bundled validation script.]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
