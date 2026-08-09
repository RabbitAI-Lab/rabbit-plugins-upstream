## Description:

Generate Xiaohongshu-style vertical image notes for knowledge cards, infographic-style posts, 干货图文, or multi-image posts with matching caption text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kpdmiao](https://clawhub.ai/user/kpdmiao)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and knowledge workers use this skill to turn source material into Xiaohongshu-ready 3:4 image-note posts with concise page-by-page points and publishable captions. It is intended for social image notes, not PPT decks, courseware, or instructor slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The renderer creates local files under an export directory.

Mitigation: Run it in an intended working directory and review the generated output location before sharing or publishing files.

Risk: Generated image notes may have layout overflow, visual defects, or text placement issues.

Mitigation: Inspect the rendered images before posting and adjust the HTML content or theme if any page is crowded or misaligned.

Risk: The skill is scoped to Xiaohongshu image notes and may be misapplied to PPT decks, courseware, or instructor slides.

Mitigation: Use a separate presentation workflow when the requested deliverable is a deck, course material, or instructor-facing slide output.

## Reference(s):

- [Xiaohongshu Copywriting Guide](artifact/references/copywriting.md)
- [ClawHub Skill Page](https://clawhub.ai/kpdmiao/skills/xiaohongshu-note)

## Skill Output:

**Output Type(s):** [Files, Markdown, Code, Shell commands, Guidance]

**Output Format:** [PNG image files plus Markdown or plain-text caption content and rendering instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 3:4 vertical PNG images at 1080x1440 @2x and ready-to-post title, body, and hashtag copy; rendering requires Node.js, Playwright, and Chromium.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
