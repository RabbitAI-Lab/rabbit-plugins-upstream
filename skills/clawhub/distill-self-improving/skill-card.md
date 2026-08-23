## Description:

Distill Self-Improving indexes user-specified local files, directories, projects, or document collections into a local knowledge structure, creating navigation records and concise Markdown distillations while leaving original files unchanged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzusp](https://clawhub.ai/user/zzusp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and operators use this skill when they explicitly want local files or project directories indexed, audited, and distilled into reusable navigation records and concise summaries. It is suited for scoped local knowledge-base maintenance rather than general reading, ad hoc Q&A, or automatic background discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local persistence of file paths, metadata, and derived summaries may expose sensitive project or personal information.

Mitigation: Use the skill only on clearly scoped directories or files, and exclude sensitive folders unless local retention of paths, metadata, and summaries is acceptable.

Risk: Broad directory scopes can include more local files than the user intended.

Mitigation: Freeze included and excluded paths before processing, report exclusion rules and counts, and avoid following reparse points or unauthorized adjacent directories.

Risk: Summaries or distillations can become stale or misleading if source files change after indexing.

Mitigation: Recheck source file identity and rerun the validation gates before relying on existing distillations for current decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zzusp/skills/distill-self-improving)
- [Distillation scenarios and failure handling](artifact/references/distillation-scenarios.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown, CSV ledgers, validation commands, and concise text reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local navigation, manifest, inventory, per-file distillation, and optional project summary artifacts under ~/.agent-knowledge/ for explicitly scoped inputs.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
