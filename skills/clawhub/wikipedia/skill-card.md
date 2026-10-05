## Description:

Provides agents with Wikipedia and Wikimedia search, article summaries, historical revisions, media, and related research tools through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Researchers, writers, and developers use this skill to look up Wikipedia articles, source links, historical edits, and Wikimedia media across supported languages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, article titles, coordinates, usernames, and IP addresses may be sent to Wikipedia or Wikimedia services.

Mitigation: Avoid submitting sensitive inputs unless their disclosure to those services is acceptable.

Risk: Public contributor and IP-edit information may be personally sensitive.

Mitigation: Limit collection and sharing of contributor or IP-edit results to necessary use.

Risk: Unpinned Python dependencies can change after installation.

Mitigation: Pin and review dependency versions before production deployment.

## Reference(s):

- [Wikipedia MCP on ClawHub](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Structured MCP tool responses with article text, metadata, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some tools return media links, contributor details, or dated article revisions.]

## Skill Version(s):

1.6.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
