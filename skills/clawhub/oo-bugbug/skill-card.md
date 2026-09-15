## Description:

BugBug helps an agent inspect action schemas, retrieve BugBug workspace test data, and run BugBug tests through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate BugBug from an agent session: listing suites, tests, profiles, and historical runs, checking run status, and executing tests after schema inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands without an independent checksum or signature.

Mitigation: Review the setup path before installation and verify installer integrity through a trusted source before running remote install commands.

Risk: The run_test action can execute BugBug tests and may consume credits or change BugBug workspace state.

Mitigation: Require explicit user confirmation before run_test or any state-changing or credit-consuming action, and inspect the live action schema before sending a payload.

## Reference(s):

- [BugBug homepage](https://bugbug.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub BugBug skill](https://clawhub.ai/oomol/skills/oo-bugbug)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live BugBug connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
