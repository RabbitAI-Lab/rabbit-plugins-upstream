## Description:

Build typed Jev and local-model decision harnesses for routing, ranking, verification, extraction, bounded scoring, confidence-aware workflows, and evaluation plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiwithenoch](https://clawhub.ai/user/aiwithenoch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design typed Jev questions, integrate TypeSafe or local-model providers, and evaluate Noul, Choice, and Score decisions with calibration, abstention, and CI gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Evaluation state and question data can be sent to configured model endpoints during remote provider tests.

Mitigation: Review JSON and JSONL cases before running remote tests, keep API keys in environment variables, and avoid confidential golden sets unless the provider and privacy approvals permit them.

Risk: Confidence, consensus, verifier support, and local-model probabilities can be mistaken for proof of correctness.

Mitigation: Tune thresholds on representative labeled cases, keep uncertain cases routed to review, and compare local providers against a pinned Jev benchmark.

## Reference(s):

- [Jev Skill Repository](https://github.com/aiwithenoch/Jev-Skill)
- [Jev Evaluation Harness](references/harness.md)
- [Jev Skill Research Notes](references/research-notes.md)
- [TypeSafe Documentation Index](https://docs.typesafe.ai/llms.txt)
- [TypeSafe Quick Start](https://docs.typesafe.ai/introduction/quickstart.md)
- [TypeSafe Primitives](https://docs.typesafe.ai/primitives.md)
- [TypeSafe Confidence](https://docs.typesafe.ai/confidence.md)
- [TypeSafe HTTP API](https://docs.typesafe.ai/api.md)
- [OpenJev Local Scorer](https://github.com/daseinlabs/open-jev)
- [Official TypeSafe Agent Skill](https://github.com/typesafe-ai/skills/tree/main/skills/typesafe-ai)
- [TypeSafe Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python)
- [TypeSafe JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js)
- [ClawHub Skill Page](https://clawhub.ai/aiwithenoch/skills/jev-skill)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce question maps, JSONL case examples, harness commands, integration code, and evaluation guidance.]

## Skill Version(s):

1.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
