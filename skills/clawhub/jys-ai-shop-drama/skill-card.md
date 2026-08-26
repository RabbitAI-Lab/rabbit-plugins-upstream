## Description:

JYS AI Shop Drama orchestrates a five-stage workflow for selecting short-drama advertising tropes, adapting plots, selecting products, writing scripts, and producing final shooting copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bettercalllu](https://clawhub.ai/user/bettercalllu)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and agent operators use this skill to manage a complete AI-assisted short-drama advertising workflow from concept selection through final script packaging. It is designed for staged human confirmation, shared trope and product libraries, and resumable project workspaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated advertising scripts may contain unsafe, under-disclosed, or non-compliant promotional claims.

Mitigation: Treat generated scripts as drafts and require human compliance review before public or commercial use.

Risk: Bundled content includes scam-themed scenarios and sensitive claim areas such as health, child, elder, chemical, food, or emergency-use contexts.

Mitigation: Review these scenarios carefully, avoid reusing blacklisted-product scripts, and remove or revise sensitive claims that are not substantiated.

Risk: The workflow can write to project workspaces and shared skill databases.

Mitigation: Approve workspace and database writes deliberately, and keep invocation triggers narrow where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bettercalllu/skills/jys-ai-shop-drama)
- [Release evidence](evidence.json)
- [WorkBuddy suite entry](artifact/SKILL.md)
- [JYS coordinator](artifact/jys/SKILL.md)
- [Workspace contract](artifact/jys/references/workspace-contract.md)
- [Creation rules](artifact/jys/references/creation-rules.md)
- [Static suite validation](artifact/jys/reports/validation.json)
- [State routing evaluation](artifact/jys/reports/state-routing-eval.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured plain text, with optional workspace Markdown files for project state and drafts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stage-gated S1-S5 workflow; project or shared-library writes are expected to occur only after user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
