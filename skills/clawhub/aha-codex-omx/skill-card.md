## Description: <br>
Codex+OMX orchestration keeps the current Codex session as the decision maker and integrator while using bounded subagents and OMX capability surfaces for search, reading, research, testing, review, and mutually exclusive writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[its-how](https://clawhub.ai/user/its-how) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to orchestrate Codex sessions with OMX, discover available capability surfaces, delegate bounded work, and keep integration and verification in the primary session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OMX-style orchestration can expand collaboration through subagents, worktrees, or higher-cost parallel work. <br>
Mitigation: Run capability discovery first, keep the primary Codex session as final integrator, use bounded single-writer units, and require secondary confirmation for large fan-out, worktrees, cross-domain integration, or high-cost parallel work. <br>
Risk: Delegated tasks or out-of-session handoffs could expose secrets or live session material if copied into prompts. <br>
Mitigation: Exclude credentials, tokens, cookies, browser session material, provider state, live account state, and equivalent secrets from delegated work and handoff material. <br>


## Reference(s): <br>
- [Capability Orchestration](references/capability-orchestration.md) <br>
- [Aha Orch repository](https://github.com/its-How/aha-orch) <br>
- [Codex CLI](https://github.com/openai/codex) <br>
- [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Codex with OMX installed for OMX-specific capability surfaces; unavailable OMX surfaces should be skipped or replaced with native Codex capabilities according to the documented detection flow.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
