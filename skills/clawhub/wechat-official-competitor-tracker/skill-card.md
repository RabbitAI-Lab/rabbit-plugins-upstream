## Description:

This skill helps an agent track WeChat Official Account competitors by retrieving account profiles, recent article lists, and article interaction metrics, then summarizing recent performance and top-performing posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to monitor a WeChat Official Account's recent publishing activity, article engagement, and overall account performance. It is suited for competitor tracking workflows that need profile data, article history, and interaction metrics exported into local reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a WeMedia API key and may write local report and cache files.

Mitigation: Use a dedicated API key with appropriate spending controls, store it only in the expected configuration location or environment variable, and review generated local files before sharing.

Risk: A local-file upload path exists even though file upload is not part of the advertised competitor-tracking workflow.

Mitigation: Do not use --file or pass local paths unless the upload behavior has been reviewed and explicitly approved.

Risk: Pagination can cause multiple paid API calls while the displayed estimate may show only one call.

Mitigation: Keep --pages at 1 unless additional pages are required, and confirm the expected total number of paid calls before running with --yes.

Risk: The artifact includes shipped Python bytecode files.

Mitigation: Remove __pycache__ artifacts from the release package before broad deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-official-competitor-tracker)
- [WeMedia API site](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown, JSON, or Excel files with terminal status markers and preview text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes report/cache files locally and reports consumption, balance, row count, and output path markers after API execution.]

## Skill Version(s):

1.0.1 (source: server release metadata; bundled frontmatter says v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
