## Description:

Searches the Zhihuiya patent database for visually similar design patents from a public image URL, with filters for country, Locarno class, legal status, dates, assignee, and pagination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to compare a product or design image against design patent records and review visually similar patents for prior-art or appearance-risk assessment. It can upload local images to obtain a temporary public URL, then call the LinkFox/Zhihuiya patent image search API and summarize or persist the JSON results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and patent-search parameters are sent to LinkFox/Zhihuiya services.

Mitigation: Use the skill only when the image and search terms are approved for those external services, and avoid submitting confidential or restricted product images.

Risk: Local image upload makes an image publicly accessible for the stated temporary period.

Mitigation: Confirm the image may be made public before uploading, and prefer an already-approved public URL when possible.

Risk: Full API responses are stored locally and authentication, billing, payment, or order outputs may be sensitive.

Mitigation: Protect the local linkfox output directory, API-key environment variables, and any payment or billing artifacts before sharing logs or workspaces.

Risk: Custom LinkFox endpoint environment variables can redirect requests to another host.

Mitigation: Keep the default endpoint unless the replacement host is explicitly trusted.

Risk: Similarity scores can be mistaken for legal conclusions about infringement.

Mitigation: Present scores as visual-similarity signals only and recommend review by a qualified patent professional for legal decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-image-search)
- [Zhihuiya patent image search API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses or saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The main search script caches repeated parameter sets for 24 hours and writes full responses under a local linkfox data directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
