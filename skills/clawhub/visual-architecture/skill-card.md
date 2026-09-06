## Description:

Create deterministic, local-first architecture artifacts from typed JSON or TypeScript-aware repo extraction: validate specs, render SVG/HTML diagrams, and emit source-backed receipts agents can cite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leostehlik](https://clawhub.ai/user/leostehlik)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to create reviewable architecture, workflow, sequence, data-flow, lifecycle, repo-evidence, and PR-delta diagrams from typed JSON specs or local repository extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated architecture artifacts may include private paths, hostnames, tokens, customer details, or internal architecture from the inspected repository.

Mitigation: Review generated HTML, SVG, JSON, receipts, and gallery files before publishing or sharing them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/leostehlik/skills/visual-architecture)
- [Visual Gallery](https://leostehlik.github.io/visual-architecture/)
- [Repo-Aware Generation](docs/repo-aware-generation.md)
- [Diagnostics](docs/diagnostics.md)
- [Public TypeScript Monorepo Case Study](docs/public-typescript-monorepo-case-study.md)
- [Harness Notes](docs/harnesses.md)

## Skill Output:

**Output Type(s):** [Files, JSON, HTML, SVG, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands plus JSON specs, SVG/HTML artifacts, share-card SVGs, and receipt JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local deterministic outputs; receipts include hashes, validation status, metrics, warnings, and evidence counts.]

## Skill Version(s):

1.8.0 (source: SKILL.md metadata, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
