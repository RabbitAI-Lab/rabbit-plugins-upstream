## Description:

Jielong CLI helps an agent manage Jielong activity workflows through the `jielong` command-line tool, including creating, viewing, updating, starting, stopping, deleting, and managing signup records for activities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-tao-hash](https://clawhub.ai/user/liu-tao-hash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Jielong signup, payment-registration, and check-in activities from an agent session. It is intended for activity lifecycle tasks such as creating activities, reviewing signups, changing activity state, and removing signup data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can globally install or update the `jielong-cli` package.

Mitigation: Install only when the package source is trusted, and review the resolved package/version before allowing host-level changes.

Risk: The skill can initiate a login QR flow and reuse the logged-in Jielong account.

Mitigation: Confirm the active account identity before performing activity operations and treat account identity output as sensitive.

Risk: The skill can mutate or delete activity and signup data.

Mitigation: Confirm destructive operations with the user outside the CLI prompt and review proposed commands before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liu-tao-hash/skills/tianba-jielong)
- [ClawHub Publisher Profile](https://clawhub.ai/user/liu-tao-hash)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or text responses with inline shell commands and JSON configuration when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a locally installed `jielong` binary and a logged-in Jielong account.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
