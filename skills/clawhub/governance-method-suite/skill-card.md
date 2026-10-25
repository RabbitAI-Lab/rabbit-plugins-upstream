## Description:

A playbook that routes agents through nine independently published skills for security checks, controls, credentials, and release gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and governance reviewers use this suite to plan agent security audits and pre-release reviews, then find the appropriate independently published sub-skill for each stage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Treating the suite's routing guidance as a complete security assessment could leave issues in individual sub-skills unchecked.

Mitigation: Review each referenced sub-skill separately before use, especially those handling prompts, documents, badges, release gates, or kill-switch procedures.

## Reference(s):

- [Governance Method Suite on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/governance-method-suite)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Markdown guidance or plain-text stage and sub-skill routing table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists nine governance stages or gives usage and expected output for a selected stage; does not run the sub-skills.]

## Skill Version(s):

1.0.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
