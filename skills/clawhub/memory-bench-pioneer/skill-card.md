## Description:

TinkerClaw Memory Bench benchmarks an OpenClaw or TinkerClaw memory database locally by default, producing retrieval-quality metrics with confidence intervals and optional, consent-gated OpenAI judging and public report submission.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to measure retrieval quality for a live or copied OpenClaw or TinkerClaw memory database and collect aggregate benchmark reports. It supports local default runs, optional external LLM judging, and optional public submission after preview and confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Benchmarking can touch sensitive local memory data from a live memory database.

Mitigation: Use the default local judge and run against a copied or filtered database when contents are sensitive.

Risk: The optional OpenAI judge can send redacted benchmark queries and retrieved memory excerpts to OpenAI.

Mitigation: Use it only after reviewing the printed request preview and confirming that redacted excerpts may leave the machine; prefer OPENAI_API_KEY over command-line keys.

Risk: Submitting results opens a public GitHub pull request with aggregate report metadata.

Mitigation: Run submit.sh with --dry-run first, review every field in the schema-validated preview, and publish only after explicit confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/memory-bench-pioneer)
- [Publisher profile](https://clawhub.ai/user/globalcaos)
- [TinkerClaw project link from skill documentation](https://github.com/globalcaos/tinkerclaw)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local benchmark metrics and aggregate reports; external judging and public submission are optional and confirmation-gated.]

## Skill Version(s):

2.1.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
