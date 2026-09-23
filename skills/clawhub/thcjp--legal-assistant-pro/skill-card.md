## Description:

Legal Doc Reviewer assists with NDA review, contract version comparison, legal citation checking, meeting brief generation, and weekly status reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Legal and business teams use this skill to draft structured review outputs for contracts, citations, meetings, and status reporting. Its outputs are decision-support materials and require qualified legal review before use as legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External callback handling may expose privileged or confidential legal material.

Mitigation: Use callback_url only with controlled, approved endpoints; omit it for privileged or highly confidential documents.

Risk: Broad command execution and local file writes may create unintended files, logs, or data exposure.

Mitigation: Run the skill in a restricted workspace, limit permissions, and review generated files and logs before sharing.

Risk: Legal-document analysis, citation checks, and privilege labels may be incomplete, outdated, or jurisdiction-specific.

Mitigation: Require qualified legal review and verify current law, citations, and privilege determinations before relying on outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/legal-assistant-pro)
- [National Laws and Regulations Database](https://flk.npc.gov.cn)
- [China Judgments Online](https://wenshu.court.gov.cn)
- [PKULaw](https://www.pkulaw.com)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown reports with structured tables, risk notes, source links, action lists, and disclaimers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically writes local Markdown files under output/{id}/ paths and may include operation logs for traceability.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
