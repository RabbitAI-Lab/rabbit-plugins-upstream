## Description:

Benchmarks Rotifer Genes in the Arena and produces a Markdown comparison report with fitness scores, security grades, and upgrade guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to compare Rotifer Genes, including Genes imported from ClawHub, and review Arena rankings, security grades, and potential upgrade paths. It is not intended for general AI benchmarking or load testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the Rotifer CLI reads project Genes and Agent definitions, writes local evaluation artifacts, and contacts public Rotifer services.

Mitigation: Use it only in projects where those operations are acceptable; review the proposed commands and preserve approval before publishing, overwriting, or saving reports.

Risk: Fetching @rotifer/playground through npx executes a third-party npm package.

Mitigation: Review the npm package provenance before running npx and approve installation explicitly.

Risk: Cross-fidelity fitness gaps can reflect the scoring model rather than capability differences.

Mitigation: Prefer same-fidelity comparisons and explain any cross-fidelity scoring caveat in the report.

## Reference(s):

- [Rotifer Arena ClawHub release](https://clawhub.ai/xiaoba-dev/skills/rotifer-arena)
- [Rotifer documentation](https://rotifer.dev/docs)
- [Rotifer Protocol specification](https://github.com/rotifer-protocol/rotifer-spec)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with comparison tables and reproduction commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include F(g) fitness, V(g) security grades when available, fidelity comparisons, and upgrade guidance; saving the report to a file requires approval.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata and bundled manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
