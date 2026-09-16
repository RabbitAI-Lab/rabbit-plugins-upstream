## Description:

DataScope helps agents operate a DataScope account through the OOMOL oo CLI to read, create, and update DataScope data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to read DataScope answers, metadata list elements, and locations, and to create or update list elements and locations after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer scripts for the oo CLI.

Mitigation: Prefer a verified oo CLI installation method with a pinned version and checksum or signature before installing.

Risk: Write actions can change DataScope metadata list elements and locations.

Mitigation: Review the exact action payload and expected effect with the user before running write actions.

Risk: The skill acts through the connected OOMOL/DataScope account.

Mitigation: Connect only the OOMOL/DataScope account the agent is intended to use.

## Reference(s):

- [DataScope homepage](https://www.mydatascope.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated OOMOL/DataScope connection through the oo CLI; write actions require explicit payload confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
