## Description:

Jotform helps agents read Jotform account data and create form submissions through the OOMOL oo CLI using a connected Jotform account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can let an agent list Jotform forms, inspect form questions, retrieve forms and submissions, and create submissions after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes running an internet installer directly in a shell.

Mitigation: Prefer a versioned, integrity-verified oo CLI installation method; review the installer or use the published install guide before running it.

Risk: The skill can create Jotform submissions, which changes account data.

Mitigation: Confirm the exact form ID, question IDs, answer values, and expected effect with the user before running any write action.

Risk: Read actions may expose forms, questions, user details, or submissions from the connected Jotform account.

Mitigation: Use only the intended connected account and avoid requesting or displaying more submission data than the task requires.

## Reference(s):

- [ClawHub Jotform skill page](https://clawhub.ai/oomol/skills/oo-jotform)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Jotform homepage](https://www.jotform.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
