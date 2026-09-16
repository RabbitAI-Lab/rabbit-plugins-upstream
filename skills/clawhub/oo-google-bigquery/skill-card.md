## Description:

Operates Google BigQuery through an OOMOL-connected account for reading, querying, creating, updating, and deleting BigQuery resources with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data teams use this skill to inspect BigQuery projects, datasets, tables, jobs, routines, and models; run SQL queries; manage resources; insert rows; and start Cloud Storage load or extract jobs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute arbitrary code on the user's machine.

Mitigation: Use the skill only if OOMOL and the oo CLI are trusted; avoid direct remote installer execution unless the installer source and integrity can be verified through safer, signed, or pinned installation instructions.

Risk: The skill can run BigQuery write and destructive actions that change or delete datasets, tables, routines, models, jobs, or data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-google-bigquery)
- [Google BigQuery homepage](https://cloud.google.com/bigquery)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or execute oo CLI connector commands; write and destructive BigQuery actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
