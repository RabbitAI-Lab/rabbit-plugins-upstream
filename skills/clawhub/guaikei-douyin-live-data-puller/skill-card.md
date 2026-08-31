## Description:

Pulls public Douyin search results, creator posts, video comments, and hot-list data as structured JSON for content research, competitor analysis, public-opinion review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect public Douyin data for short-video topic research, competitor monitoring, comment analysis, and trend tracking. It is intended for explicit Douyin public-data tasks and not for posting, editing, watermark removal, private-data access, or other platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, Douyin URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only for explicit public Douyin data tasks, avoid sensitive queries, and use a scoped token that can be rotated if exposed.

Risk: Collected social-media results are saved under the skill logs directory by default.

Mitigation: Avoid running the skill on shared machines for sensitive research, and delete exported logs when they are no longer needed.

Risk: The skill may activate on broad short-video research or competitor-analysis requests even when Douyin is not named.

Mitigation: Confirm the platform and user intent before execution when the request is ambiguous or could involve another platform.

Risk: Runtime messages may expose service-contact or token-acquisition prompts during token failures.

Mitigation: Review stderr before sharing logs externally and avoid forwarding token-related error output to end users unless it has been checked.

## Reference(s):

- [Skill README](readme.md)
- [Complete Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Input and Output JSON Schemas](assets/*.schema.json)
- [Guaikei Service Site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON on stdout with logs on stderr and optional saved JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14 or newer and GUAIKEI_API_TOKEN; commands must run from the skill root.]

## Skill Version(s):

1.0.0 (source: release evidence, package.json, changelog, constants.js)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
