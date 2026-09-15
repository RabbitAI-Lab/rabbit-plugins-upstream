## Description:

Carbone (carbone.io). Use this skill for Carbone requests involving reading, creating, updating, and deleting data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Carbone action schemas and run Carbone connector actions through an OOMOL-connected account. It supports listing templates, categories, and tags, and can update template metadata or delete templates when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer pipe commands that can execute code without local review.

Mitigation: Verify the oo CLI installer source or install the CLI through a trusted reviewed method before use.

Risk: Carbone actions are routed through OOMOL as an intermediary for the connected account.

Mitigation: Use the skill only when the user accepts OOMOL-mediated Carbone access and has connected the intended account.

Risk: Write and destructive actions can update metadata or delete Carbone templates or template versions.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-carbone)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Carbone homepage](https://carbone.io)
- [Carbone icon](https://static.oomol.com/logo/third-party/carbone.svg)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI commands that return connector JSON responses from Carbone actions.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
