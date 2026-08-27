## Description:

Uses Guaikei API-backed Node.js commands to retrieve structured public Douyin search results, creator posts, video comments, and hot-list data for short-video research and monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and content teams use this skill to collect public Douyin video, creator, comment, and trending-list data for content research, competitor analysis, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin search terms, target URLs, result limits, and GUAIKEI_API_TOKEN are sent to Guaikei's API.

Mitigation: Use the skill only for explicit Douyin public-data tasks and install it only when that data sharing is acceptable.

Risk: Generated log files can contain research topics, profile or video identifiers, public comments, and author metadata.

Mitigation: Protect or delete the logs directory when the exported data is no longer needed.

## Reference(s):

- [Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-instant-public-data)
- [Publisher Profile](https://clawhub.ai/user/engheng-art)
- [Complete Options](references/options.md)
- [Changelog](references/changelog.md)
- [Input and Output JSON Schemas](assets/*.schema.json)
- [Guaikei Token and Support Site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON from command stdout, with operational guidance and shell commands for invocation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results may also be saved as timestamped JSON files under logs/.]

## Skill Version(s):

1.0.0 (source: release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
