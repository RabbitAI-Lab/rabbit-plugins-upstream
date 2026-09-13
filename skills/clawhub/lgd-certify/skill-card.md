## Description:

lgd-certify helps agents guide users through a local CLI workflow that registers an AI artifact, hashes evidence files, runs a three-law gate check, and emits certification files and badge markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and AI governance reviewers use this skill to create self-attestation artifacts for AI projects, including an algorithm passport, evidence-chain hashes, PASS/FAIL gate output, certification JSON, and badge markdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated PASS results, certification.json, and badges may look authoritative even when they are only self-attestation artifacts.

Mitigation: Treat generated certification outputs as self-attestation unless an independent reviewer validates the evidence, state, and review process.

Risk: The certification gate can rely on local state that is not protected from tampering.

Mitigation: Protect the project directory, review the generated state files, and verify evidence-chain hashes before relying on the result.

Risk: The documented global npx install path is unpinned.

Mitigation: Use a reviewed immutable commit or pinned installer in higher-assurance environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-certify)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [LGD badge endpoint](https://medxpert.cn/badge)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown guidance with CLI commands and generated JSON or Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local project artifacts such as passport.json, evidence_chain.json, certification.json, and BADGES.md when its CLI is run.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
