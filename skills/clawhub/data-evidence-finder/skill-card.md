## Description:

Finds citable statistics and research evidence for market claims, checks measurement scope and conflicting findings, and retains evidence in JishuDB.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and proposal writers use this skill to verify numerical market claims, compare conflicting statistics, and produce traceable evidence tables and qualified citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional JishuDB Desktop setup can install and launch a per-user app and create local endpoint configuration.

Mitigation: Review the helper's approval scope and confirm the intended target before allowing installation.

Risk: Evidence and source material may be uploaded to or retained in the selected JishuDB knowledge base.

Mitigation: Confirm the destination and source-retention scope before writes or uploads; do not share tokens in chat.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bowen-aijishu/skills/data-evidence-finder)
- [Source homepage (declared in skill metadata)](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/data-evidence-finder)
- [Evidence and citation contract](references/evidence-contract.md)
- [JishuDB setup guide](references/jishudb-setup/setup.md)

## Skill Output:

**Output Type(s):** [CSV evidence tables, Markdown analysis and citations, JishuDB records]

**Output Format:** [CSV and Markdown files with retained JishuDB records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source scope, discrepancies, and qualified citations; requires authorized research and JishuDB write access.]

## Skill Version(s):

0.1.5 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
