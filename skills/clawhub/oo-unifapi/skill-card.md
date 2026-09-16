## Description:

UnifAPI lets agents inspect live connector schemas and run OOMOL-managed UnifAPI actions for reading, creating, and updating data across supported services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate UnifAPI through OOMOL-managed credentials, inspect each action's live schema, and run connector actions with JSON payloads. It supports workflows across social, SEO, content, maps, local search, events, and hotel services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review setup before installing and prefer a verified or package-manager installation of the oo CLI.

Risk: Some actions are tagged [write], and the security summary notes ambiguity about scope and effect.

Mitigation: Confirm the exact payload and expected effect with the user before running write-tagged actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-unifapi)
- [UnifAPI Homepage](https://unifapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect live action schemas before execution; write-tagged actions require confirmation of the exact payload and effect.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
