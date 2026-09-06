## Description:

Batch deep-reading helper for local qwen3.5:4b document corpora via a DSH task bridge, producing structured markdown summaries and consolidated doubt lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and knowledge-base maintainers use this skill to batch process local document collections through a DSH inbox/outbox workflow and recover per-document markdown summaries with doubt lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recovery workflow writes markdown summaries to a user-selected output directory and matching summary filenames can be overwritten.

Mitigation: Use a dedicated output directory and avoid pointing --outdir at locations containing summary files that must be preserved.

Risk: The workflow reads and writes DSH inbox, outbox, hub, names, and output paths supplied at runtime.

Mitigation: Point --inbox, --outbox, --hub, --names, and --outdir only at directories and files you control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/medxpert-l1-batch-study)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, JSON task files, and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes per-document summary files and retry task files in user-specified local directories.]

## Skill Version(s):

1.1.0 (source: evidence.release.version, artifact frontmatter, artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
