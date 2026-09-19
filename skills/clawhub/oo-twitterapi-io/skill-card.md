## Description:

TwitterAPI.io helps agents run TwitterAPI.io connector actions for X/Twitter account, user, tweet, timeline, list, community, Space, trend, monitoring, and search workflows through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query and manage TwitterAPI.io-backed X/Twitter resources from an agent, including profiles, tweets, timelines, search, monitored users, and filter rules. It is suited to connector workflows where write and destructive actions require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote script execution for installing the oo CLI.

Mitigation: Review the install path before enabling the skill and prefer a pinned, verifiable oo CLI installation method when available.

Risk: The skill can run write and destructive TwitterAPI.io actions that change or remove monitoring and filter-rule state.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running actions tagged as write or destructive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-twitterapi-io)
- [TwitterAPI.io homepage](https://twitterapi.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
