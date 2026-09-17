## Description:

Jam (wejam.ai) lets an agent operate Jam through an OOMOL-connected account for searching, reading, and exporting one page of Jam training data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Jam through a connected OOMOL account, inspect live connector action schemas, and export Jam training data for reporting or BI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts executed directly in a shell.

Mitigation: Install the oo CLI through a verified, signed, version-pinned method when available, or inspect and verify the installer before running it.

Risk: Jam actions can access data through the user's connected OOMOL account.

Mitigation: Run Jam operations only after confirming the requested action and expected data access scope, and inspect the live action schema before sending a payload.

## Reference(s):

- [Jam homepage](https://wejam.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Jam connection settings](https://console.oomol.com/app-connections?provider=wejam_ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses containing data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
