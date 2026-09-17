## Description:

Bannerbear lets agents operate Bannerbear through the OOMOL-connected oo CLI, including schema inspection, image creation, template listing, template retrieval, image retrieval, and access checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Bannerbear through an OOMOL-connected account, including creating images from templates, retrieving images and templates, listing project templates, and verifying API key access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask the agent to run remote installer scripts for the oo CLI.

Mitigation: Review the install step before use, prefer a verified package manager or download-then-inspect process, and avoid running installers with administrator or root privileges.

Risk: The create_image_sync action changes Bannerbear project state by creating images.

Mitigation: Confirm the exact payload and intended effect with the user before allowing Bannerbear write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-bannerbear)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [Bannerbear Homepage](https://www.bannerbear.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill inspects live action schemas before constructing requests and returns Bannerbear action responses through the oo CLI.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
