## Description:

Safe Refactor guides agents through behavior-preserving code refactors by requiring a test-backed behavior contract, a green baseline, small mechanical steps, grep verification for renames, and final proof.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to restructure, rename, extract, move, inline, or split existing code while preserving observable behavior. It is intended for refactor phases, not feature work or bug fixes that intentionally change behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vague requests such as "clean this up" may activate a refactor-only workflow when the user actually wants a feature or bug fix.

Mitigation: Confirm whether the requested work must preserve behavior; split intentional behavior changes into a separate follow-up task.

Risk: Refactor proposals or edits can introduce incorrect guidance or unintended behavior changes if applied without review.

Mitigation: Review the planned behavior contract, require baseline and final build/test evidence, and inspect the final diff before accepting the refactor.

## Reference(s):

- [ClawHub safe-refactor skill page](https://clawhub.ai/dennisrongo/skills/safe-refactor)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands]

**Output Format:** [Markdown guidance with file references, test and build summaries, and code changes when applied]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires observed build and test results before reporting refactor completion.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
