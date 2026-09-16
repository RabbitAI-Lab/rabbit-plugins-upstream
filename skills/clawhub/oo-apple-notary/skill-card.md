## Description:

Apple Notary helps agents operate Apple's Notary API through an OOMOL-connected account and the oo CLI for submission, status, log, and recent-submission workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill to guide Apple notarization workflows, including inspecting action schemas, submitting software metadata, checking submission status, listing recent submissions, and retrieving notarization logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that run downloaded scripts in a shell.

Mitigation: Install the oo CLI through a trusted, reviewed, versioned method outside the agent; do not allow the agent to run remote installer pipes unless the installer source has been independently reviewed.

Risk: Submitting software changes Apple Notary state and starts a notarization workflow after upload.

Mitigation: Confirm the exact action payload and expected effect with the user before running state-changing actions.

## Reference(s):

- [Apple Notary API documentation](https://developer.apple.com/documentation/notaryapi)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-apple-notary)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts for confirmation before state-changing Apple Notary actions.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
