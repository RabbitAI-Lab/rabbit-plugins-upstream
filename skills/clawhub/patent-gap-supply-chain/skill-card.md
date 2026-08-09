## Description:

Competitive intelligence workflow that infers supply-chain relationships from patent gaps using trade-secret assessment, patent quality scoring, negative verification, evidence freshness tracking, competitive triangulation, and financial cross-validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tianzhiceng297-boop](https://clawhub.ai/user/tianzhiceng297-boop)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, analysts, and developers use this skill to analyze technology, hardware, manufacturing, pharma, and materials supply chains, infer possible supplier or customer relationships from patent-ownership gaps, and produce confidence-scored reports with explicit caveats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation language can trigger supply-chain inference during generic company, stock, or industry research.

Mitigation: Confirm whether supplier or customer inference is desired, then scope the target company, technology, direction, and evidence standard before running the workflow.

Risk: Patent-gap analysis can produce misleading conclusions when trade secrets, stale evidence, negative evidence, or missing financial corroboration are not handled.

Mitigation: Apply the skill's mandatory trade-secret assessment, negative verification, evidence freshness rules, financial cross-validation, and confidence caps before presenting conclusions.

## Reference(s):

- [Detailed Workflow](references/workflow.md)
- [Checklists and Confidence Rules](references/checklists.md)
- [Industry-Specific Patent & Trade Secret Guide](references/industry-guide.md)
- [Sample Output](examples/sample-output.md)
- [Real Case Study](examples/real-case.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with tables, evidence chains, confidence ratings, and follow-up suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes direction, relationship determination, trade-secret assessment, patent quality, evidence freshness, triangulation, negative verification, financial corroboration, alternative hypotheses, and counter-intelligence flags.]

## Skill Version(s):

0.1.2 (source: server release metadata; artifact frontmatter and changelog state 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
