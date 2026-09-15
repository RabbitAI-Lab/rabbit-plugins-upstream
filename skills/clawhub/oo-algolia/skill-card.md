## Description:

Use this skill for Algolia requests, including reading, creating, updating, and deleting data through an OOMOL-connected Algolia account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Algolia action schemas, search or browse indices, retrieve records, and perform confirmed write or delete actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Do not run the installer commands automatically; use a verified, versioned, checksum- or signature-validated oo CLI installation method.

Risk: The skill can mutate Algolia account data through write and delete actions.

Mitigation: Inspect the live action schema first, confirm the exact payload and expected effect with the user, and require explicit approval for destructive deletes.

## Reference(s):

- [ClawHub Algolia skill page](https://clawhub.ai/oomol/skills/oo-algolia)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Algolia homepage](https://www.algolia.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payload construction; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
