## Description:

Control Word app sessions, documents, selections, comments, export, and review state with osascript workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs to control a live local Microsoft Word session on macOS, including document selection, comments, tracked-review actions, exports, and session cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can edit, export, or close local Word documents through Microsoft Word automation.

Mitigation: Require the agent to name the exact document and requested action before edits, exports, accept/reject-all actions, or document closing.

Risk: Selection-based Word commands may affect the wrong paragraph, story range, header, or comment context.

Mitigation: Read the current document, view, selection, and review state before mutation, then verify and report the final state after the action.

Risk: Document-wide review cleanup or overwrite operations can cause irreversible editorial or file loss.

Mitigation: Ask for explicit confirmation before destructive or overwrite operations and prefer creating a copy or Save As path first.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/word)
- [Skill Homepage](https://clawic.com/skills/word)
- [Execution Matrix](artifact/execution-matrix.md)
- [Live Control Patterns](artifact/live-control-patterns.md)
- [Safety Checklist](artifact/safety-checklist.md)
- [Setup](artifact/setup.md)
- [Troubleshooting](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local Word automation guidance for macOS osascript workflows; no cloud API output is produced by the skill itself.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
