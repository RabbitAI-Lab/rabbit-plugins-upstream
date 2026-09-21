## Description:

Discovers, deduplicates, evaluates, and exports evidence-backed concepts from one URL or an author pool. Invoke for ad hoc or recurring concept research; publishing is optional.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and strategy teams use this skill to scan a single URL or configured author pool, filter candidate ideas against evidence and quality criteria, and export concise concept cards for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches configured web and GitHub sources and writes local state under .trae/concept-radar.

Mitigation: Use trusted feeds and URLs, review source configuration before recurring scans, and keep runtime state out of release packages.

Risk: Optional Feishu publishing can send externally sourced, unescaped Markdown as the user.

Mitigation: Publish only after explicit user request, review generated Markdown before sending, and prefer trusted sources whose titles and links are unlikely to alter message formatting.

## Reference(s):

- [Evidence Policy](references/evidence-policy.md)
- [Quality Rubric](references/quality-rubric.md)
- [State Contract](references/state-contract.md)
- [Concept Radar Selection Schema](references/card-schema.json)
- [Andrej Karpathy: LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON files, with shell commands and configuration guidance for scanning, validation, export, and optional publishing.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default exports are concept-radar.md and concept-radar.json under the runtime directory; Feishu publishing is optional and requires explicit user request.]

## Skill Version(s):

0.1.0 (source: server release evidence and CHANGELOG, released 2026-09-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
