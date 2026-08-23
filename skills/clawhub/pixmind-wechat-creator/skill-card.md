## Description:

Creates, reviews, illustrates, and formats WeChat Official Account articles through Pixmind's content engine for rich-text copy into the WeChat editor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fuyunzhishang](https://clawhub.ai/user/fuyunzhishang)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and marketing teams use this skill to plan, generate, review, illustrate, and format WeChat Official Account articles. The final deliverable is WeChat-compatible rich text for copying into the official editor, not automated publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Article briefs, source URLs, and provided materials are sent to Pixmind's content service.

Mitigation: Install and use the skill only when that data transfer is acceptable, and avoid submitting confidential material unless Pixmind handling is approved.

Risk: Outline, article, review, and optional image generation can spend Pixmind API credits.

Mitigation: Obtain explicit user approval before paid generation and query existing project state before retrying after interruption or timeout.

Risk: Generated or reviewed article content may still be inaccurate, misleading, or unsuitable for publication.

Mitigation: Review and fact-check the rendered article before copying it into the WeChat editor.

Risk: Users may assume the skill publishes to WeChat or needs WeChat account credentials.

Mitigation: Keep completion to rendered rich-text copy; do not request WeChat AppID, AppSecret, account aliases, access tokens, or publication permissions.

## Reference(s):

- [Public safety rules](references/public-safety-rules.md)
- [Public tool contracts](references/public-tool-contracts.md)
- [Article presentation](references/presentation-schema.md)
- [Pixmind WeChat Creator on ClawHub](https://clawhub.ai/fuyunzhishang/skills/pixmind-wechat-creator)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, API Calls, Guidance]

**Output Format:** [Structured article presentation with Markdown content, rendered HTML, review status, image metadata, and copy guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include project ID, revision, outline, digest, sources, theme, layout, cover URL, inline assets, and local copy.rich-text action metadata.]

## Skill Version(s):

0.3.6 (source: server release metadata and skill.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
