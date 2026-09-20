## Description:

resy-fpx helps agents query and act on Resy restaurant reservations from a shell with curl, including venue search, slot checks, booking, cancellation, favorites, and Priority Notify management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to turn Resy account operations into shell-ready curl workflows for scripts or environments where the Resy MCP server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Resy credentials, session-derived tokens, profile data, and payment metadata.

Mitigation: Keep tokens and credentials out of logs and transcripts, use environment variables, and rotate credentials or tokens if exposed.

Risk: Booking, cancellation, favorite, and notify commands mutate a live Resy account with no curl-layer dry run.

Mitigation: Require explicit confirmation before write actions and read back reservations or subscriptions before and after changes.

## Reference(s):

- [Resy API ready-to-run requests](references/resy-api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces copy-pasteable command guidance; live API responses depend on the user's Resy account and token.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
