## Description:

Provides Google-backed image discovery via Serper.dev, returning image URLs, page URLs, titles, and source domains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Serper.dev for candidate image results and return result metadata, URL-only lists, or raw JSON for downstream review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and a Serper API key are used with Serper.dev.

Mitigation: Confirm that use of SERPER_API_KEY and transmission of search queries to Serper.dev are acceptable before installing or running the skill.

Risk: The inspected package includes an unused requests dependency that is not pinned.

Mitigation: Remove the unused dependency or pin it before deployment if requirements.txt is installed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-search-image)
- [Publisher profile](https://clawhub.ai/user/sensenova-skills)
- [Serper image search API endpoint](https://google.serper.dev)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Formatted text lists, newline-delimited URLs, or raw JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save raw JSON to a caller-provided file path; requires SERPER_API_KEY and sends search queries to Serper.dev.]

## Skill Version(s):

2026.8.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
