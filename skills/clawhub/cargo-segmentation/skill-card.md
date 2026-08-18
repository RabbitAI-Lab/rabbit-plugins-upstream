## Description:

Cargo Segmentation helps agents define, inspect, update, and troubleshoot saved Cargo audience segments built from model filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and go-to-market teams use this skill to build and manage named Cargo audience filters for batch runs, play triggers, exports, and change tracking. It guides safe CLI usage, segment sizing, response interpretation, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Cargo CLI can read workspace data and change segment definitions.

Mitigation: Install and use it only in trusted workspaces, run `cargo-ai whoami` before writes, and review create, update, remove, or download commands before execution.

Risk: Broad prompts or ambiguous routing can apply segmentation actions when the user intended another Cargo workflow.

Mitigation: Confirm whether the user wants segmentation, orchestration, analytics, or storage before issuing Cargo commands.

Risk: Incorrect filter JSON, especially `conjunction` instead of `conjonction`, can silently return empty or misleading segment results.

Mitigation: Validate filter keys and column slugs before calls, preview small result sets, and use `recordsCount` from Cargo responses as the authoritative audience size.

## Reference(s):

- [Segmentation response shapes](references/response-shapes.md)
- [Segmentation troubleshooting](references/troubleshooting.md)
- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-segmentation)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Cargo CLI commands and JSON filter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference JSON CLI responses, signed download URLs, segment UUIDs, model UUIDs, and filter definitions.]

## Skill Version(s):

1.0.0 (source: frontmatter, skill-metadata.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
