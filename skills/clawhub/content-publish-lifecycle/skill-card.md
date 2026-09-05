## Description:

把技术方案 / 设计从「设计 → 落地 → 检查 → 验证 → 发布 → 沉淀」串成一条可复用发布流水线，用于回答「方案做完了怎么变成能发的东西」「发出去之前该查什么」这类问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Content creators, technical teams, and publishing operators use this skill to turn designs, technical plans, SOPs, expert packages, diagrams, or agent skills into release-ready materials with review, validation, publication, and retrospective steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security and governance claims are self-attested rather than independently certified.

Mitigation: Treat generated attestation, hash manifests, and radar outputs as release evidence for review, not as third-party assurance.

Risk: Integrity verification checks file hashes but does not prove that the content is semantically correct or compliant.

Mitigation: Review the release material, license terms, and compliance claims before publication in addition to running hash verification.

Risk: Helper scripts operate on local directories or zip files and can overwrite generated attestation artifacts in the selected output directory.

Mitigation: Run the scripts only against intended package directories or copies of release archives, and inspect generated file paths before distributing outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/content-publish-lifecycle)
- [Attestation template](artifact/references/attestation-template.md)
- [Security results](artifact/security_results.json)
- [Security radar](artifact/security-radar.svg)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with optional code and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce release checklists, attestation steps, validation notes, and publishing records.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
