## Description:

Tripadvisor (tripadvisor.com). Use this skill for ANY Tripadvisor request: searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Tripadvisor locations, find nearby locations, retrieve location details, and fetch location photos through an OOMOL-connected Tripadvisor account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes directly executing remote installer scripts.

Mitigation: Use a verified official installation path, inspect the installer, and prefer checksum or signature verification before executing anything.

Risk: Tripadvisor access is mediated through OOMOL connector execution and server-side credentials.

Mitigation: Install only if you are comfortable using OOMOL as the intermediary for Tripadvisor data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-tripadvisor)
- [Tripadvisor Developers](https://www.tripadvisor.com/developers)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live action schemas before sending JSON payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
