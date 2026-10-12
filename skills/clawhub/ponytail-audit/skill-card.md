## Description:

Quality audit of the whole repo: bugs, security, real load, missing tests, speed, and what to delete. Most important first.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review a repository or named folder for concrete bugs, security and data-loss risks, load issues, missing tests, performance problems, and unnecessary code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit requires access to repository contents, which may include sensitive material.

Mitigation: Use it only on repositories the agent is authorized to read, and limit the requested scope when appropriate.

Risk: A read-only review can miss problems in code that was not inspected.

Mitigation: Check the report's 'Not checked' section and confirm important findings before making changes.

## Reference(s):

- [Skill homepage](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only, prioritized audit report with up to 20 numbered findings, concrete cases and suggested fixes; notes what was not checked.]

## Skill Version(s):

5.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
