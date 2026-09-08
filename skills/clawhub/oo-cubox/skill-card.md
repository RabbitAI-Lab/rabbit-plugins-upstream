## Description:

Cubox lets agents operate Cubox through an OOMOL-connected account, including saving web pages for queued parsing and snapshot processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Cubox from an agent through their OOMOL-connected account. It is most directly grounded for saving URLs after inspecting the live connector schema and confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates Cubox through an OOMOL-connected account and the oo CLI.

Mitigation: Install only if comfortable using OOMOL for the Cubox connection and review first-time setup commands before running them.

Risk: The save_url action changes Cubox state by saving a URL for processing.

Mitigation: Confirm the exact URL payload and intended effect with the user before running the write action.

Risk: First-time setup may require running an installer script.

Mitigation: Review the oo CLI installer before executing setup commands.

## Reference(s):

- [Cubox homepage](https://cubox.pro)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cubox)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before action execution; write payloads require user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
