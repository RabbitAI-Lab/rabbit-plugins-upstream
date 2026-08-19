## Description:

Supports academic research, paper reading, related-work discovery, encyclopedia lookup, and citation-chain tracing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and research-assistant agents use this skill to search scholarly sources, read full papers or sections, and inspect references and citations for literature reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries may be sent to multiple external scholarly services.

Mitigation: Use explicit source selections and avoid submitting sensitive or confidential research queries unless external disclosure is acceptable.

Risk: Some crawler fallback paths use browser automation and browser-environment disguise behavior.

Mitigation: Prefer official or non-crawler providers and enable crawler fallbacks only when the Camoufox/Playwright behavior is acceptable.

Risk: The skill can write results to user-supplied output paths.

Mitigation: Use dedicated safe output directories and review generated files before sharing or reusing them.

Risk: DeepXiv SDK behavior can obtain a token automatically.

Mitigation: Provide approved API tokens explicitly where possible and review SDK behavior before use in controlled environments.

## Reference(s):

- [Skill page](https://clawhub.ai/sensenova-skills/skills/sn-search-academic)
- [Publisher profile](https://clawhub.ai/user/sensenova-skills)
- [search.py unified academic search entry](references/search.md)
- [paper.py unified paper reading entry](references/paper.md)
- [refTree.py unified citation tree entry](references/refTree.md)
- [arXiv](https://arxiv.org)
- [papers.cool](https://papers.cool)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files]

**Output Format:** [Markdown guidance with shell commands and JSON script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts report success, error, attempts, and source_results fields; optional output paths write JSON files for long results.]

## Skill Version(s):

2026.8.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
