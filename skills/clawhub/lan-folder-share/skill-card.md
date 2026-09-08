## Description:

Publishes a chosen local folder as a LAN-accessible website for browsing and searching Markdown, spreadsheets, HTML reports, images, video, and related files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vesentanger](https://clawhub.ai/user/vesentanger)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to expose a narrowly scoped local folder as a LAN web link for team document browsing, preview, and search without setting up a database or pre-generated site.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The selected folder becomes readable by reachable devices on the local network without login.

Mitigation: Share only a narrow folder containing intended files, avoid home directories, repositories, credentials, and sensitive business data, and get explicit user confirmation before starting the server.

Risk: The content directory may be modified if the default README generation behavior is used.

Mitigation: Use the documented --no-readme option when the shared content directory must remain read-only.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vesentanger/skills/lan-folder-share)
- [SkillHub listing template](references/skillhub-listing.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and LAN URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and user confirmation before exposing a folder to reachable LAN devices.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
