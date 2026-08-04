## Description: <br>
Drafts, rewrites, edits, or audits technical, workplace, long-form, or creative prose to reduce AI-shaped wording, verbosity, jargon, unsupported claims, robotic structure, and formatting excess while preserving meaning and voice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joshuagoode](https://clawhub.ai/user/joshuagoode) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, developers, and editors use this skill to produce finished prose or source-aware audits that remove AI-shaped writing while preserving facts, constraints, uncertainty, and voice. It is suited to technical, workplace, long-form, and creative writing where clarity and fidelity matter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Drafts may contain sensitive information, and the skill can run bundled local Python checks against files the user provides. <br>
Mitigation: Use the skill only in a trusted local environment, avoid highly sensitive drafts unless appropriate controls are in place, and confirm file paths before lint or before/after comparison commands run. <br>
Risk: Mechanical lint and delta results can be mistaken for proof of truth, completeness, authorship, or quality. <br>
Mitigation: Treat lint and structural deltas as review signals only, run the manual completion test, and keep protected facts, uncertainty, and required wording grounded in the source. <br>
Risk: A rewrite can accidentally strengthen claims, alter scope, or drop protected names, values, warnings, requirements, or conditions. <br>
Mitigation: Build a protected-content ledger before editing and sweep the final prose against the source for actors, values, attribution, negation, certainty, force, causal links, and sequence. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/JoshuaGoode/plain-writing/tree/main/plain-writing) <br>
- [AI-shaped writing patterns](artifact/references/ai-patterns.md) <br>
- [Writing completion test](artifact/references/eval.md) <br>
- [Plain Writing ClawHub page](https://clawhub.ai/joshuagoode/skills/plain-writing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Plain text or Markdown prose, with optional shell commands for local lint and before/after comparison checks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled checks can emit human-readable or JSON lint/evaluation reports; they are review aids and do not certify factual accuracy, completeness, authorship, or regulatory conformance.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
