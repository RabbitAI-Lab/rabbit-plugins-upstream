## Description:

Helps agents research WeChat public-account topics from seed keywords, hot-search terms, or competitor accounts, then produce opportunity scoring and local report artifacts from public article data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

Content strategists, creators, and agents use this skill to identify WeChat public-account topic opportunities, compare competitor account coverage, translate hot-search terms into durable writing angles, and generate report files for editorial planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a user-provided Mangg Cloud API key for live WeChat data collection.

Mitigation: Provide the key via the CLI or MANGE_API_KEY environment variable only in trusted sessions, and avoid saving it in shared files, logs, or public repositories.

Risk: Live scans can incur API usage costs, especially with larger per-word, expansion, account, or deep-sampling settings.

Mitigation: Review the documented cost estimates and generated cost summary before large runs; use --self-test or --from-json when validating behavior without additional API calls.

Risk: The skill writes local report, raw data, workbook, and snapshot files to user-selected paths.

Mitigation: Choose output paths appropriate for potentially sensitive editorial research data and review generated files before sharing.

Risk: Hot-search workflows can surface short-lived or sensitive current-event terms that may not be suitable for content planning.

Mitigation: Translate hot terms into durable topic angles and apply editorial review before running full analysis or acting on recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-topic-radar)
- [Mangg Cloud API](https://api.we-media.cn?source=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; optional local HTML, Markdown, JSON, Excel, and snapshot files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Mangg Cloud API key for live collection; offline self-test and from-JSON rerender modes are supported.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
