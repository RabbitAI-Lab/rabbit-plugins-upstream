## Description:

mab-fto-check helps agents perform monoclonal antibody patent freedom-to-operate analysis using PatSnap patent search, sequence alignment, structure search, claim comparison, and a standardized single-file HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent, IP, and antibody development teams use this skill to collect required molecule and market inputs, run multi-module monoclonal antibody FTO searches, compare independent patent claims, and draft a source-backed FTO report. It is intended as decision support and requires attorney review before relying on conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Antibody sequences and business context may be sent to authorized patent and biology search services during normal use.

Mitigation: Use the skill only with approved PatSnap/Zhihuiya MCP accounts and confirm that the data is permitted to be shared with those services.

Risk: FTO conclusions can be incorrect or incomplete if generated without source-backed claim text or legal review.

Mitigation: Require original claim text from PatSnap MCP or approved local documents, keep unsupported patents marked pending, and have a qualified patent attorney review conclusions before business reliance.

Risk: Incomplete intake data can produce misleading search scope or jurisdiction filtering.

Mitigation: Collect sequence, target, indication, target market, competitor, and legal-status preferences before running the full workflow; otherwise limit output to an M1 sequence-search preview.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/mab-fto-check)
- [Zhihuiya Open Platform](https://open.zhihuiya.com/)
- [User intake protocol](references/user-intake-protocol.md)
- [Search modules](references/search-modules.md)
- [Modification search](references/modification-search.md)
- [Workflow steps](references/workflow-steps.md)
- [Search loop](references/search-loop.md)
- [Sequence search](references/sequence-search.md)
- [Patent family merge](references/patent-family-merge.md)
- [Output contract](references/output-contract.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON intermediate files, shell command examples, configuration guidance, and a self-contained HTML report.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The complete FTO workflow depends on authorized PatSnap/Zhihuiya MCP access; without that access the skill can provide only an analysis framework or limited preview.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
