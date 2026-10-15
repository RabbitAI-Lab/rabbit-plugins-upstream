## Description:

Connects an agent to Google Contacts and the People API for contact management, Workspace directory searches, profiles, and reporting relationships.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People using an agent with an authorized Google account can look up and manage personal contacts, search the Workspace directory, and retrieve profiles and organizational relationships.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact deletion and duplicate-merging actions may run without enforced user confirmation.

Mitigation: Keep write access disabled on shared or autonomous-agent hosts until deletion and deduplication require explicit confirmation; review actions before enabling writes.

Risk: The agent may access or change contacts in an authorized Google account.

Mitigation: Use GOG_READONLY=1 for lookup-only use and restrict OAuth scopes and the configured account.

## Reference(s):

- [gogcli documentation](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Text and JSON returned through agent tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain personal contacts and Workspace directory information.]

## Skill Version(s):

4.8.0 (source: ClawHub release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
