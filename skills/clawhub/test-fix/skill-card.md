## Description:

Fix failing tests without weakening them — run the suite once, rerun only the failing files to separate flaky from real failures, classify each real failure as source bug or wrong test, then propose minimal diffs for approval. Use when asked to fix failing tests or make the suite green.

This skill is ready for commercial/non-commercial use.

## Publisher:

[winsoftlabs30](https://clawhub.ai/user/winsoftlabs30)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to diagnose failing test suites, distinguish flaky failures from consistent ones, decide whether a consistent failure points to a source bug or a wrong test, and prepare minimal patch proposals for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: If local test tools are missing, a suggested command may offer to download an unpinned package.

Mitigation: Prefer the project's installed test runner; before downloading a package, confirm its identity and version with the user.

Risk: A proposed patch may misdiagnose a failing test.

Mitigation: Review the failure evidence and patch diff, and apply a patch only after explicit approval.

## Reference(s):

- [Test Fix on ClawHub](https://clawhub.ai/winsoftlabs30/skills/test-fix)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Markdown, Code, Files]

**Output Format:** [Markdown reports and patch files with unified diffs; shell commands as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Patch proposals require explicit approval before application.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
