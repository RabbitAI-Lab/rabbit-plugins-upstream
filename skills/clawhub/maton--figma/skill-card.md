## Description:

Helps agents inspect Figma design files, nodes, versions, comments, and design-system assets, render images, and manage comments through a user-authorized connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and other authorized users can ask an agent to inspect a supplied Figma file, export node images, review design-system assets, and manage file comments with approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing a connection grants access to Figma content within the connected account's permissions.

Mitigation: Get the user's approval before connecting; select only needed scopes and revoke unused connections.

Risk: Comments or other writes can affect shared files and notify collaborators.

Mitigation: Confirm the target and exact change with the user before every write or deletion.

Risk: Hosted functions, triggers, or destinations can continuously process or forward connected-app data.

Mitigation: Review and obtain explicit approval for hosted code, triggers, destinations, and any data transfer; restrict connections and network access.

## Reference(s):

- [Figma skill release on ClawHub](https://clawhub.ai/maton/skills/figma)
- [Maton](https://maton.ai)
- [Time trigger reference for optional scheduled automation](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Code, Guidance]

**Output Format:** [Markdown with API examples and command snippets; Figma data or image links when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Figma file URL and an authorized Maton connection; rendered image links expire.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
