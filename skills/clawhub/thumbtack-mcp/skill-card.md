## Description:

Query Thumbtack from a shell to search local service professionals and read public profile details using curl, jq, and a bundled Node.js HTML extractor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to gather public Thumbtack search and profile data for local service providers from shell workflows or one-shot scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-directed requests to Thumbtack public pages and anonymous GraphQL endpoints.

Mitigation: Use it only for read-only lookup, avoid credentials or account pages, and respect Thumbtack terms and rate limits.

Risk: Thumbtack page and GraphQL response shapes can vary or fail even when HTTP status is 200.

Mitigation: Check extractor exit codes and GraphQL errors arrays, select the correct extraction mode for each page type, and handle missing or union-shaped fields.

## Reference(s):

- [Thumbtack discovery recipes](references/discovery.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled extractor emits JSON from HTML supplied on stdin; documented workflows are read-only.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
