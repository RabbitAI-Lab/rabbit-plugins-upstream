## Description:

Helps teams compare prompt files, record version differences and effect scores, and track prompt changes in a local registry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to compare two prompt files, record their differences with an optional effect score, and maintain a local version history for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documented access gates, owner binding, and rollback protections are not implemented by the bundled CLI.

Mitigation: Treat it as a local diff-and-registry helper; require separate access controls and human approval before replacing or restoring an active prompt.

Risk: Registry writes may affect existing prompt history or expose recorded prompt changes.

Mitigation: Specify the registry path explicitly, protect the stored records, and keep backups before use on shared or production prompts.

## Reference(s):

- [Prompt Version Control on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-version-control)
- [LGD theory reference](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON summary, with a local JSON version registry]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records prompt-file differences and an optional effect score; the registry is written locally.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata; bundled skill frontmatter says 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
