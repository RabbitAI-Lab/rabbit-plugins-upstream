## Description:

Search Google Shopping for product discovery, offers, and price comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run focused Google Shopping searches through Dataify, compare products and offers, and receive concise shopping results or raw API output when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Dataify API token and may spend Dataify credits for Google Shopping lookups.

Mitigation: Configure DATAIFY_API_TOKEN in the shell instead of passing it as a command argument, and review high-volume or multi-page searches before execution.

Risk: User-selected search parameters are sent to Dataify for Google Shopping lookup.

Mitigation: Keep requests scoped to product discovery data and avoid including unnecessary sensitive information in shopping queries or filters.

## Reference(s):

- [Google Shopping API Reference](references/google_shopping_api.md)
- [Dataify Dashboard Login](https://dashboard.dataify.com/login?utm_source=skill)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-google-shopping)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, parameter previews, shell commands, and raw JSON or HTML when explicitly requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN; Google Shopping lookups may spend Dataify credits.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
