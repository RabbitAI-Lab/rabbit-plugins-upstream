## Description:

Verify hash-pinned workspace rebuild scripts survive sandbox snapshot wipes, and detect self-mutating config files whose checksum drifts because a later step rewrites an earlier step's output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to verify idempotent workspace rebuild runbooks, triage checksum drift after sandbox snapshot wipes, and distinguish benign trailing-newline changes from real corruption.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Operational commands copied from the guidance can affect selected workspace files if run against the wrong path.

Mitigation: Run examples only in the intended workspace, review paths and exit codes first, and keep backups before delete, re-run, or re-paste actions.

Risk: Checksum drift can be misclassified, causing a real content change to be treated as benign.

Mitigation: Compare byte size, trailing-newline behavior, and diffs before trusting a rebuild or restoring a file.

## Reference(s):

- [Published ClawHub skill](https://clawhub.ai/orionshaowswmw/skills/idempotent-rebuild-verification)
- [Artifact skill source](artifact/SKILL.md)
- [Artifact README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell command examples and decision tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No hidden execution, persistence, or data sharing behavior is reported by the security evidence.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
