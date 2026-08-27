## Description:

Code Workflow guides agents through research, planning, user review, and TDD implementation for code changes, with optional PR capture and GitHub companion steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to make an agent research existing context, write plan artifacts, obtain user review, and implement code changes with TDD and verification before commits or PRs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires broad searches through local and peer knowledge stores before many routine coding tasks.

Mitigation: Install it only in workspaces where those searches are acceptable; narrow trigger terms, prefer current-repository lookup by default, and require confirmation before cross-repository or RAG searches.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/code-workflow)
- [SKILL.md](SKILL.md)
- [Steps: Research, Plan, Review, Branch](steps.md)
- [Implement](implement.md)
- [PR Workflow](pr.md)
- [Plan/Research Pre-Search Obligation](plan-research-search.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, YAML/frontmatter examples, checklists, and PR body templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update research notes, plan files, task checklists, walkthrough notes, PR bodies, and visual PR evidence artifacts in an agent workspace.]

## Skill Version(s):

0.7.1 (source: server release metadata and changelog, released 2026-08-26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
