## Description:

Search Google Images with FlashData for image URLs, source pages, dimensions and titles. Use to find visual references, diagrams, product images or images that meet a size requirement. Requires a FlashData API key and paid Credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can search for visual references, diagrams, product images, or images that meet a size requirement, then use the returned image URLs, source pages, titles, and available dimensions to build an image inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the FlashData connection requires an API key and image queries use paid Credits; the security assessment reports medium confidence with partial reference-resolution coverage.

Mitigation: Keep FLASHDATA_API_KEY in protected secret configuration, and review query usage against an approved Credits budget.

## Reference(s):

- [FlashData Google Images documentation](https://flashdata.dev/docs/sources/google_images?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_images-task)
- [Get a FlashData API key](https://flashdata.dev/signup?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_images-task)
- [FlashData pricing](https://flashdata.dev/pricing?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_images-task)
- [FlashData MCP endpoint](https://flashdata.dev/mcp?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_images-task)
- [ClawHub release page](https://clawhub.ai/rocosen/skills/google-image-search-flashdata)

## Skill Output:

**Output Type(s):** [text, JSON, markdown]

**Output Format:** [Structured image search results with image URLs, source pages, titles and available dimensions; results can be presented as a Markdown table or list.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Result counts and available fields vary by query; dimensions may be missing. The skill returns URLs and metadata, not downloaded image files.]

## Skill Version(s):

1.0.2 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
