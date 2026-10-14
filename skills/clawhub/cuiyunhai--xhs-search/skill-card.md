## Description:

Searches public Xiaohongshu posts by keyword and returns post metadata, engagement figures, and optional CSV exports for content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

External content researchers and marketers use this skill to identify Xiaohongshu posts for topic research, competitor monitoring, and preliminary creator screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default service address uses unencrypted HTTP, which can expose the account token in transit.

Mitigation: Configure a working HTTPS service address before login; do not disable TLS certificate checks outside a trusted test environment.

Risk: Submitting a collection task can spend paid points without a technical approval gate.

Mitigation: Check the balance, quote the expected charge, and obtain explicit user confirmation before every submission.

Risk: Saved account tokens and exported search results may expose credentials or collected author information.

Mitigation: Keep local tokens and CSV files private, avoid sharing or committing them, and use collected data only for authorized research.

## Reference(s):

- [Xiaohongshu keyword search skill listing](https://clawhub.ai/cuiyunhai/skills/xhs-search)

## Skill Output:

**Output Type(s):** [Text, Files, Guidance]

**Output Format:** [Markdown summaries, JSON task results, and CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results include post links and public author and engagement details; CSV exports contain the collected results.]

## Skill Version(s):

2.0.1 (source: frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
