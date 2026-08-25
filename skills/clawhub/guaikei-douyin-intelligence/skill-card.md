## Description:

Provides Douyin public-data intelligence for keyword search, creator-post retrieval, comment analysis, and real-time hot-trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, marketers, and content teams use this skill to collect public Douyin search results, creator posts, comments, and hot trends for content planning, competitor monitoring, and public opinion analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research requests and target identifiers are sent to the third-party guaikei.com service.

Mitigation: Use the skill only for authorized public-data research, avoid sensitive competitors or account targets unless approved, and review requests before execution.

Risk: Successful search, post, and comment results are saved locally under the skill logs directory by default.

Mitigation: Protect the workspace, restrict access to generated logs, and delete logs that are no longer needed.

Risk: The GUAIKEI_API_TOKEN grants access to the third-party service.

Mitigation: Store the token only in an environment variable or secret manager, avoid committing or sharing it, and rotate it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-intelligence)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei service help](https://www.guaikei.com)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Input and output JSON schemas](assets/*.schema.json)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON data or log files from command execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results can contain up to 10,000 structured records per request and are saved under logs by default.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, changelog, and runtime constants)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
