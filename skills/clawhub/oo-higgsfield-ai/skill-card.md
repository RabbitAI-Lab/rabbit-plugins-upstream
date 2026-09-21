## Description:

Operate Higgsfield AI through an OOMOL-connected account by inspecting live connector schemas and running Higgsfield generation, status, and cancellation actions through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Higgsfield image and video generation requests, check generation status and outputs, and cancel queued requests through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes unverified remote installer execution.

Mitigation: Review installer commands before installing, prefer verified official documentation or pinned checksum-verified releases, and install only when the oo CLI is missing.

Risk: Write and cancellation actions can change Higgsfield AI state.

Mitigation: Confirm the exact payload and effect with the user before running generation submission or cancellation actions.

## Reference(s):

- [Higgsfield AI homepage](https://higgsfield.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-higgsfield-ai)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to inspect live connector schemas before running Higgsfield actions and to request confirmation before write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
