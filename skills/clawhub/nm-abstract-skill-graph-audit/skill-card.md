## Description:

Audit Skill() refs; detect hubs, isolates, and dangling targets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to audit OpenClaw or related skill repositories for Skill() reference topology, including hubs, orchestrators, isolates, and dangling targets. It is useful before documentation passes, renames, retirements, and release checks that need broken skill references surfaced.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit examples assume the referenced skill_graph.py script exists in a plugin checkout and may be run against private repositories.

Mitigation: Review the referenced script separately before execution, especially before running it on private repositories.

Risk: Dangling-reference and isolate findings can include false positives from examples, external plugins, placeholders, or legitimate library, entrypoint, and hook-target skills.

Mitigation: Triage findings with the documented isolate taxonomy and dangling-reference classes before making repository changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-skill-graph-audit)
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown, configuration]

**Output Format:** [Markdown guidance with shell command examples and JSON report workflow examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides use of a referenced skill_graph.py script; machine-readable audit reports may be written as JSON by that script.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
