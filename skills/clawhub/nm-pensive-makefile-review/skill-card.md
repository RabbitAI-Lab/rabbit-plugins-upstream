## Description:

Audits Makefiles for build correctness, portability, and recipe duplication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review Makefile changes, map build dependencies, find duplicated recipes, and identify portability issues before committing build-system updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional make-based testing can execute project build logic.

Mitigation: Review commands before running them and use a trusted workspace for any make target execution.

Risk: Optional apply-style generation can change Makefile-related files.

Mitigation: Inspect the resulting git diff before accepting generated changes.

Risk: Broad build-related triggers may activate during unrelated Makefile discussion.

Mitigation: Invoke the skill intentionally for Makefile review work.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-pensive-makefile-review)
- [ClawHub Publisher Profile](https://clawhub.ai/user/athola)
- [OpenClaw Metadata Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline shell and Makefile code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces review findings with context, dependency analysis, duplication candidates, portability issues, missing targets, and an approval recommendation.]

## Skill Version(s):

1.9.19 (source: release evidence; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
