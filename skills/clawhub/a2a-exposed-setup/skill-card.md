## Description:

Deploy or configure an a2a-exposed hosted agent or Cloudflare Worker, including its public A2A endpoint and wake delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to deploy and configure a public A2A endpoint for an agent, choose hosted or Cloudflare Worker hosting, and set up wake delivery and verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the skill suspicious because its setup uses changeable, unpinned tools and includes actions beyond its stated deployment purpose; the scan was partial.

Mitigation: Review the package version and requested actions before execution, pin a reviewed release when stable behavior is needed, and inspect unresolved references before relying on the complete workflow.

Risk: Deployment and teardown instructions can change account resources or delete infrastructure and data.

Mitigation: Use the setup checklist, obtain explicit human approval before account or infrastructure changes, and review dry-run output before uninstalling.

## Reference(s):

- [Setup checklist](references/checklist.md)
- [Prerequisites](references/prerequisites.md)
- [Deployment guide](references/deploy.md)
- [Wake setup guide](references/wake.md)
- [Teardown guide](references/teardown.md)
- [Hosted A2A getting started](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Hosted service](https://a2a.exposed/hosted)
- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup checklists and verification steps.]

## Skill Version(s):

0.8.65 (source: frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
