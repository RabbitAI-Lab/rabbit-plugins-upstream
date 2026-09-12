## Description:

Repeatable CloudArc workflow for validating bounded-memory streaming pack/unpack, high-cardinality multi-file .vibo packages, deduplication, remote-search range telemetry, and CI/manual benchmark gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vnbochkarev-netizen](https://clawhub.ai/user/vnbochkarev-netizen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review or change CloudArc large-package benchmarks, bounded-memory SLOs, multi-file deduplication profiles, remote-search telemetry, and CI/manual benchmark gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manual benchmark runs can take hours and consume tens of GiB of temporary disk.

Mitigation: Run the manual profile only when intentionally needed, keep its --yes gate, and prefer doctor, selfcheck, or smoke for routine checks.

Risk: The documented CloudArc SLO limits can be mistaken for measurements from the current machine.

Mitigation: Treat the README limits as the enforced contract until smoke or manual runs reproduce real benchmark artifacts in a CloudArc checkout.

Risk: Remote-search telemetry or benchmark changes can accidentally read payload data or hide provider errors.

Mitigation: Preserve the contract that metadata/search never reads the data section, only NotImplementedError triggers sidecar fallback, and provider errors remain visible.

## Reference(s):

- [CloudArc Benchmark Contract](references/contract.md)
- [CloudArc Bounded-Memory Benchmark 1.3.0 Release Notes](references/release-notes.md)
- [ClawHub Skill Page](https://clawhub.ai/vnbochkarev-netizen/skills/cloudarc-bounded-memory-benchmark)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python helper commands, JSON telemetry checks, and benchmark artifact expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide local benchmark runs that write JSON, Markdown, and SVG artifacts; the manual profile is gated by --yes because it can consume hours and tens of GiB of temporary disk.]

## Skill Version(s):

1.3.0 (source: VERSION, release evidence, and release notes dated 2026-09-11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
