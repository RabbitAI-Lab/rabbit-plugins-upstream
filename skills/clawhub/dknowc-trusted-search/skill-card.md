## Description:

深知可信搜索（法律、政策、标准） helps agents retrieve and verify authoritative legal, policy, standards, government-service, subsidy, tax-benefit, and compliance materials through DKnowC trusted and deep search services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need sourced answers, policy research, standards lookup, city policy comparison, subsidy or tax-benefit verification, or compliance evidence. It is intended for search-backed answers with clickable provenance HTML and clean Markdown, not unsupported legal or policy advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles phone-based MaaS API-key setup and can return an API key for the current task.

Mitigation: Use DKNOWC_API_KEY through the environment, do not display the full key, keep registration results current-task only unless the user explicitly consents to persistence, and review or revoke keys when no longer needed.

Risk: The trusted-search and deep-search endpoints can be overridden, which could send queries or keys to an unintended endpoint.

Mitigation: Keep the default DKnowC endpoints and avoid --endpoint or endpoint override environment variables unless the operator has reviewed the destination.

Risk: Legal, policy, standards, subsidy, and compliance outputs may be misleading if facts are unsupported or citations are mismatched.

Mitigation: Require source-backed citation markers, clickable provenance HTML, and review of generated answers before relying on them for decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-trusted-search)
- [ClawHub publisher profile](https://clawhub.ai/user/dylanzhangzx)
- [DKnowC MaaS platform](https://platform.dknowc.cn/)
- [DKnowC Open API base](https://open.dknowc.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, HTML, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown answer plus local clickable-provenance HTML, clean Markdown, optional visualization HTML/SVG, and JSON intermediate files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY. Search and rendering artifacts are scoped to official-docs/search-results and official-docs/output.]

## Skill Version(s):

1.1.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
