## Description:

Autobound helps agents search, read, and enrich Autobound company and contact data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Autobound action schemas, search and enrich companies or contacts, and retrieve account and signal metadata through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can ask an agent to run remote installer scripts for the oo CLI.

Mitigation: Install or verify the oo CLI through a trusted method before using the skill; do not let an agent execute curl-to-bash or irm-to-iex install commands without review.

Risk: Authentication, Autobound connection, billing, or credit-impacting steps can affect account access or costs.

Mitigation: Have the user confirm login, connection, and billing actions directly before retrying workflows that require them.

## Reference(s):

- [Autobound ClawHub skill page](https://clawhub.ai/oomol/skills/oo-autobound)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Autobound homepage](https://www.autobound.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live oo connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
