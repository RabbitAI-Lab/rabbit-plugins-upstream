## Description:

Humanitix (humanitix.com). Use this skill for ANY Humanitix request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read Humanitix account data through an OOMOL-connected account, including event metadata, event lists, and account tags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends directly executing remote installer scripts for the oo CLI.

Mitigation: Confirm trust in OOMOL, install the oo CLI through a verified or inspectable method, and avoid running setup from an elevated shell unless specifically required.

Risk: Humanitix account reads are routed through OOMOL's connector.

Mitigation: Confirm the user is comfortable using the OOMOL-connected account before installing or running the connector.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-humanitix)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Humanitix](https://humanitix.com)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Humanitix connector responses are returned as JSON when actions are run with the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
