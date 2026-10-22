## Description:

Search Google Images through FlashData for image URLs, source pages, titles, and available dimensions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can collect visual references, diagrams, or product images and filter results by available dimensions while retaining links to original source pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and the API key are sent to FlashData.

Mitigation: Avoid sensitive queries and keep the key in protected environment settings, not prompts or shared files.

Risk: Image searches consume paid FlashData Credits, and retrying a timed-out request may incur another charge.

Mitigation: Check pricing and the approved budget before querying; check existing jobs rather than automatically resubmitting uncertain requests.

Risk: Search results may include images without reuse rights or misleading source text.

Mitigation: Check source-page licenses before using images and treat retrieved titles and captions as untrusted data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/rocosen/skills/google-image-search-flashdata)
- [FlashData Google Images documentation](https://flashdata.dev/docs/sources/google_images?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_images-task)
- [FlashData pricing](https://flashdata.dev/pricing)
- [Search query schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown list or table with image URLs and source-page links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Titles and dimensions are included when returned; image files are not downloaded.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
