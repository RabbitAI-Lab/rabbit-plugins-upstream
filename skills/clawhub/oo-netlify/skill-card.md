## Description:

Netlify enables agents to read, create, update, and delete Netlify data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Netlify sites, builds, deploys, forms, submissions, accounts, and users through a connected OOMOL account. It supports read operations and clearly marked write or destructive Netlify actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The one-time oo CLI installation command downloads and executes an installer.

Mitigation: Install the oo CLI only from a trusted source, and prefer a verified installer if one is available.

Risk: The connected Netlify account can perform write or destructive actions such as creating sites, cancelling deploys, or deleting submissions.

Mitigation: Review the exact site, deploy, submission, and JSON payload before approving write or destructive actions.

## Reference(s):

- [ClawHub Netlify skill page](https://clawhub.ai/oomol/skills/oo-netlify)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Netlify homepage](https://www.netlify.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the oo CLI and may return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
