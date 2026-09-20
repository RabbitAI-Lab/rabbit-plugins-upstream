## Description:

Next suggests follow-up actions after task completion, using topic guides and optional hooks to detect stalls, enforce ask gates, and compose next-action choices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to surface concrete next-step options after a task completes, especially when follow-up work may be hidden in task lists, PRs, issues, CI, session state, or local plans. It also helps identify stalled workflows and route them to a fix flow when required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic hooks may inspect transcripts, debug logs, workspace files, plugin directories, and project trackers more broadly than expected.

Mitigation: Install only after review, and use manual invocation or narrower hook configuration when working across sensitive repositories or private trackers.

Risk: The skill can suggest GitHub, Plane, shell, and task-management follow-ups that affect active development workflows.

Mitigation: Review proposed actions before execution and keep destructive or externally visible operations behind explicit user confirmation.

Risk: Local helper scripts depend on hook wiring, transcript paths, jq, and environment-specific behavior.

Mitigation: Validate hook behavior in a non-sensitive workspace before enabling automatic invocation in routine sessions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/next)
- [Ask gates](artifact/ask-gates.md)
- [Suggestion patterns](artifact/suggestion-patterns.md)
- [Stall detection](artifact/stall-detect.md)
- [Stop hook trigger](artifact/resources/next-trigger.sh)
- [Reactive guard](artifact/resources/next-reactive-guard.sh)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, API calls, configuration]

**Output Format:** [Markdown guidance with option labels, descriptions, and inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce AskUserQuestion option content and hook decision JSON when installed with supported hooks.]

## Skill Version(s):

0.10.1 (source: server release metadata and CHANGELOG, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
