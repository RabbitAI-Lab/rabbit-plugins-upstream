## Description:

Photo Scout helps agents search for topic-specific images, screen candidates with multimodal visual review, download selected originals, and verify source pages when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sedey999](https://clawhub.ai/user/sedey999)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and image-research users use this skill to find high-quality logos, people photos, product images, scenery, event images, and food photos. It is intended for workflows where a vision-capable agent can review screenshots or contact sheets before downloading selected images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to external image and search sites, and screenshots and downloaded images are saved locally.

Mitigation: Avoid sensitive queries, use a clear work directory, and clean up generated screenshots, candidates, and selected images after review.

Risk: The artifact includes behavior for fetching unwatermarked originals and bypassing publisher-side controls.

Mitigation: Use only licensed or authorized image sources, review source terms before reuse, and disable or avoid original-fetch behavior where rights are unclear.

Risk: A vision-capable agent may still select irrelevant, outdated, or rights-sensitive images.

Mitigation: Manually review selected outputs and use the source-page verification workflow for events, brands, people, and other high-context image requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sedey999/skills/photo-scout)
- [Visual Scoring Rules](references/scoring.md)
- [Source Selection Guidance](references/sources.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands and generated image, JSON, screenshot, and XLSX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces candidate metadata, contact sheets, selected image files, source verification screenshots, and reports under the chosen work directory.]

## Skill Version(s):

4.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
