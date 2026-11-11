## Description:

Query Google Places for text search, place details, resolve, reviews, or scriptable JSON via goplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to install and configure goplaces, then run Google Places text search, place details, resolve, reviews, and JSON workflows from the command line.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install a third-party Homebrew tap and executable.

Mitigation: Install only after reviewing the publisher, tap, and release source according to local software supply-chain policy.

Risk: Google Places queries and API-key-backed requests are sent to Google Places or to a custom GOOGLE_PLACES_BASE_URL when configured.

Mitigation: Use an appropriately scoped GOOGLE_PLACES_API_KEY, avoid entering sensitive place queries, and set GOOGLE_PLACES_BASE_URL only to trusted endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/goplaces)
- [goplaces homepage](https://github.com/steipete/goplaces)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-output options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Human-readable command output by default; supports --json for scriptable responses.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
