## Description:

Map an unfamiliar repository, select task-relevant implementation and verification paths, and build a code-cited context pack for planning, debugging, review, or handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use Nexus to map unfamiliar repositories, focus investigation on task-relevant code paths, and prepare a cited context pack for planning, debugging, review, or handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository maps and context packs can reveal sensitive project names, file paths, symbols, or private source details if shared without review.

Mitigation: Use an authorized repository and private output directory, then review generated maps, source manifests, and context packs before disclosure.

Risk: Installing or running the skill from an untrusted source or unresolved package version can expose the agent workflow to unexpected instructions or code.

Mitigation: Install only from a trusted source and revision; prefer a verified git clone route or confirm the resolved package and version before use.

Risk: The mapper reduces secret exposure but is not a complete secret scanner or sandbox for hostile or changing filesystems.

Mitigation: Keep the mapped repository scope explicit, use task-specific exclusions where needed, avoid mapping sensitive stores, and treat scanner output as a disclosure aid rather than proof of safety.

## Reference(s):

- [Nexus ClawHub skill page](https://clawhub.ai/antreasantoniou/skills/nexus)
- [Context pack template](references/context-pack-template.md)
- [Security policy](SECURITY.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown context pack with code citations and supporting shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces context-pack.md, directory-map.md, and sources.txt in a user-selected destination; the mapper writes a new owner-only map file and does not overwrite existing outputs.]

## Skill Version(s):

1.0.0 (source: changelog, released 2026-09-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
