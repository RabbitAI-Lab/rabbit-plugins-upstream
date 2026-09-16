## Description:

Goody (ongoody.com) helps agents read, create, and update Goody data through the OOMOL oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Goody from an OOMOL-connected account, including retrieving users, orders, products, payment methods, and workspaces. The skill also guides agents to inspect live action schemas and confirm state-changing actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands executed through a shell.

Mitigation: Install the oo CLI only after independently trusting and verifying the OOMOL installer source and installation method.

Risk: Some Goody connector actions may change state, and get_order is labeled as write despite being described as retrieval.

Mitigation: Inspect the live action schema and confirm any action tagged write or destructive with the user before execution.

## Reference(s):

- [ClawHub Goody skill page](https://clawhub.ai/oomol/skills/oo-goody)
- [Goody homepage](https://www.ongoody.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live Goody action schemas before running connector actions; action responses are JSON.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
