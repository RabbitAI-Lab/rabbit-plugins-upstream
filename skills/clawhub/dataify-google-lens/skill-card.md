## Description:

Run Google Lens or reverse-image search from an image. Do not use for text-only Google Images queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to turn an image URL and optional Lens filters into a Dataify Google Lens request, then receive a compact summary of image-search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image URLs, optional query text, and search parameters are sent to Dataify for processing.

Mitigation: Use the skill only when that third-party API handling is acceptable, and avoid private, internal, signed, or sensitive image URLs.

Risk: The Dataify API token is required for live requests.

Mitigation: Configure the token through the environment and do not paste or expose it in chat, previews, or result summaries.

## Reference(s):

- [Dataify Google Lens API Reference](artifact/references/google_lens_api.md)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-google-lens)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with inline shell commands; raw JSON or HTML only when explicitly requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns compact result summaries by default, preserving source links and noting truncation when useful.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
