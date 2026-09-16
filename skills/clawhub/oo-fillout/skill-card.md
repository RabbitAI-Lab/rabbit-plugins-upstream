## Description:

This skill helps agents operate Fillout through an OOMOL-connected account, including reading, creating, and deleting form submission data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Fillout through an OOMOL-connected account, including listing forms, reading metadata and submissions, creating submissions, and deleting submissions after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing a remotely downloaded installer directly in a shell.

Mitigation: Review the setup path before installing and prefer a verified, versioned, or otherwise trusted oo CLI installation method.

Risk: Fillout write and delete actions can create or remove form submissions.

Mitigation: Confirm the exact payload, target form, and submission ID with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Fillout skill page](https://clawhub.ai/oomol/skills/oo-fillout)
- [Fillout homepage](https://www.fillout.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
