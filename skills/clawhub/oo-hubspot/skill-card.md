## Description:

HubSpot (hubspot.com). Use this skill for ANY HubSpot request -- reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate HubSpot through an OOMOL-connected account, including reading CRM data, creating or updating contacts, companies, and deals, inspecting properties, and retrieving campaign analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path can run an unverified remote installer for the required oo CLI.

Mitigation: Prefer a verified, pinned, or package-manager installation source, and review the installer payload before executing setup commands.

Risk: Write actions can create or update HubSpot CRM records and activities.

Mitigation: Inspect the live action schema, construct the exact JSON payload, and confirm the payload and expected effect with the user before running write actions.

Risk: Commands run against the user's connected HubSpot account and can access account-specific CRM data.

Mitigation: Use read/list/search actions narrowly, request only needed fields, and verify the connected account context before sensitive operations.

## Reference(s):

- [HubSpot homepage](https://www.hubspot.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect action schemas before running HubSpot connector actions; command responses are JSON.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
