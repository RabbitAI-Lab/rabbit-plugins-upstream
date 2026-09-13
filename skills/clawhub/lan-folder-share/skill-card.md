## Description:

Publishes a selected local folder as an unauthenticated LAN web knowledge base for browsing and searching Markdown documents, spreadsheets, HTML reports, images, and media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vesentanger](https://clawhub.ai/user/vesentanger)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to publish a tightly scoped local folder as a browser-accessible LAN knowledge base for shared documents, reports, spreadsheets, and media without a database or pre-generated site files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated LAN access can expose every browsable file in the selected folder to reachable devices on the network.

Mitigation: Confirm the sharing scope before startup and use only a tightly scoped folder containing files intended for LAN-wide sharing.

Risk: Folder selection, exclusions, or symlinks may expose more files than the user expects.

Mitigation: Avoid home directories, repositories, credential folders, private reports, and folders containing symlinks; review the selected path and exclusions before sharing.

Risk: Shared HTML files are executable browser content for viewers.

Mitigation: Share only trusted HTML reports and treat rendered HTML as active content.

Risk: Forwarding the LAN server to public or untrusted networks increases exposure.

Mitigation: Keep the service on a trusted private LAN, do not port-forward it, and restrict firewall approval to private networks where applicable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vesentanger/skills/lan-folder-share)
- [Artifact README](artifact/README.md)
- [SkillHub listing reference](artifact/references/skillhub-listing.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and LAN URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local and LAN HTTP URLs after the Node.js server starts.]

## Skill Version(s):

1.0.10 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
