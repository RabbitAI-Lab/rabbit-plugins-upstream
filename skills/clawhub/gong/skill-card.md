## Description:

Gong API for searching calls, transcripts, and conversation intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jdrhyne](https://clawhub.ai/user/jdrhyne)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, sales operations teams, and authorized agents use this skill to query Gong call metadata, bounded transcript excerpts, user lists, and activity statistics without granting write access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gong queries can expose customer names, email addresses, recordings, and sensitive sales conversations.

Mitigation: Retrieve only the requested fields and time range, start with call metadata before transcripts, and avoid transcript or participant exports unless explicitly scoped by the user.

Risk: Local Gong credentials could be leaked or overused if handled casually.

Mitigation: Use the narrowest available Gong API key, keep credentials in the protected local file documented by the skill, avoid placing secrets in chat or shell arguments, and rotate keys through Gong settings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jdrhyne/skills/gong)
- [Publisher profile](https://clawhub.ai/user/jdrhyne)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON results from bounded Gong API queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only helper with bounded pagination, transcript excerpt limits, credential permission checks, tenant URL validation, and explicit partial-result indicators.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
