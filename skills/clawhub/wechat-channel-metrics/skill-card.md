## Description:

Retrieves precise WeChat Channel video engagement metrics, including likes, comments, favorites, shares, and plays, and marks whether values are exact or display-rounded.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators, social media analysts, and agents use this skill to query metrics or work metadata for a specific WeChat Channel video. It is intended for workflows that need exported JSON, Markdown, report Markdown, or Excel results after API-key setup and paid-call confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a WeMedia API key and may store it in local configuration.

Mitigation: Install only when local API-key storage is acceptable, restrict access to the skill directory, and rotate the key if it is exposed.

Risk: Queries send requested WeChat Channel video identifiers or URLs to api.we-media.cn.

Mitigation: Use the skill only for data that may be shared with that service, and avoid submitting sensitive local paths or unrelated identifiers.

Risk: ClawHub security evidence marks the release suspicious because broader API and file-upload capabilities are bundled beyond the narrow metrics workflow.

Mitigation: Review before installing, avoid local file-path inputs, and prefer a publisher update that removes upload and unrelated endpoint capabilities before broad deployment.

Risk: The skill writes result and cache files on disk.

Mitigation: Run it in a workspace where generated Markdown, JSON, Excel, and cache files can be retained or deleted according to the user's data-handling policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-channel-metrics)
- [ClawHub publisher profile](https://clawhub.ai/user/dunkong)
- [WeMedia API site](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python shell commands; runtime outputs can be Markdown, JSON, Excel, or report Markdown files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and a WeMedia API key. The script prints machine-readable markers for key setup, confirmation, consumption, balance, row count, and output file path.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter reports v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
