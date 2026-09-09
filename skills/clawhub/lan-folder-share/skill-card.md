## Description:

Publishes a selected local folder as a LAN-accessible web site where colleagues can browse and search Markdown documents, Excel/CSV sheets, HTML reports, images, and video without a database or pre-configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vesentanger](https://clawhub.ai/user/vesentanger)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operations staff, and team members use this skill to turn a scoped local directory into a browser-accessible LAN document and media share. It is best suited for trusted local-network sharing of intended files, not sensitive folders or public internet exposure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The selected folder can be exposed to every reachable device on the LAN without authentication.

Mitigation: Use only a dedicated folder containing files intentionally prepared for LAN sharing, and avoid home directories, repositories, credential folders, and sensitive business data.

Risk: The skill may write a default README.md into the shared content directory.

Mitigation: Use --no-readme when the content directory must remain read-only or when generated files are not acceptable.

Risk: The README includes curl-to-bash install guidance for SkillHub tooling.

Mitigation: Do not follow the installer command unless the installer source has been independently trusted and verified.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/vesentanger/skills/lan-folder-share)
- [SkillHub Listing Template](references/skillhub-listing.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with shell commands and deployment parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js; produces LAN and localhost URLs when the server starts.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
