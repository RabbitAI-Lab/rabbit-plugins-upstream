## Description:

Guides the preparation, review, validation, publication, and follow-up of technical content and other release assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and methodology all rights reserved

## Use Case:

Developers and content teams use this skill to turn technical designs into publication-ready materials, check release readiness, and document follow-up. Its bundled tools can generate local file-hash attestations and a security radar chart; it is not a complete automated publishing pipeline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled attestation and manifest may not match this release.

Mitigation: Regenerate and verify the attestation and manifest against the final package before relying on integrity claims.

Risk: Broad trigger words and file-write and web-search permissions can bring the skill into unrelated tasks.

Mitigation: Invoke it only for publication-readiness work and review proposed writes and searches before execution.

## Reference(s):

- [ClawHub release listing](https://clawhub.ai/zhaoxinghua09-cell/skills/content-publish-lifecycle)
- [Attestation template](references/attestation-template.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance and checklists with optional local attestation and chart files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-first; can respond in the user's language. Publishing requires separate review and action.]

## Skill Version(s):

1.0.2 (source: ClawHub release; bundled skill files say 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
