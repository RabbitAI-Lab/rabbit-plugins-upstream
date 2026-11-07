## Description:

deja-vu memory — search the user's past AI coding sessions with the deja CLI. Holds what they already settled and never wrote into the repo (naming rules, banned or already-tried tools, required checks before merge, preferred values, who owns what). Use before your first edit in a task, before you call a change done or ready to merge, before you recommend a tool, library, design or reviewer, before re-debugging an error that may already be solved, when they say 'didn't we fix this before', 'what did we decide about X' or 'I already have that', and before telling them something on this machine does not exist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vshulcz](https://clawhub.ai/user/vshulcz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use the skill to search prior AI coding sessions for earlier decisions, fixes, preferences, and project rules before editing, debugging, recommending tools, or reporting work complete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When the deja CLI is unavailable, routine use may automatically run an unpinned package through npx.

Mitigation: Use a reviewed, pinned installation and disable the automatic npx fallback.

Risk: Retrieved transcripts can contain irrelevant or unsafe text that enters the agent's context.

Mitigation: Scope searches to relevant projects and treat retrieved history as reference material, following the skill's confirmation boundaries for past user rules.

Risk: Synchronizing extracted rules can change rule files across installed agents.

Mitigation: Review the exact rule changes and every destination file before synchronization.

## Reference(s):

- [Deja-vu memory for OpenClaw](https://vshulcz.github.io/deja-vu/guide/memory-for-openclaw.html)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Markdown with shell commands and summaries of retrieved session history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are bounded excerpts from prior session transcripts.]

## Skill Version(s):

0.24.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
