## Description:

Guides agents to pressure-test conventional answers by decomposing claims into bedrock facts, challenging inherited assumptions, and rebuilding a conclusion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deciqai](https://clawhub.ai/user/deciqai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and decision-makers use the skill to examine costly or hard-to-reverse choices, pressure-test claims grounded in convention, and produce a structured first-principles teardown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes a per-run third-party request that may retrieve mutable instructions; the security scan marked the skill suspicious and was partial because two referenced files were missing.

Mitigation: Review the retrieved instructions and the missing components before use; if stable behavior is required, rely only on the locally reviewed skill content.

## Reference(s):

- [Sources — first-principles](references/sources.md)
- [Aristotle's Logic — Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/aristotle-logic/)
- [Euclidean geometry — Encyclopaedia Britannica](https://www.britannica.com/science/Euclidean-geometry)
- [Llama models](https://www.llama.com/)
- [First Principles skill page](https://www.deciqai.com/c/first-principles)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown teardown with a claim, tagged assumptions, bedrock, reconstruction, convention diff, and confidence/open questions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.8 (source: target metadata and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
