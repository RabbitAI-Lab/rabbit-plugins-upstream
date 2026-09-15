## Description:

Kontent.ai helps agents search and read Kontent.ai content through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to retrieve and list Kontent.ai content items, content types, and languages after inspecting the connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands for the oo CLI.

Mitigation: Install the oo CLI from a verified release or inspect and verify the installer before execution; do not let an agent run installer commands blindly.

Risk: The skill can prompt account login or Kontent.ai connection steps when credentials are missing or expired.

Mitigation: Perform account login and connection steps yourself only after an auth or connection failure shows they are needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kontent-ai)
- [Kontent.ai homepage](https://kontent.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal action output includes connector data and an execution id under meta.executionId.]

## Skill Version(s):

1.0.3 (source: server evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
