## Description:

Searches recent top-tier Agentic AI conference and journal research, filters papers through an H=(E,T,C,S,L,V)+P lens, and produces a readable literature review with an optional confirmed local wiki compilation step.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and technical readers use this skill to gather and summarize recent Agentic AI literature for a chosen subfield. It can optionally organize the generated review into a project-local wiki after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional wiki compilation writes generated files to disk.

Mitigation: Proceed only after reviewing the confirmation prompt, including the absolute raw and wiki paths, and keep the wiki root inside the current project.

Risk: Literature reviews can include incomplete or misleading paper selections if search coverage is insufficient.

Mitigation: Use the skill's disclosed search log, coverage checklist, and paper-count thresholds to review whether the output is adequately supported.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/neuhanli/skills/agentic-ai-research)
- [wiki-creator README](wiki-creator/README.md)
- [schema-guide.md](wiki-creator/references/schema-guide.md)
- [page-authoring.md](wiki-creator/references/page-authoring.md)
- [query-mode.md](wiki-creator/references/query-mode.md)
- [cascade-update.md](wiki-creator/references/cascade-update.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown literature review, optional local wiki files, and concise execution guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary deliverable is a human-readable literature review; optional wiki output is project-local and gated by explicit confirmation.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
