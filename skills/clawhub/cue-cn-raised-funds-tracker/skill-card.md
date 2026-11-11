## Description:

Creates a sourced ledger of A-share raised-funds balances, project spending and disclosed progress, changes, substitutions, and closing balances.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Financial analysts and corporate reporting teams use this skill to turn an A-share raised-funds disclosure into a period-by-period ledger of proceeds, dedicated-account balances, project spending and disclosed progress, and changes or substitutions. Each entry is tied to a quoted disclosure passage; the skill does not make compliance or investment judgments.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious, citing an offline-boundary conflict, local usage markers and home-directory tracking, and a validator exception for self-calculated figures; some components were only partially analyzed and the tool-misuse analyzer was degraded.

Mitigation: Review the reported behavior before installation, limit access to files and credentials, and verify each ledger entry against its cited disclosure text.

Risk: The scan does not establish whether financial documents or credentials are sent remotely, and it does not establish that the artifact is safe.

Mitigation: Confirm runtime behavior before supplying sensitive reports or CUE_API_KEY; do not infer a safe or unsafe transmission outcome from this scan alone.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/huhoo/skills/cue-cn-raised-funds-tracker)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese Markdown ledger with six fixed sections, quoted disclosure text, source anchors, and a source list; without CUE_API_KEY it produces a fill-in outline.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records one item per account, project, and reporting period; copies disclosed progress percentages rather than calculating them.]

## Skill Version(s):

0.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
