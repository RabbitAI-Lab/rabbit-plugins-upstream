## Description:

Enigma lets agents operate Enigma through an OOMOL-connected account for business search, entity lookup, aggregate counts, KYB verification, list management, schema metadata, and task tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operations teams use this skill to query and manage Enigma business data through an OOMOL-connected account, including searches, entity lookups, KYB checks, and user-managed lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute changing external code on the user's machine.

Mitigation: Review the setup path before installing and independently verify the OOMOL installer source before running curl or PowerShell installer commands.

Risk: The skill can create, submit, and delete Enigma data through the connected account.

Mitigation: Confirm write and destructive payloads with the user before execution, especially list creation, suggestions, and delete_list targets.

Risk: Actions run through an OOMOL-connected Enigma account.

Mitigation: Use the skill only when OOMOL is trusted and the connected account scopes are appropriate for the requested task.

## Reference(s):

- [ClawHub Enigma Skill](https://clawhub.ai/oomol/skills/oo-enigma)
- [Enigma Homepage](https://www.enigma.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
