## Description:

Personal AI (personal.ai) lets an agent read, create, and update Personal AI data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Personal AI personas through an OOMOL-connected account, including sending messages or instructions and uploading memories, text documents, or public URL content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running unverified remote installer scripts directly in a shell.

Mitigation: Prefer a signed package, pinned release, checksum or signature verification, or manual inspection before installing the oo CLI.

Risk: Using the skill can send selected content through OOMOL to Personal AI and write to Personal AI state.

Mitigation: Install only if OOMOL is an acceptable intermediary, review selected content before sending, and confirm the exact payload and effect before write actions.

## Reference(s):

- [Personal AI homepage](https://personal.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Personal AI skill on ClawHub](https://clawhub.ai/oomol/skills/oo-personal-ai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent actions may return JSON from the oo CLI connector.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
