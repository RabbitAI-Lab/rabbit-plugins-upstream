## Description:

sith-choir orchestrates multiple LLM provider API keys to produce, verify, refine, and report answers with voting, escalation, vision relay, caching, and JSON-capable CLI output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when they hold multiple model-provider API keys and want one agent to route work across them for answer generation, verification, refinement, vision relay, voting, and operational reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, answers, and selected images are sent to the configured model providers, and API keys are used from the credentials file.

Mitigation: Use only trusted providers, avoid secrets or regulated data, review provider data terms, and install only when this routing behavior is acceptable.

Risk: Custom base endpoint support can forward credentials and content to arbitrary configured URLs.

Mitigation: Do not configure custom base endpoints unless the exact destination is trusted and reviewed.

Risk: Answer caching and session memory can persist user questions and answer text under the skill state directory.

Mitigation: Use --no-cache for sensitive prompts, avoid --session when persistence is not wanted, and keep state files restricted to mode 0600.

Risk: Misconfiguration or unexpected provider behavior can spend tokens or expose content across multiple accounts.

Mitigation: Use --plan before live runs, set --budget limits, keep credentials chmod 600, and run the offline selftest before trusting a new installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/sith-choir)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [Design & Research Foundation](artifact/references/design.md)
- [Mixture-of-Agents Enhances Large Language Model Capabilities](https://arxiv.org/abs/2406.04692)
- [FrugalGPT](https://arxiv.org/abs/2305.05176)
- [LLM-as-a-Judge / MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685)
- [Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171)
- [Reflexion](https://arxiv.org/abs/2303.11366)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [CLI text or single-document JSON, with markdown-style answer and report content where requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports exact-question caching, session memory, per-stage output caps, budget controls, provenance reports, latency/token metrics, and offline self-test output.]

## Skill Version(s):

1.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
