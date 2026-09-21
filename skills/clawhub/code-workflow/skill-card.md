## Description:

Guides coding agents through a code-change workflow from research and planning through user review, TDD implementation, build verification, commits, and optional PR evidence capture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding agents use this skill to structure non-trivial code changes with research notes, implementation plans, explicit review gates, TDD-oriented execution, and PR preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can search local and peer planning corpora and dispatch plan or research artifacts to configured RAG systems.

Mitigation: Review and narrow the output directory, RAG receiver, and pre-lookup configuration before installation; disable dispatch paths that are not needed.

Risk: The workflow includes automatic paths that may post plans to GitHub issues or publish artifacts to configured systems.

Mitigation: Require explicit user approval before GitHub posting, PR creation, or external artifact dispatch, and verify receiver settings in each workspace.

Risk: Included hook scripts may block or warn during plan and research artifact edits.

Mitigation: Install hooks intentionally, test them in a scratch workspace, and document which hooks are advisory versus blocking for the team.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/code-workflow)
- [CHANGELOG 0.10.1 comparison](https://github.com/es6kr/skills/compare/code-workflow-v0.10.0...code-workflow-v0.10.1)
- [Skill overview](SKILL.md)
- [Workflow steps](steps.md)
- [Implementation guide](implement.md)
- [PR guide](pr.md)
- [Plan and research pre-search guide](plan-research-search.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with checklists, command examples, file naming conventions, and workflow gates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce research, plan, walkthrough, commit, and PR preparation artifacts depending on user approval and configured companion skills.]

## Skill Version(s):

0.10.1 (source: server release metadata and CHANGELOG, released 2026-09-20; SKILL.md metadata.version is 0.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
