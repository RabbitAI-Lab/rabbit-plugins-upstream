## Description:

Magnific (Freepik) lets an agent search Freepik stock images and templates, retrieve resource metadata, and create resource download URLs through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Magnific (Freepik) from an agent workflow when they need to search resources, inspect resource details, or generate download URLs through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include internet-downloaded installer scripts that could run arbitrary code.

Mitigation: Review and verify the oo CLI installation method before use, and avoid running the installer from an elevated shell.

Risk: Skill use routes requests through an OOMOL-connected Freepik account and may depend on account scopes, credentials, billing, or credits.

Mitigation: Confirm the connected account, scopes, and billing posture before issuing actions that generate download URLs or consume credits.

## Reference(s):

- [Magnific (Freepik) Skill Page](https://clawhub.ai/oomol/skills/oo-freepik)
- [Magnific (Freepik) Homepage](https://www.magnific.com/freepik)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON containing data and meta.executionId values from OOMOL-connected Freepik actions.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
