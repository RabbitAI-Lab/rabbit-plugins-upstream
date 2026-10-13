## Description:

Checks whether specific job postings and product listings are still available, and supports one-shot page conditions, URL watchers, and submission confirmations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[moyecj-snap](https://clawhub.ai/user/moyecj-snap)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to check specific job or product URLs before applying, contacting employers, or recommending items; they can also monitor page changes and verify completed submissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned payment-capable npm CLI may introduce supply-chain risk.

Mitigation: Use a pinned, reviewed AgentCash CLI version and avoid global installation in sensitive environments.

Risk: Paid URL checks and long-running watchers can incur USDC charges.

Mitigation: Get explicit confirmation before paid batch checks or 30-day watchers.

Risk: Checking a URL sends that URL to the Livecheck service.

Mitigation: Send target URLs only when sharing them with livecheck.fly.dev is acceptable.

## Reference(s):

- [Livecheck on ClawHub](https://clawhub.ai/moyecj-snap/skills/livecheck)
- [Getting Started](rules/getting-started.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Interprets availability as live, closed, or unknown; may report page signals and confirmation receipts.]

## Skill Version(s):

4.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
