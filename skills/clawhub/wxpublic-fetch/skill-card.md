## Description:

Fetches WeChat public-account articles for a specified account and date range, saves the articles as local Markdown files with downloaded images, and records saved paths for follow-up questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiongweixp](https://clawhub.ai/user/xiongweixp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to retrieve WeChat public-account articles by account name and date range, then save the resulting content locally for reading, summarization, and follow-up analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires AppID and SecureKey credentials for the article-list service.

Mitigation: Prefer environment variables over inline command arguments, rotate credentials if exposed, and avoid sharing logs or transcripts that include secrets.

Risk: Requested article URLs and fetched content are processed by external services.

Mitigation: Review whether the target accounts, URLs, or article contents are sensitive before use, and avoid using the skill for confidential material.

Risk: The skill writes downloaded articles and images to a local output directory.

Mitigation: Use a dedicated output directory, review generated files before reuse, and clean up stored content when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiongweixp/skills/wxpublic-fetch)
- [wxpublic-fetch README](artifact/README.md)
- [微信公众号获取服务](https://wxpub.aibana.art)
- [anything-md conversion service](https://anything-md.doocs.org/)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown files, local image files, JSON manifest records, and a concise text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a local output directory with article Markdown files and an images subdirectory; uses AppID and SecureKey credentials supplied by arguments or environment variables.]

## Skill Version(s):

1.0.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
