## Description:

SerpApi lets agents search and read Google web, News, and Maps data through the OOMOL SerpApi connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to run SerpApi-backed Google web, News, and Maps searches through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes commands that execute remote installer scripts directly in a shell.

Mitigation: Review the installer source before use, and prefer a verified, pinned, package-manager, or checksum-validated install path for the oo CLI.

Risk: The skill depends on OOMOL authentication and a connected SerpApi provider before connector actions can run.

Mitigation: Run setup or connection steps only after an auth or connection failure, and keep normal search usage to the documented read-oriented connector actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-serpapi)
- [SerpApi homepage](https://serpapi.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON when run with the documented --json flag.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
