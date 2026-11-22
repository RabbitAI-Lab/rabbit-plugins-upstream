## Description:

Look up what AI has actually done in mathematics, and how well each claim is evidenced, on qed.bot, a public register of AI claims on math problems (Erdős problems, Millennium problems, record bounds, formalised theorems). Each claim is graded for autonomy, evidence and fidelity, and cited Lean proofs are rebuilt rather than taken on report. Use when your owner asks whether AI solved a problem, how strong a claimed AI proof is, which open problems have AI work on them, who holds a record bound, how much an announcement disclosed, or wants a Lean proof file checked for sorry and nonstandard axioms, or wants to send the register a paper, a claim or a correction for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[logic](https://clawhub.ai/user/logic)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to research AI mathematics claims, understand how the register grades their evidence, check Lean proof files for incomplete declarations or nonstandard axioms, and submit missing claims or corrections for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The register's grades may be mistaken for a verdict that a mathematical proof is correct.

Mitigation: Present autonomy, evidence, and fidelity grades as assessments of the attached evidence, and state that the register does not rule on proof correctness.

Risk: The security review was incomplete because some referenced materials were not included in the scan.

Mitigation: Treat the scan as partial and review relevant linked materials before relying on behavior they describe.

Risk: A private or public proof check may incur a credit or USDC charge.

Mitigation: Use only an explicitly authorized payment method within its approved limit, and check whether a public result is already available before paying.

## Reference(s):

- [qed.bot public register](https://qed.bot)
- [qed.bot agent documentation](https://qed.bot/agents)
- [qed.bot MCP endpoint](https://qed.bot/mcp)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text, JSON]

**Output Format:** [Text, Markdown, or JSON summaries with cited records and evidence grades]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report registry grades as evidence grades; they are not verdicts on proof correctness.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
