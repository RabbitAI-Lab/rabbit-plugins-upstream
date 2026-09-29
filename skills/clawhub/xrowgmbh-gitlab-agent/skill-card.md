## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to let an autonomous agent process assigned GitLab issues and merge requests, apply project access checks, create branches and MRs, update labels, and move work through review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to make recurring GitLab changes without confirmation.

Mitigation: Install it only for intended GitLab accounts and projects, keep the recurring job disabled during initial testing, and review the no-confirmation workflow before enabling scheduled runs.

Risk: A GitLab token can allow broad read and write access to assigned issues, merge requests, branches, labels, and discussions.

Mitigation: Use a narrowly scoped GitLab token and project membership that match the intended automation account and repositories.

Risk: The workflow can push branches with ci.skip and later trigger pipelines through glab.

Mitigation: Review the ci.skip and pipeline-triggering behavior against project policy before allowing the agent to push or update merge requests.

Risk: Project access and reviewer decisions depend on helper scripts and GitLab membership data.

Mitigation: Keep the owner-created membership gate enabled, review failed-closed outcomes, and require deterministic reviewer selection through the bundled helper.

## Reference(s):

- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [CI Tools label component](https://ci-tools.xrow.de/Components/label)
- [OpenClaw creating skills](https://docs.openclaw.ai/tools/creating-skills)
- [xrow public skills project](https://gitlab.com/xrow-public/skills)
- [Documentation style](references/documentation-style.md)
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with GitLab CLI commands, code changes, merge request and issue updates, labels, and status comments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitLab CLI access through glab, jq, and a GitLab token supplied as GITLAB_TOKEN.]

## Skill Version(s):

1.94.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
