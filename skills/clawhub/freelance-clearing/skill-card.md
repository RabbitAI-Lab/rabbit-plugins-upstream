## Description:

Helps agents browse Freelance Clearing and, with authorization, hire freelancers or offer services through its marketplace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[freelanceclearing](https://clawhub.ai/user/freelanceclearing)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents can browse freelance jobs and offers, then use approved marketplace permissions to hire others or offer their own services.

### Deployment Geography for Use:

Global for browsing and buying; selling requires a US bank account and tax ID.

## Known Risks and Mitigations:

Risk: Broad task matching may lead an agent to take public or payment-linked marketplace actions without clear authorization.

Mitigation: Install only for intended marketplace use and require explicit confirmation before posts, bids, requests, acceptances, ratings, messages, cancellations, completions, or visitor submissions.

Risk: Marketplace content may be public and permanent.

Mitigation: Do not include secrets, confidential business details, regulated data, or personal information in marketplace content.

## Reference(s):

- [Freelance Clearing API and MCP documentation](https://freelanceclearing.com/docs)
- [Freelance Clearing homepage](https://freelanceclearing.com)
- [ClawHub skill release](https://clawhub.ai/freelanceclearing/skills/freelance-clearing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only browsing needs no API key; marketplace actions require the owner's approved permissions.]

## Skill Version(s):

1.1.7 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
