## Description:

Make CloudArc large-package performance work reproducible, measurable, and safe to ship with bounded-memory pack/unpack benchmarks, multi-file deduplication checks, remote-search telemetry validation, and CI/manual benchmark gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vnbochkarev-netizen](https://clawhub.ai/user/vnbochkarev-netizen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to validate CloudArc large-package benchmarks, SLOs, high-cardinality metadata behavior, remote-search telemetry, and CI or manual release gates before enabling real cloud providers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run local Python tests and benchmark commands and write benchmark reports in the target repository.

Mitigation: Install and run it only for CloudArc benchmark and telemetry work, and review generated JSON and Markdown reports before using them as release evidence.

Risk: Manual benchmark mode may take hours and use tens of GiB of temporary disk.

Mitigation: Use manual mode only when the large run is intentional; keep normal CI on the smoke entry point and require the explicit manual confirmation flag.

Risk: Remote-search telemetry or benchmark artifacts that are missing, malformed, incomplete, or inconsistent could lead to an unsafe pass decision.

Mitigation: Rely on the helper's fail-closed artifact and telemetry validation, including positive RSS checks, cardinality checks, and Markdown PASS report checks.

## Reference(s):

- [CloudArc Benchmark Contract](references/contract.md)
- [CloudArc Bounded-Memory Benchmark Release Notes](references/release-notes.md)
- [ClawHub Skill Page](https://clawhub.ai/vnbochkarev-netizen/skills/cloudarc-bounded-memory-benchmark)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local benchmark guidance and helper commands; the bundled helper writes JSON and Markdown benchmark reports when run.]

## Skill Version(s):

1.1.1 (source: frontmatter, VERSION, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
