## Description:

Opt-in, model-neutral guidance for evidence-aware, dignified AI communication, with a compact response contract and offline deterministic text audit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and operators use this skill when they want opt-in communication guidance that separates evidence, inference, uncertainty, and next actions. It can also help generate compact JSON or Markdown completion contracts and run a local deterministic text audit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented npx installation command can retrieve mutable registry code.

Mitigation: Use a pinned ClawHub client version or install in a controlled environment before deployment.

Risk: State, audit, and feedback paths are local operator choices, and notes or inputs may contain sensitive material.

Mitigation: Review selected paths, keep files workspace-scoped unless an outside path is intentional, and avoid placing secrets in feedback notes, prompts, filenames, or contracts.

Risk: The text audit is heuristic and can be mistaken for a truth, safety, or policy guarantee.

Mitigation: Treat audit results as advisory and require contextual review for consequential claims or high-stakes decisions.

Risk: The helper does not sandbox the surrounding host agent or tools.

Mitigation: Use host-level permission controls and review any action that relies on tools outside this skill.

## Reference(s):

- [NIST AI Risk Management Framework: Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [OWASP LLM01:2025 Prompt Injection](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM01_PromptInjection.html)
- [JSON Schema 2020-12 Validation](https://json-schema.org/draft/2020-12/json-schema-validation)
- [RFC 8259 JSON](https://www.rfc-editor.org/rfc/rfc8259.html)
- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- [OpenAI Reasoning Best Practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices)
- [Heart of Light Contract Schema](https://clawhub.ai/orionshaowswmw/heart-of-light/schemas/contract-v1.json)
- [Heart of Light Audit Schema](https://clawhub.ai/orionshaowswmw/heart-of-light/schemas/audit-v1.json)
- [Heart of Light Feedback Schema](https://clawhub.ai/orionshaowswmw/heart-of-light/schemas/feedback-v1.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance, JSON records, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce workspace-scoped state or feedback files only when explicitly invoked; audits hash input and do not echo audited text.]

## Skill Version(s):

3.0.2 (source: SKILL.md frontmatter, README.md, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
