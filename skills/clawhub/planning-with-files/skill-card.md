## Description:

Persistent file-based planning for multi-step AI-agent work that keeps plans, findings, and progress on disk and can inject selected planning context through lifecycle hooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to maintain durable Markdown planning state for complex, multi-step work. It is intended for tasks that benefit from persistent task plans, findings, progress logs, plan recovery, and optional gated or autonomous planning workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Planning hooks place selected project planning content into the model context, so sensitive or untrusted content in planning files may be exposed to the host agent flow.

Mitigation: Keep secrets out of planning files, treat injected planning content as data, and store external research in findings.md rather than task_plan.md.

Risk: Session replay can emit bounded local transcript excerpts when explicitly run with --replay.

Mitigation: Use --metadata for aggregate same-project counts, and run --replay only when prior local transcript excerpts are intentionally needed.

Risk: Unattended or long-running planning workflows can repeatedly inject stale or tampered plan content.

Mitigation: Use attestation or v3 modes for sensitive work and re-attest after intentional plan edits.

Risk: An unpinned external npx install route may not identify the exact reviewed version or commit.

Mitigation: Avoid unpinned external npx installs unless the exact version or commit can be verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/planning-with-files)
- [Reference: Manus Context Engineering Principles](reference.md)
- [Examples: Planning with Files in Action](examples.md)
- [Attestation locking and fallback](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/attestation-locking.md)
- [Performance notes](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/perf-notes.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown planning files with inline shell or PowerShell commands and hook-provided context text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates project-local planning artifacts such as task_plan.md, findings.md, progress.md, optional .planning state, and ledger JSONL files.]

## Skill Version(s):

3.16.1 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
