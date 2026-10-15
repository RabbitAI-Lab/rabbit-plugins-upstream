## Description:

Helps agents search Clay data, query tables and workflows, and run routines through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and teams using Clay can look up companies and people, query tables and workflow runs, check credits, and launch routines through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include commands that download and execute an installer.

Mitigation: Review the installer source before running it, or use OOMOL's documented installation path if available.

Risk: Searches and routines can change Clay state or trigger downstream mutations.

Mitigation: Confirm the exact payload and effect before write actions; obtain explicit approval for destructive actions.

## Reference(s):

- [Clay skill on ClawHub](https://clawhub.ai/oomol/skills/oo-clay)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Clay](https://www.clay.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with JSON results and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be paginated; routines can complete asynchronously.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
