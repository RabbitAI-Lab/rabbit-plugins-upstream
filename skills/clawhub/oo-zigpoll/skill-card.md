## Description:

Use this Zigpoll skill for requests that search or read survey, poll, participant, response, slide, account, and current-user data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Zigpoll through OOMOL, including listing accounts, polls, slides, participants, and responses, fetching user or poll details, and generating survey links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zigpoll participant and response data may contain sensitive survey information.

Mitigation: Use an OOMOL-connected Zigpoll account that is appropriate for the surveys the agent is expected to access.

Risk: Connector action payloads may be incorrect if constructed from stale assumptions.

Mitigation: Inspect the live Zigpoll action schema before running connector actions and match payloads to that schema.

## Reference(s):

- [ClawHub Zigpoll Skill](https://clawhub.ai/oomol/skills/oo-zigpoll)
- [Zigpoll Homepage](https://www.zigpoll.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Zigpoll connector schemas before constructing action payloads; command responses are JSON when run with --json.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
