## Description:

A short-video opening-hook specialist that first checks whether the content has enough substance, then diagnoses or generates concise opening candidates with rule-based rationale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content teams use this skill to improve the first seconds of short videos or X posts by checking source material, selecting hook directions, and refining candidates without overstating the underlying content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives mutable external vault and writing-framework files authority over its behavior.

Mitigation: Review and constrain the referenced vault and framework files before use, and run the skill only with trusted local writing resources.

Risk: The skill can save user feedback into persistent memory.

Mitigation: Require confirmation before memory or framework write-back and periodically audit saved feedback.

Risk: Opening hooks may become misleading if they promise more than the supplied content can support.

Mitigation: Keep the skill's gate check active and require generated hooks to match the evidence, claims, and examples present in the source material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-hook)
- [规则卡](artifact/references/规则卡.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with structured diagnostics, hook candidates, and concise rationale]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes gate checks, opening diagnostics, grouped hook candidates, and source-material cautions.]

## Skill Version(s):

0.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
