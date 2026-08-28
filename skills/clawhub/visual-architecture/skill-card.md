## Description:

Create deterministic, local-first architecture artifacts from typed JSON or language-aware repo extraction: validate specs, render SVG/HTML diagrams, and emit source-backed receipts agents can cite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leostehlik](https://clawhub.ai/user/leostehlik)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to create reviewable system maps, agent workflows, sequence diagrams, data-flow diagrams, lifecycle diagrams, repository evidence maps, and PR delta review sketches from local JSON specs or repository extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks an agent to run a bundled local Python renderer, read repository files, run git diff for PR maps, and write diagram and receipt files.

Mitigation: Install only when that local access is acceptable for the target project, and run it in a workspace where generated files and repository reads are expected.

Risk: Generated diagrams may be mistaken for source-backed architecture evidence when receipts show incomplete or false source backing.

Mitigation: Review generated receipts before citing artifacts, especially examples where sourceBacked is false or node and edge evidence is incomplete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/leostehlik/skills/visual-architecture)
- [Visual Architecture gallery](https://leostehlik.github.io/visual-architecture/)
- [README](README.md)
- [Diagnostics](docs/diagnostics.md)
- [Repo-Aware Generation](docs/repo-aware-generation.md)
- [Harness Notes](docs/harnesses.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON specs and shell command blocks; generated artifacts may include SVG, self-contained HTML, share-card SVG, and JSON receipts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are local and deterministic when produced through the bundled renderer; receipts include hashes, validation status, metrics, warnings, and evidence quality signals.]

## Skill Version(s):

1.6.0 (source: SKILL.md frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
