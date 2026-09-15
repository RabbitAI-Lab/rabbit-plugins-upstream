## Description:

Detect Language (detectlanguage.com) helps agents search and read Detect Language data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Detect Language through an OOMOL-connected account for single-text language detection, batch detection, account status checks, and supported-language listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documentation includes one-line remote installer commands for the oo CLI.

Mitigation: Install only after independently verifying the installer source and contents, or prefer official package or download-and-verify installation steps.

Risk: Detect Language requests are routed through OOMOL as an intermediary.

Mitigation: Install and use the skill only when the user is comfortable with OOMOL mediating Detect Language requests and credentials server-side.

## Reference(s):

- [Detect Language homepage](https://detectlanguage.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-detect-language)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before running read-only Detect Language actions through the oo CLI.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
