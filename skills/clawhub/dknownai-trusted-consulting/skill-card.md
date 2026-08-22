## Description:

深知可信咨询 helps an agent answer policy, government service, tax, social security, housing fund, subsidy, licensing, industry standard, compliance, and public-service questions through DKnownAI's trusted consultation API, returning cited answers plus local traceability outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and employees use this skill when they need policy or public-service consultation with source citations and a local traceability report. It is especially relevant for questions involving eligibility conditions, required materials, application paths, amounts, ratios, timing, and compliance risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Consultation questions are sent to a remote DKnownAI service, while the skill text may create an overly broad privacy expectation.

Mitigation: Review the publisher's data transmission, retention, and local-storage terms before using the skill with sensitive personal, business, or legal-policy materials.

Risk: The skill may request phone verification to obtain an API key.

Mitigation: Use it only when phone verification is acceptable for the deployment context, and avoid exposing full API keys in chat, files, logs, or command arguments.

Risk: Policy and compliance answers can affect decisions if sources are stale, incomplete, or misapplied.

Mitigation: Require cited source review for consequential advice and treat unsupported conclusions as needing further verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-trusted-consulting)
- [README](artifact/README.md)
- [Consultation introduction](artifact/reference/consult_intro.md)
- [Sample consultation answer](artifact/reference/sample_consult_answer.md)
- [Sample traceability report](artifact/reference/sample_trace_report.html)
- [Trusted consultation API endpoint](https://open.dknowc.cn/chat/trusted/unification)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Cited text answer with source list, local HTML traceability report, and clean Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY from the environment before trusted consultation can run; generated consultation artifacts are written under official-docs/search-results and official-docs/output.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
