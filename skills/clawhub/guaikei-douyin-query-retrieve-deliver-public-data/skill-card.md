## Description:

Fetches public Douyin search results, creator posts, video comments, and hot-list data through CLI commands and returns structured JSON for analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content teams use this skill to retrieve public Douyin data for keyword research, creator monitoring, comment review, trend tracking, and downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords, video URLs, author URLs, result limits, and the GUAIKEI token are sent to guaikei.com.

Mitigation: Install and run the skill only when that data transfer is acceptable, use explicit Douyin requests, and keep the GUAIKEI_API_TOKEN scoped and protected.

Risk: Retrieved public comments, identifiers, and related result data may be saved under the skill's logs directory by default.

Mitigation: Periodically review and delete logs that contain comments or identifiers, and avoid retaining data beyond the user's operational need.

Risk: Broad auto-trigger rules can run the skill for ambiguous short-video research requests.

Mitigation: Confirm user intent for broad or ambiguous requests and avoid collecting data unless the request clearly targets public Douyin data.

Risk: Use of retrieved public data may be subject to Douyin terms and privacy obligations.

Mitigation: Confirm that collection, storage, and downstream analysis comply with applicable platform terms, privacy obligations, and internal policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-query-retrieve-deliver-public-data)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Usage documentation](artifact/readme.md)
- [Command options](artifact/references/options.md)
- [Input and output schemas](artifact/assets/)
- [Changelog](artifact/references/changelog.md)
- [GUAIKEI token and help site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON on stdout with logs and prompts on stderr; Markdown documentation describes CLI usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a GUAIKEI_API_TOKEN environment variable and may save retrieved public data under the skill logs directory.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, SKILL.md metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
