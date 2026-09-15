## Description:

Guides an agent in using the OOMOL oo CLI to run DiscoLike connector actions for company discovery and business data retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and business teams use this skill to query DiscoLike through an OOMOL-connected account for company discovery, firmographic profiles, growth metrics, SSL certificate metrics, digital footprint scores, and usage counters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include remote installer commands that could be unsafe if run blindly.

Mitigation: Use an official install path that can be inspected and verified before running the connector.

Risk: The skill operates through a connected DiscoLike account and can access account-specific usage and billing counters.

Mitigation: Run only intended read actions after setup and inspect the live action schema before constructing each request.

## Reference(s):

- [DiscoLike homepage](https://discolike.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and an execution ID.]

## Skill Version(s):

1.0.3 (source: evidence.json release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
