## Description:

This skill supports Douyin public-data research by running keyword search, author post collection, video comment retrieval, and real-time hot-list queries for content research, competitor analysis, sentiment insight, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, marketers, and content researchers use this skill to collect structured public Douyin data for topic discovery, competitor monitoring, comment analysis, and trend tracking. It is suited for workflows where an agent can translate natural-language research requests into the provided Node.js commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin research queries, target URLs, the API token, and fetched public data may be sent to guaikei.com or saved locally under logs by default.

Mitigation: Use the skill only for intended Douyin public-data research, keep GUAIKEI_API_TOKEN in the environment, restrict access to generated logs, and delete or protect logs that contain sensitive research targets, comments, or account data.

Risk: Broad activation rules may cause an agent to run this skill for short-video research even when the user has not explicitly named Douyin.

Mitigation: Confirm that the user wants Douyin public-data research before running commands when the requested platform or data source is ambiguous.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-omni-public-data)
- [Skill documentation](artifact/readme.md)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Input and output JSON schemas](artifact/assets/)
- [Guaikei token and support site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON to stdout with stderr logs and JSON result files saved under logs/.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; command outputs follow the JSON schemas in artifact/assets/.]

## Skill Version(s):

1.0.0 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
