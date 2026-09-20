## Description:

Intelliprint lets agents search and read Intelliprint backgrounds, mailing lists, recipients, and print jobs through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve Intelliprint account data, including reusable backgrounds, mailing lists, recipients, and print jobs. The documented actions are read-oriented get and list operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run a downloaded installer script before the user has independently reviewed or verified it.

Mitigation: Use an official reviewed installation method or verify the installer before execution, and do not let an agent run the installer blindly.

Risk: The skill accesses data from a connected Intelliprint account through OOMOL.

Mitigation: Install only when the user trusts OOMOL and is comfortable connecting the relevant Intelliprint account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-intelliprint)
- [Intelliprint homepage](https://www.intelliprint.net)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses read-oriented Intelliprint get and list actions; live action schemas are checked before payload construction.]

## Skill Version(s):

1.0.3 (source: evidence metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
