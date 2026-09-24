## Description:

浙江工程招投标合同公示的供应商视角整理，按公司查中标项目、时间、金额与同类报价区间。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up a Zhejiang public-works supplier's winning tender history, contract dates, amounts, and peer price ranges for similar project types. The skill should be used for Zhejiang engineering tender history, not national tender coverage, non-engineering procurement, or enterprise credit evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender search queries are sent to the publisher's HTTPS service.

Mitigation: Avoid using sensitive or unrelated query data, and evaluate the publisher service before use in sensitive workflows.

Risk: Product credentials, cookies, and an install identifier are stored in plaintext under ~/.odf.

Mitigation: Keep unrelated secrets out of that file, protect local filesystem access, and remove the file when access is no longer needed.

Risk: The underlying dataset covers only collected public contract notices, so missing records can be misread as no tender history.

Mitigation: Tell users that uncollected records may exist and do not present the output as enterprise credit evaluation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/zj-tender-history)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Plain text or Markdown-style tender-history results produced after running a local Node.js command.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include project lists, signing dates, contract amounts, amount bands, peer percentile ranges, coverage notes, and exclusion notes.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter and manifest list 1.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
