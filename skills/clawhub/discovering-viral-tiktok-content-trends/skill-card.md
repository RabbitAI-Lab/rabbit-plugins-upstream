## Description:

Discovers viral content trends and trending formats on TikTok using apidojo's TikTok scraper on Apify, returning trend metrics, content format patterns, and hook analysis for a requested niche.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, brand social teams, and video strategists use this skill to research viral TikTok posts in a niche, identify repeatable formats and hooks, and produce actionable content recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends selected TikTok URLs or search keywords to Apify and requires an APIFY_TOKEN.

Mitigation: Use the skill only when that data flow is acceptable, scope the token appropriately, and avoid submitting sensitive campaign plans or private identifiers as search inputs.

Risk: The optional local scripts/run_actor.js helper is referenced but not bundled in the artifact.

Mitigation: Review any local helper implementation before running it, or use the disclosed Apify MCP or REST API path instead.

Risk: Saved CSV or JSON output files can overwrite prior reports if filenames are reused.

Mitigation: Use unique, date-stamped output filenames when preserving earlier trend reports matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/discovering-viral-tiktok-content-trends)
- [Apify TikTok scraper actor](https://apify.com/apidojo/tiktok-scraper)
- [Apify actor run API endpoint](https://api.apify.com/v2/acts/apidojo~tiktok-scraper/runs?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, guidance]

**Output Format:** [Markdown trend report with tables, scores, examples, shell command snippets, and API call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CSV or JSON result files when the optional Apify helper is used.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
