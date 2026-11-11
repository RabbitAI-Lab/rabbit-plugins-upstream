## Description:

Helps video editors find downloadable footage, music, sound effects, and design assets, check their stated licenses, and record credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Video editors and creators use the skill to find accessible media and design assets for an edit, check each asset's stated license, and prepare credits where needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious with medium confidence, citing unpinned installation commands and reported behavior outside the asset-sourcing purpose; inspection was partial because two local references could not be resolved.

Mitigation: Review unpinned installation commands and the packages they may download, decide whether the reference-study workflows fit the task, and keep confidential project terms out of external search queries.

## Reference(s):

- [Skill repository page (declared homepage)](https://github.com/vargHQ/skills/tree/main/video-asset-sources)
- [ClawHub release page](https://clawhub.ai/vargai/skills/video-asset-sources)
- [Every source tested](artifact/references/all-sources.md)
- [Tested queries](artifact/references/tested-queries.md)
- [Traps and dead ends](artifact/references/traps.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and shell commands, with downloaded media assets and a JSON credits file as applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asset choice and licensing depend on the selected source; credit details are recorded when required.]

## Skill Version(s):

1.0.3 (source: server-resolved release version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
