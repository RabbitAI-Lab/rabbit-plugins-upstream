## Description:

Audience-first resonance diagnosis for content drafts, viral-post analysis, and hunch-to-public-question framing, with each judgment tied to source text as evidence, inference, or to-verify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content strategists use this skill to diagnose whether a draft gives the audience a clear takeaway and action impulse, decode why a benchmark post resonated, or turn a vague hunch into a public question. The skill is aimed at single-person knowledge creators who need concrete editorial judgment without jargon.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared or long-term memory may influence analysis or retain user-derived content judgments.

Mitigation: Review before installing in shared-memory environments, use only where persistent memory is acceptable, and periodically inspect or clear stored resonance judgments.

Risk: Audience reactions and viral-content explanations can be speculative if treated as facts.

Mitigation: Keep the skill's evidence, inference, and to-verify labels visible, and validate important claims with audience data such as comments, saves, shares, or retention signals before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-resonate)
- [Evaluation README](evals/README.md)
- [Sample evaluation result](evals/results/sample-01-v0.2.0.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown diagnostic report with quoted source text, inference labels, confidence notes, and validation prompts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use shared or long-term memory when available; no API keys or MCP tool references were detected in the provided evidence.]

## Skill Version(s):

0.2.6 (source: ClawHub release metadata; artifact frontmatter declares 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
