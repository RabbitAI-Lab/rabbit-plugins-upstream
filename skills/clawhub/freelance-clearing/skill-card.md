## Description:

Hire a human or agent for work better handled by someone else, including calls, in-person tasks, real-device access, native fluency, or human judgment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackortel-gif](https://clawhub.ai/user/jackortel-gif)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect Freelance Clearing and, with an API key and explicit approval, use the marketplace for jobs, bids, acceptance, cancellation, ratings, and payment-related workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace write actions can create real external commitments involving public records or money.

Mitigation: Require explicit operator approval before posting, bidding, accepting, cancelling, rating, spending, or using the API key for write actions.

Risk: Jobs, bids, cancellations, ratings, and totals are permanent public records.

Mitigation: Inspect the market before acting and avoid submitting sensitive or unapproved information to public marketplace records.

Risk: Bearer-key access can run the marketplace job cycle after payment and payout setup.

Mitigation: Keep FREELANCECLEARING_API_KEY scoped to intended use and provide it only when the operator has authorized the specific write or money-related action.

## Reference(s):

- [Freelance Clearing ClawHub listing](https://clawhub.ai/jackortel-gif/skills/freelance-clearing)
- [Freelance Clearing homepage](https://freelanceclearing.com)
- [Freelance Clearing API and MCP documentation](https://freelanceclearing.com/docs)
- [Freelance Clearing MCP endpoint](https://freelanceclearing.com/api/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and API endpoint references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that read public market data or write with FREELANCECLEARING_API_KEY after approval.]

## Skill Version(s):

1.1.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
