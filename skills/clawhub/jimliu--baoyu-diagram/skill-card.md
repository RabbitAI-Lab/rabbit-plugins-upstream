## Description:

Create professional, dark-themed standalone SVG diagrams across architecture, flowchart, sequence, structural, mind map, timeline, state machine, data-flow, and conceptual formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimliu](https://clawhub.ai/user/jimliu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical writers, architects, and product teams use this skill to turn technical or conceptual material into polished diagrams for documentation, articles, and presentations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that the skill automatically runs an unpinned local runtime or converter and may fetch Bun through npm at runtime.

Mitigation: Install only where local command execution and runtime fetching are acceptable, and prefer a release that pins the runtime and dependencies.

Risk: The security scan reports an inconsistent SVG-only versus PNG output contract.

Mitigation: Review expected SVG and PNG outputs before relying on generated artifacts in a workflow, and prefer a release that documents PNG output in the manifest.

Risk: The security guidance calls for size limits before rasterizing SVGs.

Mitigation: Apply input size limits and review complex SVGs before conversion.

## Reference(s):

- [Baoyu Diagram ClawHub Skill Page](https://clawhub.ai/jimliu/skills/baoyu-diagram)
- [Architecture Diagram Layout](artifact/references/architecture.md)
- [Flowchart Layout](artifact/references/flowchart.md)
- [Sequence Diagram Layout](artifact/references/sequence.md)
- [Structural Diagram Layout](artifact/references/structural.md)

## Skill Output:

**Output Type(s):** [code, shell commands, guidance]

**Output Format:** [Standalone SVG file with optional @2x PNG conversion result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill writes self-contained SVG output and may invoke a local converter to produce a scaled PNG.]

## Skill Version(s):

1.117.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
