## Description:

Laravel Cloud (cloud.laravel.com). Use this skill for Laravel Cloud requests that search and read account data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Laravel Cloud organizations, applications, environments, deployments, and available regions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path may execute installer scripts downloaded from the internet.

Mitigation: Review the setup path before installing and prefer a pinned, inspectable, signed, or package-manager-based oo CLI installation method.

Risk: The connector can read Laravel Cloud account data through the connected OOMOL account.

Mitigation: Use the skill only with the intended connected account and require explicit confirmation before any future write or destructive connector actions.

## Reference(s):

- [Laravel Cloud Skill Page](https://clawhub.ai/oomol/skills/oo-laravel-cloud)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Laravel Cloud Homepage](https://cloud.laravel.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
