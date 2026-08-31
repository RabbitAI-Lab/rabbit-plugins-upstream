## Description:

Skyvern (skyvern.com). Use this skill for ANY Skyvern request - reading, creating, and updating data. Whenever a task involves Skyvern, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Skyvern browser automation through an OOMOL-connected account, including starting tasks, inspecting run output, listing runs, and canceling active runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can start browser automation through a connected Skyvern account, including against logged-in or sensitive websites.

Mitigation: Install only when this authority is intended, and require explicit user confirmation before starting any Skyvern task.

Risk: The skill can cancel active task or workflow runs, which may interrupt ongoing automation.

Mitigation: Confirm the target run ID and expected effect with the user before invoking cancel_run.

Risk: Incorrect run_task payloads can cause unintended browser behavior.

Mitigation: Fetch the live action schema before constructing payloads and confirm write-action payloads before execution.

## Reference(s):

- [Skyvern homepage](https://www.skyvern.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-skyvern)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect schemas and run Skyvern connector actions; run results may include outputs, hosted files, screenshots, and recordings.]

## Skill Version(s):

1.0.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
