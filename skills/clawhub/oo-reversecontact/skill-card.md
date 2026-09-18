## Description:

Helps agents enrich company and professional profiles through Reverse Contact using an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Reverse Contact V2 enrichment for companies by domain and people by email, name, or company context through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that could execute unverified code.

Mitigation: Review the oo CLI installer through an official source, prefer a pinned release or verified package, and do not let an agent run curl-to-bash or PowerShell iex setup commands automatically.

Risk: Reverse Contact lookup data passes through OOMOL-connected services.

Mitigation: Confirm the connected account, authorization scope, and data handling expectations before using the skill with sensitive profile or company data.

## Reference(s):

- [Reverse Contact homepage](https://www.reversecontact.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Reverse Contact action payloads.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
