## Description:

Query Google Places API (New) via the goplaces CLI for text search, place details, resolve, and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aperdigaokbk](https://clawhub.ai/user/aperdigaokbk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up places, retrieve place details and reviews, and produce either human-readable place results or JSON suitable for scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party Homebrew tap and upstream CLI.

Mitigation: Install only if you trust the tap and upstream project, and review updates before deployment.

Risk: The Google Places API key can expose quota, billing, or data-access risk if misused.

Mitigation: Use a dedicated API key with API restrictions, quota limits, and billing controls, and rotate it if compromise is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aperdigaokbk/skills/goplaces)
- [goplaces homepage](https://github.com/steipete/goplaces)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, JSON]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON output from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the goplaces binary and GOOGLE_PLACES_API_KEY.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
