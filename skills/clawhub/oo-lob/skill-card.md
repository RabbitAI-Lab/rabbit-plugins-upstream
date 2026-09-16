## Description:

Lob (lob.com) skill for address autocomplete, verification, and standardization through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Lob address autocomplete and address verification actions through an OOMOL-connected Lob account. It supports single and bulk US or international address verification workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts directly in a shell.

Mitigation: Review setup instructions before installing and prefer an independently verified or package-manager installation path for the oo CLI.

Risk: Lob requests are executed through OOMOL's connector with server-side credential handling.

Mitigation: Use the skill only for the listed Lob address autocomplete and verification actions unless you intentionally want OOMOL to handle that Lob request.

## Reference(s):

- [ClawHub Lob Skill](https://clawhub.ai/oomol/skills/oo-lob)
- [Lob Homepage](https://www.lob.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live Lob action schemas are fetched before payload construction; command responses are JSON when the oo CLI is run with --json.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
