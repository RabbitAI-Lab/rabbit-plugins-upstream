## Description:

Lunheng Article Pipeline coordinates OpenClaw subagents to produce evidence-based long-form academic, business, industry, or public-account articles with literature, data, case, analysis, writing, critique, audit, and human review stages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to orchestrate rigorous long-form research writing over published sources, with explicit checkpoints for topic consent, outline review, drafting, adversarial critique, audit, and final delivery. It is not intended for short-form writing or sensitive unpublished material unless the user chooses local or sanitized handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Topics, prompts, sources, drafts, and cover prompts may be sent to external search, extraction, image-generation, and model providers.

Mitigation: Complete the Phase 0 consent gate before use; for sensitive or unpublished material, choose sanitized wording, local model handling, and local SVG image options.

Risk: The workflow writes a multi-file project tree in the workspace.

Mitigation: Confirm the project name and planned file list before Phase 1, and keep writes constrained to the workspace run directory.

Risk: Generated long-form research can still contain weak evidence, outdated sources, or unsupported claims.

Mitigation: Use the built-in human review checkpoints, evidence cards, adversarial critique, and audit reports before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [README](README.md)
- [Skill definition](SKILL.md)
- [Pipeline runbook](references/pipeline-readme.md)
- [Deliverables, failure modes, and gates](references/deliverables.md)
- [M-Gate algorithm specification](references/_shared/M-Gate-Algorithm.md)
- [Failure modes](references/_shared/failure-modes.md)
- [Case studies](references/case-studies.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance]

**Output Format:** [Markdown documents and structured project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a run directory with briefs, status files, evidence cards, outlines, drafts, audit reports, final article files, image assets, evidence packages, and delivery notes.]

## Skill Version(s):

2.2.11 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
