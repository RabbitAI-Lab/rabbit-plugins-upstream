## Description:

Coresignal lets agents search, preview, and collect Coresignal Base Company records through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Coresignal company data via an OOMOL-connected account, including search, preview, and collection workflows for Base Company records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to pipe a downloaded installer script directly into a shell.

Mitigation: Prefer a verified or package-managed oo CLI installation path, or review the installer source before running it.

Risk: Future connector actions could include write or destructive operations.

Mitigation: Confirm the exact action, payload, and expected effect with the user before running any action marked write or destructive.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-coresignal)
- [Coresignal homepage](https://coresignal.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
