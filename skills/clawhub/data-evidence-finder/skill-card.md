## Description:

Find citable statistics, verify scope and conflicting claims, and save evidence tables and citations in JishuDB. / 查找可引用数据，核对统计口径和矛盾证据，将数据表与引用保存到JishuDB。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill when a proposal, presentation, market question, or claim needs citable numerical evidence, checked statistical scope, qualified citations, and retained JishuDB evidence records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unapproved source retention or uploads could store data the user is not authorized to retain.

Mitigation: Require approval for the JishuDB knowledge base, output directory, source retention choices, and uploads or imports before saving sources.

Risk: Conflicting or incompatible statistics could be merged or cited beyond their measured scope.

Mitigation: Preserve raw values, periods, geography, units, definitions, and observed or forecast status; label contradictions and non-comparable measurements separately.

Risk: Chart or image-only evidence can be misread when OCR or vision support is unavailable or uncertain.

Mitigation: Use authorized OCR or vision only when available, record uncertain digits and image locators, and exclude unverified extraction from recommended numerical support.

Risk: Private user documents or confidential facts could be exposed through public discovery queries.

Mitigation: Use only public or explicitly authorized browsing and never place private documents or confidential facts into public search queries.

## Reference(s):

- [Evidence contract](references/evidence-contract.md)
- [ClawHub skill page](https://clawhub.ai/bowen-aijishu/skills/data-evidence-finder)
- [Project homepage](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/data-evidence-finder)
- [199IT report category](https://www.199it.com/archives/category/report)
- [199IT RSS feed](https://www.199it.com/feed)

## Skill Output:

**Output Type(s):** [Files, Markdown, Text, Guidance]

**Output Format:** [CSV evidence tables, Markdown notes, citation text, discrepancy notes, revision manifests, and JishuDB records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include evidence.csv, evidence-notes.md, citation-text.md, discrepancies.md, revision.md, and linked JishuDB records when approved.]

## Skill Version(s):

0.1.2 (source: evidence.json release.version and skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
