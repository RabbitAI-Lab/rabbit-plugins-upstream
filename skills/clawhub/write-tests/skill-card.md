## Description:

Write Tests guides an agent to author risk-ranked tests that catch regressions, prove each new test can fail, mock only external boundaries, and pin untested legacy behavior with characterization tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to add or improve tests for features, regressions, TDD work, and legacy characterization work. The workflow ranks observable behaviors by risk and verifies that new tests fail before they pass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run project test commands and make test-related edits in the active repository.

Mitigation: Confirm the intended repository and target area before use, run commands non-interactively, and review the final diff and quoted test results.

Risk: Temporary behavior mutations used to prove that tests can fail could be accidentally retained.

Mitigation: Use mutation hygiene before reporting: inspect production-source diffs, remove temporary mutations, and rerun the relevant suite to confirm the final green result.

## Reference(s):


## Skill Output:

**Output Type(s):** [Code, Shell commands, Markdown, Guidance]

**Output Format:** [Markdown report with code edits, test names, and quoted test-run summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit test files and run project test suites in non-interactive mode.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
