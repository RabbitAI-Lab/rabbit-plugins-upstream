## Description:

Code Review guides an agent through production-readiness reviews of working-tree or branch changes, including DRY/design checks, test and build execution, categorized findings, and permission-gated fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review code changes before release, verify build and test status, surface categorized findings, and decide which fixes an agent should apply after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run repository-controlled test and build commands, which may execute untrusted code.

Mitigation: Use it only on repositories you trust, or first approve the exact commands and run them in a disposable sandbox without secrets or broad filesystem/network access.

## Reference(s):

- [Branch scope review workflow](references/branch-review.md)
- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/code-review)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with categorized findings, build/test status, cited file locations, and optional shell commands for verification.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose fixes, but artifact behavior requires reporting first and waiting for explicit user approval before editing code.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
