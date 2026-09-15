## Description:

Scrapfly (scrapfly.io) skill that lets an agent scrape public URLs and retrieve monitoring metrics through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to inspect Scrapfly action schemas, run scraping or monitoring actions through an OOMOL-connected account, and recover from setup, authentication, connection, credential, and billing errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts, which can execute unverified code on the user's machine.

Mitigation: Review the installer path before installing; prefer a pinned, verified, or platform-package-manager installation method and avoid running remote installer scripts directly with elevated privileges.

## Reference(s):

- [ClawHub Scrapfly skill page](https://clawhub.ai/oomol/skills/oo-scrapfly)
- [Scrapfly homepage](https://scrapfly.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, PowerShell, text, and JSON command examples; connector action results are returned as JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action payload construction.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
