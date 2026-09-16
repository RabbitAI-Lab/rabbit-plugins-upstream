## Description:

Recall.ai (recall.ai). Use this skill for ANY Recall.ai request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Recall.ai through an OOMOL-connected account, including creating, retrieving, listing, removing, and deleting bot-related meeting resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path tells users to execute remote installer scripts for the oo CLI, which the security evidence flags as high-impact enough to require review.

Mitigation: Review the installer path before installing and prefer an official versioned package, signed installer, package manager, or checksum-verified download.

Risk: The skill can create Recall.ai bots, remove active bots from calls, and delete completed bot media.

Mitigation: Confirm the exact payload, target resource, and user intent before running write or destructive actions.

## Reference(s):

- [Recall.ai homepage](https://www.recall.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Recall.ai ClawHub skill page](https://clawhub.ai/oomol/skills/oo-recallai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include action schemas, connector command output, execution identifiers, and setup guidance.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
