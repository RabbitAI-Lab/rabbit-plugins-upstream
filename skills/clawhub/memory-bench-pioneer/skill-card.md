## Description:

Benchmarks an OpenClaw memory database with retrieval-quality metrics, confidence intervals, and optional judged evaluations while keeping the default workflow local.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to benchmark TinkerClaw or OpenClaw memory retrieval quality, collect aggregate memory statistics, and optionally prepare anonymized benchmark results for public submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill benchmarks a live memory database that may contain sensitive information.

Mitigation: Use the default local judge, benchmark a copied database with --db, and review the generated report before any submission.

Risk: The optional OpenAI judge can transmit benchmark queries and redacted retrieved memory excerpts to api.openai.com.

Mitigation: Choose --judge openai only after reading the printed request preview and confirming that the redacted excerpts are acceptable to send.

Risk: Submitting results can create a public GitHub pull request containing the statistics report.

Mitigation: Run submit.sh with --dry-run first, avoid --contributor and --include-token-stats unless publishing that attribution or usage summary is acceptable, and publish only after reviewing every field.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/globalcaos/skills/memory-bench-pioneer)
- [TinkerClaw Repository](https://github.com/globalcaos/tinkerclaw)
- [TinkerClaw Issues](https://github.com/globalcaos/tinkerclaw/issues)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Analysis, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default local judging; optional OpenAI judging and GitHub pull request submission require explicit user consent.]

## Skill Version(s):

2.1.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
