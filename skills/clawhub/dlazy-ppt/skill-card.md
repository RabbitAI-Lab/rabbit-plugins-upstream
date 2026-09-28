## Description:

Generates visually unified image-based PowerPoint decks from articles, reports, papers, notes, or outlines using dLazy for slide images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and business users turn written source material into visually consistent presentations with speaker notes. Slides are full-page images rather than separately editable elements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slide prompts and attached source images are sent to dLazy.

Mitigation: Do not submit confidential documents or images unless the upload is approved by your organization.

Risk: The dLazy API key is configured in a shared local runtime.

Mitigation: Protect access to the local runtime and API key; rotate the key if it is exposed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Project homepage (declared in skill metadata; source provenance unavailable)](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown progress and delivery report with paths to an image-based PPTX, slide images, outline, and speaker notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and Python dependencies; each slide is a full-slide image.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; skill frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
