## Description:

Verify LaTeX formulas with a multi-layer cross-validation workflow covering SymPy roundtrip checks, Wolfram CAS comparison when available, dimensional consistency, single-formula verification, batch verification, and LaTeX report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diamond2nv](https://clawhub.ai/user/diamond2nv)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, engineers, physics modelers, and developer agents use this skill to verify LaTeX formulas before publication or code implementation. It helps run syntax, algebraic, CAS, and dimensional checks and produce reproducible LaTeX verification reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to run a local CLI with shell, file, and network access.

Mitigation: Install and run it only in environments where local file, shell, and network access are acceptable, and pin the package version for automated or sensitive workflows.

Risk: Optional package extras expand behavior beyond the formula-verification path, including Zotero, LLM, graph, and NLP features.

Mitigation: Use only the core verification commands unless those broader features are explicitly needed.

Risk: CAS cross-validation depends on Wolfram Engine availability and can skip that layer when wolframscript is not installed.

Mitigation: Check verbose output for skipped CAS validation and rely on the remaining syntax, SymPy roundtrip, and dimensional checks when Wolfram is unavailable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/diamond2nv/skills/hfpclawer-formula-verify)
- [hfpapers-crawler Repository](https://github.com/diamond2nv/hfpapers-crawler)
- [hfpclawer PyPI Package](https://pypi.org/project/hfpclawer/)
- [Wolfram Engine](https://www.wolfram.com/engine/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Files]

**Output Format:** [Markdown guidance with shell commands, YAML configuration snippets, CLI output expectations, and LaTeX report file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent through local CLI workflows that may read and write formula registries, configuration files, and LaTeX report files.]

## Skill Version(s):

0.19.3 (source: server release; artifact frontmatter says 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
