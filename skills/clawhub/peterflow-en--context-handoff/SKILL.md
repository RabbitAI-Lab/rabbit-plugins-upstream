---
name: context-handoff
description: Hand context to a new receive-only chat when explicitly invoked, or send relevant context to an already authorized subtask through its existing channel.
---

# Hand off context

Identify your role first. A **receiver** follows its dispatch message and ends at the authorized stopping point. An **explicitly invoked sender** follows [new-chat handoff](references/new-chat.md). A **coordinator** sending information for an authorized assignment uses [subagent sync](references/subagent.md). Discussion, editing or review of this skill and ordinary summaries stay in the current task.

Build the smallest packet that lets the recipient orient itself:

- Goal, recipient role, authority for this turn, scope and stopping condition. Include the user's latest corrections. Keep future work separate from present authorization.
- Absolute workspace and topic paths, branch, working-copy state and observation time. Identify uncommitted artifacts the recipient needs to be able to reach.
- Source of truth and shortest reading order. Include decisions that affect the next step, why the chosen approach won and what earlier assumption it supersedes. Link to existing plans, decisions and evidence. Mark the minimum “read on receipt” and defer other sources until work is authorized.
- Completed, in-progress, blocked and unverified work. Distinguish static inspection, mock tests, live runs, historical evidence, environment failures and checks never run.
- Exact interruption point, owner, last command or receipt, any pending process/session and awaited result. Preserve the present state without restarting work to prepare the handoff.
- Suggested skills, their locations and trigger conditions only where helpful for later work.
- Missing information that would matter after authorization. Mark unknowns and avoid speculative repository scans.

Use a unique system-temporary directory and an absolute path for a longer or reusable packet. Include essential text inline when the recipient cannot access the filesystem. Exclude credentials and unrelated conversation history. Keep enough information for the receiving role to locate the authoritative material and verify receipt.
