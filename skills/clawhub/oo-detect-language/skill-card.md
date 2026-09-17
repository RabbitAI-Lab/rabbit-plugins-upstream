## Description:

Detect Language (detectlanguage.com) lets an agent detect the language of one or more text strings, list supported languages, and inspect account usage through an OOMOL-connected Detect Language account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill when they need an agent to detect text language, batch-detect languages, list supported languages, or check Detect Language account status through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that may execute code from OOMOL-controlled endpoints.

Mitigation: Review the installer first or use a verified package or source before running setup commands, especially in sensitive environments.

Risk: The skill depends on an authenticated OOMOL-connected Detect Language account and may fail when authentication, connection scope, billing, or credentials are unavailable.

Mitigation: Run account setup only after a relevant command failure and resolve authentication, connection, or billing errors before retrying actions.

## Reference(s):

- [Detect Language homepage](https://detectlanguage.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Detect Language skill page](https://clawhub.ai/oomol/skills/oo-detect-language)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
