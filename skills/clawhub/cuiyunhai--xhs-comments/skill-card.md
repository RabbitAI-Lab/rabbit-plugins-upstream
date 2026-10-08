## Description:

Collects public Xiaohongshu note comments in batches and returns comment details for analysis or CSV export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and analysts collect publicly available Xiaohongshu note comments to monitor audience feedback and compare discussion across notes. The skill supports batch collection, comment lookup, and CSV export; use requires an account and credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default HTTP backend can expose account tokens and collected comments in transit.

Mitigation: Avoid the default endpoint on untrusted networks; use a verified HTTPS service address if the provider supports it.

Risk: Stored account tokens and exported comments may expose credentials or identifiable user information if shared or retained carelessly.

Mitigation: Treat the saved token like a password and limit sharing and retention of comment exports to authorized uses.

## Reference(s):

- [Xiaohongshu Comments skill on ClawHub](https://clawhub.ai/cuiyunhai/skills/xhs-comments)

## Skill Output:

**Output Type(s):** [JSON, CSV files, Guidance]

**Output Format:** [JSON command responses and optional CSV exports; agent summaries in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Comment records can include nickname, content, like count, IP location, and reply count.]

## Skill Version(s):

1.1.0 (source: release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
