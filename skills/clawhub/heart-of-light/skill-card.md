## Description:

Opt-in, model-neutral guidance for evidence-aware, dignified AI communication, with a compact response contract and offline deterministic text audit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers, operators, and external users use this opt-in skill to apply evidence-aware communication guidance, produce compact completion contracts, and run a local deterministic text audit without network or host-configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local audit is heuristic and can miss issues or flag benign text.

Mitigation: Treat audit results as advisory, keep human review for consequential claims, and avoid presenting findings as truth or safety guarantees.

Risk: Mode and feedback commands can write local state or feedback files when explicitly invoked.

Mitigation: Review selected file paths before enabling writes, keep paths workspace-scoped unless there is an explicit operator override, and avoid placing secrets in audit text or feedback notes.

Risk: A mutable installer command can change what is installed in sensitive environments.

Mitigation: Use a pinned ClawHub installer command for sensitive deployments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/heart-of-light)
- [Research and Evidence Ledger](references.json)
- [NIST AI Risk Management Framework: Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [OWASP LLM01 Prompt Injection](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM01_PromptInjection.html)
- [JSON Schema 2020-12 Validation](https://json-schema.org/draft/2020-12/json-schema-validation)
- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html)
- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- [OpenAI Reasoning Best Practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices)
- [Contract Schema](https://clawhub.ai/orionshaowswmw/heart-of-light/schemas/contract-v1.json)
- [Audit Schema](https://clawhub.ai/orionshaowswmw/heart-of-light/schemas/audit-v1.json)
- [Feedback Schema](https://clawhub.ai/orionshaowswmw/heart-of-light/schemas/feedback-v1.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance, JSON contract/audit/state/feedback records, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline helper output is deterministic and workspace-scoped; audit findings are heuristic and do not echo input text.]

## Skill Version(s):

3.0.5 (source: server release metadata; artifact frontmatter reports 3.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
