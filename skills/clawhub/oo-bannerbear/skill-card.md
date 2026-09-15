## Description:

Enables an agent to operate Bannerbear through an OOMOL-connected account for template inspection, synchronous image creation, project authentication checks, and image or template retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Bannerbear actions from an agent through an already connected OOMOL account, including listing templates, creating images from templates, retrieving images or templates, and checking API key access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer one-liners from the internet.

Mitigation: Review the installer path before use; prefer an official package manager, versioned download, and checksum or signature verification before installation.

Risk: Bannerbear write actions can create generated media and change service state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Bannerbear skill page](https://clawhub.ai/oomol/skills/oo-bannerbear)
- [Bannerbear homepage](https://www.bannerbear.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON and include returned data plus an execution id when actions run.]

## Skill Version(s):

1.0.2 (source: evidence.json release.version and artifact frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
