## Description:

Gate CI builds on browser fingerprint regressions by adding pinned liarjs scans, baseline diffs, and score floors to browser or scraping pipelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liarjsdev](https://clawhub.ai/user/liarjsdev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI maintainers use this skill to add browser fingerprint checks to GitHub Actions, GitLab CI, Docker, or Playwright/Puppeteer workflows. It helps detect score drops or changed checks before Chromium builds or scraping harness changes ship.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CI scans may run a pinned npm package and, unless offline mode or a private endpoint is used, make a network request to the liarjs endpoint.

Mitigation: Pin liarjs in CI, use --offline or --endpoint for private infrastructure when needed, and review CI or Docker changes before merging.

Risk: Baseline files can hide or normalize fingerprint regressions if refreshed casually.

Mitigation: Commit baseline updates deliberately with diff output, and store failed scan JSON as a build artifact for diagnosis.

## Reference(s):

- [CI recipes](references/ci-recipes.md)
- [ClawHub skill page](https://clawhub.ai/liarjsdev/skills/fingerprint-ci-gate)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML, TypeScript, Dockerfile, and bash snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose pinned liarjs commands, CI snippets, baseline JSON handling, and scan artifact handling.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
