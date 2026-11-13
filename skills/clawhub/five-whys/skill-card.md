## Description:

Use for the 5 Whys, or when the user wants the root cause of a failure: "why did this happen?", "this keeps breaking", "write the postmortem", "find the real cause". Asks why repeatedly with evidence at each step, then sets countermeasures. Skip for one-off typos or when the cause is already proven.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ysskrishna](https://clawhub.ai/user/ysskrishna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and incident responders use this skill to trace recurring failures or incidents to a changeable root cause, check each causal link against evidence, and define countermeasures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because Skillspector could not resolve a local reference, so the benign verdict does not cover a complete review.

Mitigation: Review the supplied skill and its local reference before relying on the scan result.

Risk: A plausible causal explanation could be mistaken for an established finding.

Mitigation: Label each link verified or hypothesis, cite supporting evidence, and use the reverse test before summarizing the root cause.

## Reference(s):

- [ClawHub five-whys release](https://clawhub.ai/ysskrishna/skills/five-whys)
- [Worked example](references/example.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with a causal chain table, evidence labels, and countermeasures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May distinguish verified findings from hypotheses and include evidence references.]

## Skill Version(s):

2026.11.11 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
