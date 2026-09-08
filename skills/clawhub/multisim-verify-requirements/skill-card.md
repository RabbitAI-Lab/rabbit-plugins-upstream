## Description:

Translates circuit design requirements into measurable criteria and reports PASS, FAIL, or unverified results from Multisim experiment data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yxy050208](https://clawhub.ai/user/yxy050208)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn Multisim design requirements into explicit measurable checks, run the verification tool, and summarize evidence-backed pass, fail, and unverified outcomes. It is suited for acceptance testing, tolerance checks, and design review where existing simulation data must support each conclusion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required Multisim MCP tools may be unavailable or not connected in the user's agent harness.

Mitigation: Confirm the intended Multisim MCP tools are available before installing or using the skill.

Risk: Proposed reruns or circuit changes could alter experiments or circuits if approved without review.

Mitigation: Review any rerun or modification plan before approving changes to experiments or circuits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yxy050208/skills/multisim-verify-requirements)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown summary with measurable criteria, observed values, targets, tolerances, statuses, evidence, counts, and minimal rerun recommendations when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves unverified tool outcomes and does not automatically overwrite experiments or modify circuits without user approval.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
