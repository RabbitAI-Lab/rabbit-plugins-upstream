## Description:

BugBug (bugbug.io) enables an agent to read, create, update, and run BugBug test data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to inspect BugBug suites, tests, run profiles, and run history, and to execute BugBug tests with schema-validated JSON payloads. It is intended for agents operating through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can install the OOMOL CLI through remote pipe-to-shell commands.

Mitigation: Review the OOMOL CLI installation path and use an official, verified installer before allowing an agent to run installation commands.

Risk: The skill can run a BugBug test and change state in the connected workspace.

Mitigation: Confirm the exact run_test payload and expected effect with the user before executing write actions.

## Reference(s):

- [ClawHub BugBug skill page](https://clawhub.ai/oomol/skills/oo-bugbug)
- [BugBug homepage](https://bugbug.io)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI and return connector JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
