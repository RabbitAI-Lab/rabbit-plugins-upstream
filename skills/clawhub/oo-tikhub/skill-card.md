## Description:

TikHub (tikhub.io). Use this skill for ANY TikHub request: searching, reading data, and invoking supported TikHub endpoints through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect TikHub connector schemas and retrieve TikHub endpoint, usage, pricing, account, or functional API data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad TikHub endpoint invocation can affect account data, API-key-related information, or paid usage when treated as routine read-only activity.

Mitigation: Before allowing invoke_endpoint, require the agent to show the endpoint, live schema, expected returned data, and likely credit or billing impact.

Risk: The skill can only operate through the user connected OOMOL/TikHub account.

Mitigation: Install or enable it only when agents are intended to use that connected account, and reconnect or adjust scopes only after an auth or scope error.

## Reference(s):

- [TikHub homepage](https://tikhub.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an OOMOL sign-in, a connected TikHub account, and applicable TikHub path scopes for account and usage actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
