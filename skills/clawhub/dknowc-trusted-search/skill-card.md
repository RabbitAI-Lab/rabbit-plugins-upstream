## Description:

dknowc trusted search retrieves and verifies authoritative sources for laws, policies, standards, government-service evidence, compliance, subsidies, tax-benefit, and policy research tasks, returning sourced answers with clickable provenance and clean Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and policy analysts use this skill to retrieve and cross-check authoritative legal, policy, standards, and government-service materials. It is intended for evidence-backed answers that include source-linked provenance HTML and clean Markdown deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and included policy or business context are sent to dknowc remote services.

Mitigation: Use the skill only when the provider's privacy terms are acceptable, and avoid submitting sensitive private documents or confidential facts in search prompts.

Risk: Endpoint override options could redirect queries or API keys away from the default dknowc endpoints.

Mitigation: Use the default service endpoints in normal operation and review any endpoint override before running search or deep-search commands.

Risk: The skill requires a DKNOWC API key and registration flow can return a key for the current task.

Mitigation: Treat returned API keys as secrets, do not expose full keys to users, and persist them only with explicit user consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-trusted-search)
- [Publisher profile](https://clawhub.ai/user/dylanzhangzx)
- [DKNOWC platform](https://platform.dknowc.cn/)
- [DKNOWC Open API](https://open.dknowc.cn/)
- [Search introduction reference](artifact/reference/search_intro.md)
- [Sample search result](artifact/reference/sample_search_result.md)
- [Sample trace report](artifact/reference/sample_trace_report.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown, HTML, and JSON files with concise guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final deliverables can include a direct answer, clickable provenance HTML, clean Markdown, search-result JSON, and optional self-contained policy visualization HTML or SVG.]

## Skill Version(s):

1.1.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
