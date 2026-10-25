## Description:

根据公司与报告期生成带来源追溯的财报深度点评初稿，并将评级与目标价留待人工判断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts and investment-research teams use it to draft source-traceable financial-report reviews for A-share and Hong Kong-listed companies. Ratings and target prices remain for human completion.

### Deployment Geography for Use:

China and Hong Kong

## Known Risks and Mitigations:

Risk: Optional connection checks can expose the Cue API key to unintended destinations.

Mitigation: Until destinations and redirects are safely validated, use the documented workflow without Cue credentials and avoid authenticated curl examples.

Risk: External document parsing and channel use may involve sharing documents, charges, or directory access.

Mitigation: Submit only public documents to external parsing, and deliberately approve charges and directory grants before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-cn-earnings-note)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Markdown report with a JSONL source index and progress ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [AI draft with traceable source labels; ratings and target prices are left for human review.]

## Skill Version(s):

0.3.42 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
