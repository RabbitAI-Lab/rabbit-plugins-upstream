## Description:

Frugal Subagents adds Claude Code guidance and a PreToolUse hook that steers delegated helpers toward cheaper models, blocks nested helper spawns, caps helper starts per session, and bundles lightweight web research and extraction workers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ikotelkin](https://clawhub.ai/user/ikotelkin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill in Claude Code sessions that delegate web research, listing comparison, extraction, or other helper-heavy work. It helps keep delegated work on lower-cost models, avoids helper recursion, and tells the agent how to handle limits when they are reached.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The advertised per-session helper cap can be bypassed during concurrent starts.

Mitigation: Do not rely on the helper count as a hard billing or security boundary under heavy parallel delegation; use Claude Code's built-in subagent limits when strict enforcement matters.

Risk: If Node.js is missing or the hook fails, helper starts proceed without the guard's enforced limits.

Mitigation: Install Node.js before relying on enforcement, run the documented hook self-test, and apply the skill's cheap-model and no-nesting rules manually until the guard is active.

Risk: Detailed research or extraction outputs may be written to broad workspace locations.

Mitigation: Name output files explicitly and avoid storing sensitive research results in shared or overly broad workspace paths.

## Reference(s):

- [Claude Code plugin documentation](https://code.claude.com/docs/en/plugins)
- [Node.js runtime](https://nodejs.org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration snippets, and hook feedback text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bundled workers write detailed research or extraction results to files and return short digests to the calling agent.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
