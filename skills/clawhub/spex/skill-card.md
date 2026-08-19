## Description:

Spec-Driven Development (Spex) skill that manages the full SDLC from requirement analysis and design to incremental implementation and submission through manual /spex command routing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiangxin](https://clawhub.ai/user/jiangxin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use Spex to run a spec-driven development workflow: create or modify specifications, apply implementation steps, review fixes, merge completed work, archive finished specs, and initialize the local Spex environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify repositories and create commits or merges as part of SDLC automation.

Mitigation: Run it in a controlled working tree, review planned file changes before commit or merge, and keep normal branch protection and code review controls enabled.

Risk: Initialization and helper commands can alter the local environment, install Python dependencies, and place a `spex` command in `~/.local/bin`.

Mitigation: Start with `spex init --dry-run`, use `--skip-deps` when managing dependencies separately, and review installation effects before enabling the tool.

Risk: Local hooks and pager/debug settings can execute or expose behavior outside the skill's high-level workflow.

Mitigation: Inspect `.spex/hooks/` before running workflows, avoid untrusted `PAGER` values, and avoid debug logging when secrets or proprietary output may be present.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/jiangxin/spex/tree/master/skills/spex)
- [ClawHub skill page](https://clawhub.ai/jiangxin/skills/spex)
- [Claude Code Skills Specification](references/SKILLS-SPEC.md)
- [Apply Review Loop](references/apply-review-loop.md)
- [Compact SOP Style](references/compact-sop-style.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with command-oriented procedures, JSON where helper scripts request structured data, and shell commands for local workflow actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Manual invocation only; routes to specific /spex command procedures and bundled helper scripts.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter and pyproject.toml report 0.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
