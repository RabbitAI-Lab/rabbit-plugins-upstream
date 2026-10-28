## Description:

Guides an agent to decompose claims, decisions, or assumptions to irreducible facts, then rebuild a concise first-principles analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deciqai](https://clawhub.ai/user/deciqai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to pressure-test expensive or hard-to-reverse decisions, inherited assumptions, business models, architecture choices, and AI cost claims by reducing them to citable or irreducible foundations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags that the skill tells agents to fetch and prefer mutable remote instructions at runtime.

Mitigation: Review before installing, and prefer operation where the installed SKILL.md is authoritative or update checks require explicit approval with version and hash verification.

Risk: First-principles analysis can produce misleading guidance if bedrock claims are asserted without citations or if inherited assumptions are not fully interrogated.

Mitigation: Require cited or irreducible bedrock facts, tagged assumptions, and an explicit reconstruction audit before using the output for high-impact decisions.

## Reference(s):

- [First Principles ClawHub Listing](https://clawhub.ai/deciqai/skills/first-principles)
- [Sources - first-principles](references/sources.md)
- [Wright Brothers and the Lift Tables (1901)](examples/wright-brothers-1901.md)
- [SpaceX and the Cost of a Rocket (2002-2008)](examples/spacex-rocket-cost-2002.md)
- [The Physics of AI Inference Cost (2024-2026)](examples/ai-inference-cost-physics-2024-2026.md)
- [Aristotle's Logic](https://plato.stanford.edu/entries/aristotle-logic/)
- [Euclidean Geometry](https://www.britannica.com/science/Euclidean-geometry)
- [Wright Brothers and the Invention of the Aerial Age](https://airandspace.si.edu/explore/stories/wright-brothers-and-invention-aerial-age)
- [Llama Models](https://www.llama.com/)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured teardown with claim, tagged assumptions, bedrock facts, reconstruction, changes, confidence, and open questions.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
