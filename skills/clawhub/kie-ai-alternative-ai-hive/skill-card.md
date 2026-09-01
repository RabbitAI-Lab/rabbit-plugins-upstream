## Description:

This skill helps AIGC, ecommerce, advertising, and developer teams assess and plan a testable migration or fallback route from Kie.ai-style generative media API aggregation to AI-HIVE, including capability mapping, routing choices, runnable examples, task records, and acceptance criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and business teams use this skill to inventory current AI media API usage, compare Kie.ai-oriented workflows with AI-HIVE, run small non-production image or video samples, and prepare a staged migration with rollback and acceptance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad automatic activation is paired with API-key setup and AI-HIVE media generation workflows.

Mitigation: Install only when AI-HIVE migration or media-generation assistance is intended, and require explicit user approval before API-key setup, uploads, generation calls, polling, or downloads.

Risk: API keys may be stored for repeated CLI use.

Mitigation: Prefer environment variables for sensitive keys, avoid production secrets during evaluation, review local key storage, and confirm revocation controls before operational use.

Risk: Generated media calls and uploads may involve user assets, platform costs, retention rules, and third-party terms.

Mitigation: Use non-production or authorized assets for initial samples, verify AI-HIVE terms, pricing, retention, and billing before use, and keep task logs for review.

Risk: Migration recommendations could be misleading if based on stale pricing, model availability, or claims about another platform.

Mitigation: Follow the skill's comparison boundary: re-check current documentation, contracts, price snapshots, and same-input samples before making production decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/kie-ai-alternative-ai-hive)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base](https://ai-hive.iclip.cn/api)
- [Kie.ai evidence page](https://kie.ai/seedance-2-5)
- [Platform source and comparison boundary](references/platform.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON files, runnable shell commands, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create migration audit files, blueprint JSON, AI-HIVE task records, and downloaded generated media when the user runs the provided scripts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
