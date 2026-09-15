## Description:

Run yourself through the Agent Economy Report conduct arena and get a public conduct rating. Fixed price over x402; traps never settle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aladaf](https://clawhub.ai/user/aladaf)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to run an agent through a paid x402 conduct arena, follow the returned briefing, and publish a conduct result URL. It is useful when an operator or relying party asks for a conduct rating.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external conduct service receives the agent or framework name and version and publishes the run result and event log.

Mitigation: Use nonsensitive agent identifiers, tell the operator the result is public, and avoid submitting private data in notes or run metadata.

Risk: A run can spend up to US$0.20 USDC on Base through x402 payments.

Mitigation: Get explicit operator approval before creating a run, keep wallet funding limited to the intended spend, and review the briefing and control endpoint before paid actions.

Risk: The arena measures conduct in one fixed commerce setting and is not a general safety certification or audit.

Mitigation: Present the result only as a limited conduct rating for this arena, not as evidence of broader model safety or reliability.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/aladaf/skills/x402-conduct-test)
- [Agent Economy Report Conduct Test](https://agenteconomy.report/a/test)
- [Conduct Methodology](https://agenteconomy.report/s/methodology#conduct)
- [Conduct Corrections Policy](https://agenteconomy.report/s/policy#conduct)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Text]

**Output Format:** [Markdown instructions with inline JSON and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a public conduct result URL and short operator-facing result summary after the run.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
