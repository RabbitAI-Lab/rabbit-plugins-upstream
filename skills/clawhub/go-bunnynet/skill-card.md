## Description:

Guides Go developers in using an unofficial client for Bunny.net core APIs, including CDN, DNS, storage configuration, statistics, and billing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to write Go code for Bunny.net core account APIs and handle authentication, responses, and account changes safely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An account API key could be exposed in generated code or logs.

Mitigation: Load BUNNYNET_API_KEY from the environment; never hardcode or log it.

Risk: Account-changing calls could modify or delete resources, purge caches, rotate keys, or affect billing and account settings.

Mitigation: Review the generated code and confirm each mutation before running it against a real account.

## Reference(s):

- [go-bunnynet setup and reference](references/setup.md)
- [go-bunnynet project homepage](https://github.com/psyb0t/go-bunnynet)
- [go-bunnynet ClawHub release](https://clawhub.ai/psyb0t/skills/go-bunnynet)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not cover storage file transfers or the separate Stream API.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
