## Description:

Cronly enables an agent to read and manage Cronly projects and job monitors through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Cronly through their OOMOL-connected account, including inspecting connector schemas, listing or retrieving projects and job monitors, and creating or deleting those resources when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include internet installer commands that can execute remote code.

Mitigation: Install only when the source is trusted, prefer official verifiable installation instructions, and avoid running pipe-to-shell or PowerShell iex commands blindly.

Risk: The skill can create and delete Cronly projects and job monitors in the connected account.

Mitigation: Confirm the exact payload and effect before write actions, and require explicit approval for the specific target before destructive actions.

## Reference(s):

- [Cronly homepage](https://cronly.app/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Cronly skill page](https://clawhub.ai/oomol/skills/oo-cronly)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use live Cronly connector schemas and return JSON responses with execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
