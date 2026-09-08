## Description:

Helps users retrieve article-level WeChat Official Account analytics, including basic article metadata, engagement metrics, extracted content, media lists, snapshots, and full reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and agents use this skill to run selected WeMedia API queries for a single WeChat Official Account article and export the returned data as a report or data file after confirming paid requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a WeMedia API key and can make paid API calls after user confirmation.

Mitigation: Install only when the publisher is trusted, provide an API key only in the intended runtime, and require explicit review of the fee estimate before running paid endpoints.

Risk: The skill stores returned results as local files.

Mitigation: Review output paths before sharing files and handle exported article data according to the user's data-retention and confidentiality requirements.

Risk: Release evidence flags bundled bytecode and out-of-scope file-upload/API capabilities for review.

Mitigation: Remove shipped .pyc files before approval, isolate or remove unrelated upload helpers, and make any local-file upload behavior explicit and opt-in.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-official-article-analytics)
- [WeMedia API site](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Excel files, Shell commands, Configuration guidance]

**Output Format:** [Markdown, JSON, or Excel files with terminal status markers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes result files locally and reports output path, total consumption, and account balance when available.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter reports v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
