## Description:

Use when an agent needs a public bounded deterministic W04 trace-integrity verification from supplied redacted JSON evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[slowsleeper1](https://clawhub.ai/user/slowsleeper1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to submit a small redacted expected-versus-observed trace evidence manifest to a public verifier and receive a deterministic trace-integrity result. The result helps identify missing trace IDs or missing links in the supplied evidence without treating absent evidence as proof of runtime failure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive data could be exposed if a user submits secrets, credentials, customer data, production traces, or other sensitive payloads to the public verifier endpoint.

Mitigation: Submit only small redacted trace evidence manifests and exclude secrets, credentials, customer data, production traces, and other sensitive content.

Risk: The verifier compares only supplied evidence, so missing input can produce an incomplete result without proving an actual runtime failure.

Mitigation: Interpret results as bounded evidence checks and confirm that the expected and observed manifests are complete enough for the decision being made.

Risk: Public endpoint rate limiting is nominal and may be enforced in a location-dependent, eventually consistent way.

Mitigation: Keep requests bounded, handle throttling or transient rejection, and avoid depending on a strict globally synchronized request ceiling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/slowsleeper1/skills/soja-trace-evidence-checks)
- [Public W04 trace-integrity verifier endpoint](https://soja-w04-public-evaluate.slowsleeper1.workers.dev/v1/trace-integrity-verifier/evaluate)

## Skill Output:

**Output Type(s):** [Guidance, JSON]

**Output Format:** [Markdown instructions with JSON request and response examples; verifier responses are machine-readable JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bounded redacted JSON evidence manifests up to 64 KiB; no API key is required per the artifact.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
