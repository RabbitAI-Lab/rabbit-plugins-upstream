## Description:

Use WaiverFile through an OOMOL-connected account to search and read site details, waiver forms, signed waivers, reference-matched waivers, and upcoming events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams with an OOMOL-connected WaiverFile account use this skill to retrieve WaiverFile site, form, event, and signed-waiver records from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read connected WaiverFile records, including signed waiver data available to the connected account.

Mitigation: Install and use the skill only with accounts and agents authorized to access those WaiverFile records.

Risk: The setup guidance includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified package or inspect the installer before running it, consistent with the security guidance.

## Reference(s):

- [ClawHub WaiverFile Skill](https://clawhub.ai/oomol/skills/oo-waiverfile)
- [WaiverFile Homepage](https://www.waiverfile.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only WaiverFile connector actions return JSON data through the oo CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
