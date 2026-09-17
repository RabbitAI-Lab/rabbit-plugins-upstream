## Description:

Route4Me helps agents inspect schemas and run Route4Me optimization list, create, and delete actions through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Route4Me route optimization records from an agent, including reading optimizations, creating optimization problems, and deleting selected optimizations with confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer scripts for the oo CLI.

Mitigation: Prefer installing the oo CLI from a verified package or staged download with checksum or signature validation.

Risk: The skill can create and delete Route4Me optimization problems.

Mitigation: Confirm exact payloads and targets before write or destructive Route4Me actions.

## Reference(s):

- [ClawHub Route4Me skill page](https://clawhub.ai/oomol/skills/oo-route4me)
- [Route4Me homepage](https://route4me.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke Route4Me connector actions that return JSON data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
