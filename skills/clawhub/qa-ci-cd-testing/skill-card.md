## Description:

Helps QA, development, and DevOps teams design layered CI/CD testing stages, quality gates, feedback loops, and tool integrations for continuous testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and DevOps teams use this skill to turn testing strategy and automation architecture into CI/CD pipeline checks. It supports staged test planning, quality gate definition, feedback loops, and CI/CD test efficiency improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated CI/CD pipeline changes or release steps could affect production systems if applied without review or authorization.

Mitigation: Review generated pipeline recommendations before applying them, require explicit authorization for release or deployment steps, and validate rollback or canary strategy before production use.

Risk: Credentials or deployment secrets could be exposed if included in prompts or generated CI/CD configuration.

Mitigation: Keep credentials out of prompts and generated files, use approved secret management, and scan CI/CD changes before committing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-ci-cd-testing)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with tables and CI/CD pipeline configuration recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pipeline IDs, staged test configuration, quality gates, feedback loops, and test case tables.]

## Skill Version(s):

1.7.6 (source: server release metadata; artifact frontmatter reports 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
