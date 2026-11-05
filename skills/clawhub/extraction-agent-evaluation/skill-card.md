## Description:

Design evidence-backed structured extraction workflows and evaluate field truth, grounding, record completeness and matching errors. Use for extraction schemas, agent evaluation and source-drift plans rather than source discovery or a whole dataset purchasing decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redrookai](https://clawhub.ai/user/redrookai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to define structured extraction tasks and evaluate agent outputs against source-checked labels. It helps assess record completeness, field correctness, source support, matching errors, and source drift; an optional Python helper scores a narrow flat-record JSON format.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A schema-valid extraction can still contain unsupported facts, incorrect matches, or omitted records.

Mitigation: Evaluate field correctness, source support, record completeness, and identity matching separately against source-checked labels.

Risk: The optional scorer checks source-pointer consistency but does not determine whether the cited source supports a fact.

Mitigation: Use a stronger source check where the material requires it, and review facts against the correct entity and source version.

## Reference(s):

- [ClawHub release](https://clawhub.ai/redrookai/skills/extraction-agent-evaluation)
- [Worked example: trials at facilities](artifact/references/example.md)
- [Practice: design the extraction and its test](artifact/references/practice.md)
- [Flat-record scoring helper](artifact/scripts/score_flat_records.py)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Code]

**Output Format:** [Markdown guidance, extraction and evaluation schemas, and optional JSON scoring results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional scorer supports a fixed flat-record schema; source-pointer consistency does not establish semantic entailment.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
