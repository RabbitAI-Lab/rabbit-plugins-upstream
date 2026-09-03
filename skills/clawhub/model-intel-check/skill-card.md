## Description:

Black-box evaluation skill for checking whether an OpenAI-compatible API endpoint appears to serve the expected model capability level, using standardized AIME and GPQA-style benchmark runs and comparison against reference scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2641183145-oss](https://clawhub.ai/user/2641183145-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to benchmark a model API endpoint, compare observed scores with public reference anchors, and identify likely model substitution, quantization loss, stripped reasoning behavior, or endpoint inconsistency. It supports CLI and local web UI workflows that produce auditable result files for manual review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses model-provider API credentials for the tested endpoint.

Mitigation: Use temporary or scoped API keys supplied through environment variables, avoid putting credentials in configuration files, and rotate credentials after benchmark runs when appropriate.

Risk: The security review notes WAF-bypass User-Agent guidance.

Mitigation: Only use the User-Agent behavior when authorized by the provider or intermediary, and review provider terms before running high-concurrency benchmarks.

Risk: Benchmark conclusions can be misleading because public questions may be contaminated, transport failures may be miscounted, or endpoint routing may change during a run.

Mitigation: Follow the documented anti-cheat checks, rerun transport failures before scoring, record endpoint model echoes, and manually review missed answers before drawing conclusions.

## Reference(s):

- [Reference Score Anchors](references/README.md)
- [Benchmark Catalog](references/benchmarks.md)
- [Anti-Cheat and Integrity Checks](references/anti-cheat.md)
- [Dataset Preparation Notes](data/README.md)
- [Kimi Vendor Verifier](https://github.com/MoonshotAI/Kimi-Vendor-Verifier)
- [DeepSeek-R1 Reference](https://github.com/deepseek-ai/DeepSeek-R1)
- [OpenAI GPT-5 Reference](https://openai.com/index/introducing-gpt-5/)
- [Gemini Model Reference](https://deepmind.google/models/gemini/)
- [GPQA Dataset](https://huggingface.co/datasets/Idavidrein/gpqa)
- [MathArena](https://matharena.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, JSON files, Markdown reports]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, JSONL result files, text review files, and local web UI output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses endpoint API credentials supplied by environment variables and writes benchmark results under a local results directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
