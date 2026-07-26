## Description: <br>
Runtime-neutral orchestration: keep this session as decision maker/integrator; for non-trivial work prefer bounded available agents for search, reading, research, testing, review, and mutually exclusive writes. Preserve confirmation gates and the lowest-sufficient route; prefer a matching runtime adapter when available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[its-how](https://clawhub.ai/user/its-how) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to guide an AI agent in choosing bounded delegation, verification, review, and handoff routes for non-trivial work while preserving confirmation gates and permission limits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may encourage use of subagents, worktrees, or handoff files for non-trivial tasks. <br>
Mitigation: Keep each unit bounded and disclosed, and require explicit secondary confirmation for large fan-out, worktree use, cross-domain integration, or high-cost parallelism. <br>
Risk: Out-of-session handoff material could expose sensitive session or account state if prepared carelessly. <br>
Mitigation: Exclude credentials, tokens, cookies, browser session material, provider state, live account state, and equivalent secrets from handoff content. <br>


## Reference(s): <br>
- [Capability Orchestration](references/capability-orchestration.md) <br>
- [Source Repository](https://github.com/its-How/aha-orch) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline commands and configuration references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only orchestration guidance; no code installation or hidden access requested.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
