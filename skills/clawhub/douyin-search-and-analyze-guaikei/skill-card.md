## Description:

Uses Guaikei's Douyin tools to search public Douyin content, collect public account posts, retrieve comments, and track hot lists for content analysis, competitor monitoring, sentiment review, and trend research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and content teams use this skill to turn natural-language Douyin research requests into CLI calls that return structured public search, post, comment, and hot-list data. It is intended for internal research workflows such as topic discovery, competitor analysis, public comment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends keywords, target URLs, limits, and the API token to Guaikei's service.

Mitigation: Use it only for requests appropriate for the third-party service, avoid sensitive research topics or regulated personal data, and manage GUAIKEI_API_TOKEN through the environment with normal rotation practices.

Risk: Full scraped results are automatically retained on disk under the skill's logs directory.

Mitigation: Treat logs as retained research data; restrict access, delete unneeded outputs, and avoid collecting data that your workflow is not allowed to store.

Risk: The skill can run on ambiguous short-video requests and may collect Douyin public data when the user did not explicitly name Douyin.

Mitigation: Confirm the intended platform and scope before running broad or ambiguous collection requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/douyin-search-and-analyze-guaikei)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Usage documentation](readme.md)
- [Complete option reference](references/options.md)
- [Changelog](references/changelog.md)
- [Input and output JSON schemas](assets/*.schema.json)
- [Guaikei service site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Analysis guidance]

**Output Format:** [JSON on stdout, diagnostic logs on stderr, and JSON result files saved under logs/]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >=16.14 and GUAIKEI_API_TOKEN; supports keyword, URL, sort, time, duration, content type, and limit parameters.]

## Skill Version(s):

1.0.0 (source: package.json, artifact changelog, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
