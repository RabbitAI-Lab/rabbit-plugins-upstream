## Description:

Clinical Trial Chief Advisor is a conversational advisor for clinical-trial methodology, regulatory evidence, design, compliance, QC, tone, sample-size handoff, and routed registry, safety, and literature intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical-trial practitioners, clinicians, nurses, medical students, and supporting developers use this skill to ask plain-language questions about study design, regulatory interpretation, operations, safety, QC, competitive intelligence, and sample-size workflows across the clinical-development lifecycle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clinical-trial questions, metadata, and local draft answers may be sent to the author-hosted Coze endpoint, and the security evidence notes incomplete runtime consent and inconsistent persistence disclosures.

Mitigation: Install only if external analysis is acceptable, avoid patient data, unpublished sponsor data, trade secrets, credentials, and regulated confidential material, and review config.json before use if runtime confirmation is required.

Risk: Requests include a stable hashed machine identifier for audit, attribution, or rate limiting.

Mitigation: Use the skill only in environments where stable per-machine attribution is acceptable, and avoid shared or regulated machines unless local policy permits this telemetry.

Risk: Local memory or Q&A logging settings could persist sensitive prompts if enabled.

Mitigation: Keep qa_store in noop mode unless local logging is explicitly needed, and treat any local Q&A log as sensitive data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/medstatstar/skills/ct-advisor)
- [Project Homepage](https://github.com/medstatstar/ct-advisor)
- [README](README.md)
- [Workflow Steps](references/steps.md)
- [Reference Index](knowledge/reference-index.md)
- [ClawHub Audit Trace](docs/clawhub_audit_trace_20260815.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text responses, with code, shell commands, configuration snippets, and structured guidance when the task calls for them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source labels, verification warnings, routed sibling-skill results, and bilingual English or Chinese output.]

## Skill Version(s):

0.9.69 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
