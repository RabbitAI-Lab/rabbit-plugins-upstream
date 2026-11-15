## Description:

Query Google Places for text search, place details, resolve, reviews, or scriptable JSON via goplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use the goplaces command-line tool to search Google Places, resolve locations, and retrieve place details and reviews. Results can be read directly or returned as JSON for scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI requires a Google Places API key, which could be exposed if stored or shared carelessly.

Mitigation: Keep GOOGLE_PLACES_API_KEY in a secret store and avoid including it in shared commands or logs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/hillstreet-ph/skills/goplaces)
- [Project homepage](https://github.com/steipete/goplaces)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Text, JSON]

**Output Format:** [Command-line instructions and Google Places results in human-readable text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [JSON output is available for scripting; requires the goplaces CLI and GOOGLE_PLACES_API_KEY.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
