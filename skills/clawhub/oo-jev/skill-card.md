## Description:

Jev lets an agent evaluate text or structured JSON state against typed Noul, Choice, and Score questions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to call Jev evaluations through OOMOL using the oo CLI without directly handling Jev credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided text or JSON to Jev through OOMOL.

Mitigation: Avoid sensitive payloads unless sharing them with Jev through OOMOL is acceptable.

Risk: Fallback setup guidance includes remote CLI installer commands.

Mitigation: Verify the installer source or use a safer installation method before running remote installer commands.

Risk: Security evidence says the action is under-labeled as safe/read-like.

Mitigation: Inspect the live connector schema and confirm the payload and intended effect before running evaluations.

## Reference(s):

- [Jev homepage](https://typesafe.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands invoke the OOMOL oo CLI and can return Jev responses as JSON.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
