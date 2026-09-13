## Description:

code-polish helps developers run pre-release code review with lint and type checks, diff-focused analysis, parallel review agents, validated findings, and optional fixes after approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and engineers use this skill before committing, pushing, or reviewing a GitHub PR to find real issues in changed code and apply targeted fixes after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run a repository-defined validation command.

Mitigation: Review the command it plans to run from CLAUDE.md, especially for third-party or untrusted repositories.

Risk: Fix mode can edit files while polishing local work.

Mitigation: Keep uncommitted work backed up or reviewable, and inspect the resulting diff before committing or pushing.

Risk: Third-party PR code and PR text are untrusted inputs.

Mitigation: Use review mode for third-party PRs so the skill reports findings without editing the checked-out tree.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/code-polish)
- [Source homepage](https://github.com/tenequm/skills/tree/main/skills/polish)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown review reports with file and line findings, inline code suggestions, shell commands, and optional file edits in fix mode.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are grouped by correctness, cleanliness, design, and efficiency; fix mode waits for approval before applying reported fixes.]

## Skill Version(s):

3.1.0 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
