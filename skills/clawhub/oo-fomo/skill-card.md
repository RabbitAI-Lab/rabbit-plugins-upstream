## Description:

Fomo lets agents read, create, update, and delete Fomo event data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Fomo events from an OOMOL-connected account, including listing, retrieving, creating, updating, and deleting events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute remote installer scripts for the oo CLI.

Mitigation: Prefer a verified oo CLI installation method such as a signed or checksummed release or trusted package manager, and review first-time setup manually before installation.

Risk: The skill can create, update, and delete Fomo events.

Mitigation: Confirm exact payloads before write actions and get explicit approval before destructive delete actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fomo)
- [Fomo homepage](https://fomo.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; command responses are JSON when run with --json.]

## Skill Version(s):

1.0.3 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
