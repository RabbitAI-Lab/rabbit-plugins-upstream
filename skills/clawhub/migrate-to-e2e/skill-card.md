## Description:

Moves an existing Playwright, Cypress, Selenium, Detox, Maestro, or TesterArmy suite to e2e one slice at a time, with the old suite running beside the new one until each ported test is proven. Keeps a MIGRATION.md progress file so any later session resumes where the last stopped. Optionally plants a defect to show both suites catch it. Use for /migrate-to-e2e, "migrate our tests to e2e", "port these Maestro flows", "move our TesterArmy tests", or when a project has an e2e config and an older suite still running.

This skill is ready for commercial/non-commercial use.

## Publisher:

[e2e](https://clawhub.ai/user/e2e)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to migrate an existing automated test suite to e2e incrementally while keeping the original suite running. It guides test inventory, porting, validation, and progress tracking across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External runner packages and linked guides are outside the bundled skill security review.

Mitigation: Use a reviewed, pinned runner release and inspect its companion skill and referenced guidance before execution.

Risk: Migration runs can interact with accounts or test data.

Mitigation: Use test accounts and isolated test data.

Risk: Model-assisted steps depend on provider settings.

Mitigation: Review provider settings before enabling model-assisted steps.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/e2e/skills/migrate-to-e2e)
- [e2e migration documentation](https://e2e.com/docs/migrate)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance, migration progress files, test code, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Incremental migration, typically one test slice per session; outputs depend on the source test runner and project.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
