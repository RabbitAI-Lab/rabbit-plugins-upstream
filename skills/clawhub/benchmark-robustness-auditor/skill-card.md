## Description:

Offline defensive robustness auditor for LLM benchmarks that detects contamination, temporal gaps, selection and few-shot artifacts, judge bias, hidden-instruction payloads, TS-guessing, and paired score-comparison uncertainty with deterministic stdlib Python tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, evaluation engineers, and benchmark maintainers use this skill to audit LLM benchmark datasets and result artifacts for offline robustness risks, produce defensible JSON or Markdown reports, and route CI decisions from documented exit codes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Benchmark and corpus JSONL files may contain sensitive local evaluation data.

Mitigation: Keep inputs local, restrict access to generated reports and ledgers, and avoid sharing raw JSONL artifacts outside the evaluation boundary.

Risk: The default BENCHSCAN_LEDGER path is current-directory relative and can collide in shared workspaces.

Mitigation: Set BENCHSCAN_LEDGER to a controlled per-project or CI path before running report, trend, or audit commands.

Risk: scripts/selftest.sh executes hardcoded local shell and Python snippets.

Mitigation: Run the self-test only from the trusted released package after normal package review and scanning.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/benchmark-robustness-auditor)
- [Operations Guide](docs/operations.md)
- [Integration Guide](docs/integration.md)
- [Evidence Grounding](docs/evidence.md)
- [Manifest](manifest.json)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON report contracts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces compact JSON outputs from benchscan subcommands, optional Markdown reports, documented exit codes, and hash-chained trend ledger entries.]

## Skill Version(s):

2.0.0 (source: server release evidence, frontmatter, manifest, and changelog dated 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
