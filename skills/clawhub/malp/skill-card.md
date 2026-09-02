## Description:

Project context tracker that helps agents discover, open, create, refresh, classify, retire, and promote `.malp/` directories for project-local working context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[inertia186](https://clawhub.ai/user/inertia186)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use MALP to maintain project-local context notes, scout which context to load, and manage active, attic, and unindexed `.malp/` workspaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or edit local `.malp/` directories and `~/.malp-home/` maps.

Mitigation: Only create, refresh, classify, retire, or delete MALP context for an explicitly requested target, and use scoped approval when the environment requires it.

Risk: Project context notes may capture sensitive or personal working information if used carelessly.

Mitigation: Avoid storing secrets in `.malp/` notes and consider ignoring `.malp/` in git when the notes are personal.

Risk: Kino scouting and git-history recommendations are heuristic and may be incomplete or stale.

Mitigation: Treat Kino output as provisional and verify recommendations against direct project evidence before acting.

## Reference(s):

- [MALP Operational Tasks](references/tasks.md)
- [MALP Indexing States](references/indexing.md)
- [MALP Attic](references/attic.md)
- [Clawpatch-aware MALP Work](references/clawpatch.md)
- [Repo Strategies for `.malp/`](references/repo-strategies.md)
- [MALP Style Notes](references/style.md)
- [Stargate M.A.L.P. Reference](references/stargate-malp-kino.md)
- [Kino Scout Script](scripts/kino.py)
- [Mobile Analytic Laboratory Probe](https://stargate.fandom.com/wiki/Mobile_Analytic_Laboratory_Probe)
- [Kino](https://stargate.fandom.com/wiki/Kino)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text and Markdown-style notes with inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update `.malp/` project context files and `~/.malp-home/` maps when requested.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
