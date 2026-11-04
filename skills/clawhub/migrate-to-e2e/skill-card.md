## Description:

Moves existing end-to-end test suites to e2e incrementally, keeping the source suite alongside each proven port and tracking migration progress in MIGRATION.md.

This skill is ready for commercial/non-commercial use.

## Publisher:

[e2e](https://clawhub.ai/user/e2e)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use the skill to move existing end-to-end suites to e2e in small, verified slices while keeping the original suite available during migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Test runs may expose real user data or credentials.

Mitigation: Use a disposable test environment with synthetic data and limited test credentials.

Risk: Installation commands may use dependencies whose versions change over time.

Mitigation: Review and lock dependency versions before running installation commands.

Risk: An AI provider may process visible application content during test steps.

Mitigation: Approve the provider for that content or use deterministic tests.

Risk: External runner releases and the companion skill installed later were outside the supplied security assessment.

Mitigation: Review the selected runner release and companion skill before using them.

## Reference(s):

- [e2e migration documentation](https://e2e.com/docs/migrate)
- [Playwright migration guide](https://e2e.tester.army/docs/migrate/playwright.md)
- [Cypress migration guide](https://e2e.tester.army/docs/migrate/cypress.md)
- [Selenium migration guide](https://e2e.tester.army/docs/migrate/selenium.md)
- [Detox migration guide](https://e2e.tester.army/docs/migrate/detox.md)
- [Maestro migration guide](https://e2e.tester.army/docs/migrate/maestro.md)
- [TesterArmy migration guide](https://e2e.tester.army/docs/migrate/testerarmy.md)
- [e2e web engine guide](https://e2e.tester.army/docs/web.md)
- [e2e mobile engine guide](https://e2e.tester.army/docs/mobile.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown migration progress and project test or configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Migration progress is recorded in MIGRATION.md; each session handles one slice.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
