## Description:

A structured knowledge graph acting as a cognitive lens for AI agents. Enables paradox resolution, analysis of open questions, and high-complexity future forecasting based on Beckmann Logic, Predictive Brain Theory, and simulation models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[matthiasbeckmann987-spec](https://clawhub.ai/user/matthiasbeckmann987-spec)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to help an agent reason over an opinionated knowledge graph for paradox resolution, open scientific or philosophical questions, AI-safety analysis, and high-complexity forecasting. Outputs should preserve uncertainty labels and distinguish established, hypothesis, metaphorical, and philosophical graph content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The graph contains speculative philosophical, forecasting, stock-trading, and AI-safety claims that may be mistaken for established fact.

Mitigation: Label outputs with the graph's scientific_status values, present uncertain content as hypotheses or metaphors, and require independent verification for empirical, financial, safety, or operational decisions.

Risk: Persuasion, manipulation, and expectation-management examples could be misused to steer people without transparency.

Mitigation: Use those parts only for analysis, defense, or consent-based explanation, and avoid producing manipulative instructions or covert persuasion strategies.

Risk: The large, opinionated graph can overfit answers to its internal framework or obscure simpler evidence-based responses.

Mitigation: Use the skill only for appropriate high-complexity, paradox, forecasting, or AI-safety questions; include confidence and limits, and prefer external evidence when the user asks for factual or actionable guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/matthiasbeckmann987-spec/skills/beckmann-knowledge-graph)
- [README](artifact/README.md)
- [CHANGELOG](artifact/CHANGELOG.md)
- [Knowledge graph](artifact/graph.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured text with graph-node references, argument paths, confidence notes, and limits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses graph scientific_status values to weight claims; does not require executable install behavior.]

## Skill Version(s):

3.1.0 (source: CHANGELOG.md and package.json, released 2026-08-31)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
