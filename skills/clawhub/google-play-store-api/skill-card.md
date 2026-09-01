## Description:

Search Google Play, read full Android app listings including install counts and Data safety details, and page reviews by cursor through the Scavio API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to search Android apps, inspect Google Play listings, compare competitors, retrieve reviews, and collect structured app metadata for ASO or market research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SCAVIO_API_KEY exposure or misuse can authorize Scavio API calls.

Mitigation: Load the key from an environment variable or secret store, keep it out of source code, and rotate it if exposed.

Risk: Review pagination and repeated endpoint calls can consume credits quickly because each Google Play endpoint call costs credits.

Mitigation: Estimate credit use before deep crawls, cap pagination, and use the reviews already returned by the app listing before calling the reviews endpoint.

Risk: Google Play results can vary by country, language, sort order, and cursor state.

Mitigation: Record hl, gl, sort, and cursor choices, keep review sort fixed while paging, and treat a pagination 404 as the stop signal.

## Reference(s):

- [Scavio Google Play Search Documentation](https://scavio.dev/docs/google-play-search)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/google-play-store-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with API request examples and structured JSON response handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Google Play endpoint calls consume Scavio credits.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
