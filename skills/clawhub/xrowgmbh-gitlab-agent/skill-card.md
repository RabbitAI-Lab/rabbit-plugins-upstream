## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use the agent to process assigned GitLab issues and merge requests, manage work queue status, and prepare code changes for review, subject to its project access checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious, citing actions beyond its assigned-work purpose, including changes to projects that fail the owner-access check.

Mitigation: Review the reported GitLab actions and authorization gaps before installing; grant access only to explicitly approved projects.

Risk: Security coverage is incomplete: one component was only partially inspected and some references were unresolved.

Mitigation: Treat the scan as incomplete and review affected files and references before relying on the skill.

## Reference(s):

- [GitLab user permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [GitLab contribution guide](https://docs.gitlab.com/development/contributing/#make-changes-and-open-a-merge-request)
- [Discovery performance notes](references/discovery-performance.md)
- [Discovery benchmark results](references/discovery-benchmark.json)

## Skill Output:

**Output Type(s):** [GitLab work item updates, Merge requests, Code changes, Markdown status summaries]

**Output Format:** [GitLab updates via glab, repository changes, and Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured GitLab account and access to the relevant projects.]

## Skill Version(s):

1.150.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
