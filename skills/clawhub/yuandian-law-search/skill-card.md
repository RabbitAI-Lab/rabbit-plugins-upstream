## Description: <br>
Searches the YuanDian/Open ChinaLaw platform for Chinese legal provisions, regulations, cases, company records, and hallucination checks to support legal research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cat-xierluo](https://clawhub.ai/user/cat-xierluo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Lawyers, legal researchers, and agent workflows use this skill to retrieve Chinese statutes, regulations, cases, enterprise records, and supporting evidence for legal analysis and research reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Legal queries, company lookups, and hallucination-detection text are sent to YuanDian/Open ChinaLaw services. <br>
Mitigation: Install and use the skill only when that external processing is acceptable for the matter and data involved. <br>
Risk: Sensitive legal research results can be retained locally in archives and generated report files. <br>
Mitigation: Use --no-cwd-report for confidential work, set project-specific archive locations where appropriate, and periodically delete archive materials that no longer need to be retained. <br>
Risk: The manual update flow can replace skill files from an unsigned GitHub update channel. <br>
Mitigation: Avoid do-update unless the upstream repository or downloaded version has been reviewed and verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/yuandian-law-search) <br>
- [clawdis homepage](https://github.com/cat-xierluo/legal-skills) <br>
- [YuanDian/Open ChinaLaw platform](https://open.chineselaw.com) <br>
- [README](artifact/README.md) <br>
- [Keyword expansion guide](artifact/references/01-keyword-expansion.md) <br>
- [Typical legal research workflows](artifact/references/02-typical-workflows.md) <br>
- [Report consolidation guide](artifact/references/03-report-consolidation.md) <br>
- [Enterprise portrait guide](artifact/references/06-enterprise-portrait.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and generated legal research report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include local archives of API queries and responses for later review.] <br>

## Skill Version(s): <br>
1.7.5 (source: server release, SKILL.md frontmatter, CHANGELOG released 2026-07-20) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
