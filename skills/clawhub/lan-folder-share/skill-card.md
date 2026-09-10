## Description:

Publishes a local folder as a LAN-accessible web knowledge share where users can browse and search Markdown, spreadsheet, HTML, image, video, and audio files from a browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vesentanger](https://clawhub.ai/user/vesentanger)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, teams, and employees use this skill to share a narrowly scoped local documentation or report folder with trusted colleagues on the same LAN. It is suited for lightweight knowledge sharing where browser access and refresh-based updates are enough, and not for sensitive content requiring authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The LAN HTTP server has no authentication, so any reachable device on the network can browse the selected folder.

Mitigation: Use only a narrowly scoped folder containing files intentionally meant for LAN-wide access, and do not share home directories, repositories, credentials, internal reports, or personal data.

Risk: The server may expose more local content than expected if folder contents, symlinks, or self-contained assets are not reviewed before launch.

Mitigation: Review the target folder before deployment, avoid folders containing symlinks or untrusted self-contained assets, and do not treat tree or search exclusions as a security boundary.

Risk: A LAN share can become publicly reachable if the address is forwarded or exposed through an untrusted network.

Mitigation: Keep the service on trusted private networks, avoid public forwarding, and allow firewall access only for private networks where applicable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/vesentanger/skills/lan-folder-share)
- [SkillHub Listing Template](references/skillhub-listing.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and deployment parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to confirm the shared folder, site name, and port before starting a local Node.js LAN server.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
