## Description: <br>
Audit agentic framework directories, prompt systems, skills, planner files, workflow guidance, memory-like files, configs, and agent-facing documentation for behavioral failures, prompt bloat, instruction conflicts, over-enforcement, unsafe autonomy, prompt-injection exposure, inefficient tool-use guidance, layer drift, review-integrity risks, and production-readiness issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[illimitedenterprise](https://clawhub.ai/user/illimitedenterprise) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to audit agentic framework projects and prompt-bearing files for behavioral-control risks, prompt-injection exposure, instruction conflicts, unsafe autonomy, review-integrity gaps, and production-readiness issues. It is suited for Hermes, Codex/OpenAI-style skills, OpenClaw/ClawHub skills, LangGraph, CrewAI, AutoGen, and custom agent frameworks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit output may include prompt or instruction text from scanned targets, including confidential project material. <br>
Mitigation: Run the skill only on repositories and agent configuration where the operator intends that material to appear in local audit artifacts. <br>
Risk: Sensitive-file scanning is opt-in and redaction is heuristic, so confidential values may not be fully protected if sensitive files are included. <br>
Mitigation: Keep likely secret-bearing files excluded by default and include them only after explicit operator review. <br>
Risk: Deterministic findings and same-agent review observations are heuristic review evidence, not certification that a project is safe. <br>
Mitigation: Treat generated reports as inputs to human review, preserve deterministic findings as authoritative, and require explicit approval before applying remediation. <br>


## Reference(s): <br>
- [Audit Taxonomy](references/audit-taxonomy.md) <br>
- [Framework Profiles](references/framework-profiles.md) <br>
- [ClawHub Release Checklist](references/clawhub-release.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, CSV, Guidance, Configuration] <br>
**Output Format:** [Markdown reports, JSON findings and instruction graphs, CSV inventory, gated review packets, and dry-run remediation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Report-only by default; automatic patching is disabled and same-agent review is gated.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
