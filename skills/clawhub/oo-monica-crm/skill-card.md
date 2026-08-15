## Description:

Operate Monica CRM through an OOMOL-connected account for reading contacts and notes, creating and updating notes, and deleting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to perform Monica CRM contact and note workflows through the OOMOL Monica CRM connector. It supports read operations directly and requires review before write or destructive note operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update Monica CRM notes.

Mitigation: Review the exact target and payload with the user before running write actions.

Risk: The skill can delete Monica CRM notes.

Mitigation: Confirm the note identifier and obtain explicit approval before running destructive actions.

Risk: The skill depends on the OOMOL connector and oo CLI having access to the user's Monica CRM account.

Mitigation: Install and use it only when the user trusts OOMOL and the oo CLI with Monica CRM access.

## Reference(s):

- [Monica CRM skill page](https://clawhub.ai/oomol/skills/oo-monica-crm)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Monica CRM homepage](https://www.monicahq.com/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration]

**Output Format:** [Markdown guidance with bash commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: evidence release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
