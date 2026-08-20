## Description:

Distill Self-Improving indexes user-confirmed local files, directories, projects, or document collections into a local knowledge structure with navigation, audit ledgers, per-file Markdown distillations, optional group summaries, and explicit skip reasons while leaving original files unchanged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzusp](https://clawhub.ai/user/zzusp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge workers use this skill when they explicitly want an agent to register local project or document paths, build auditable indexes, and produce concise per-file or cross-file summaries for later lookup. It is suited to controlled local knowledge-base maintenance, not ordinary one-off file reading or automatic discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-authorized local files and persists summaries and indexes that may expose sensitive project or document details.

Mitigation: Review the exact paths before authorizing processing, treat ~/.agent-knowledge as sensitive, and rely on the skill's skip guidance for credentials, private data, and other restricted content.

Risk: A stale or incorrect distillation could misrepresent the current source file.

Mitigation: Recheck original files before relying on prior summaries and run the bundled collection validator gates for scope, manifest, source mapping, and output consistency.

Risk: Unintended directories could be indexed if the requested scope is ambiguous.

Mitigation: Use only user-confirmed paths, stop for clarification when boundaries are unclear, and keep discovered but unconfirmed paths out of scope.

## Reference(s):

- [Batch Migration, Exceptions, and Real Scenarios](references/distillation-scenarios.md)
- [ClawHub skill page](https://clawhub.ai/zzusp/skills/distill-self-improving)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown files, CSV ledgers, validator command guidance, and concise text status reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes owned navigation, scope, inventory, manifest, distillation, and summary artifacts under ~/.agent-knowledge; original source files remain unchanged.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
