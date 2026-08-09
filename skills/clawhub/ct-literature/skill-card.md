## Description:

Searches public scholarly literature across OpenAlex, Europe PMC, and optional Semantic Scholar, normalizes records into a de-duplicated evidence base, and produces literature evidence reports with optional safety-focused subsets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

Clinical-trial, medical, and regulatory users use this skill to retrieve and summarize published literature for trial-planning background, protocol or CSR introductions, systematic-review preparation, and qualitative published-safety checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search topics and filters may be sent to public bibliographic APIs.

Mitigation: Use only non-confidential topics and confirm that public API transmission is acceptable before running searches.

Risk: The skill handles API keys and includes reversible .env key obfuscation.

Mitigation: Prefer environment variables or a real secret manager, do not package .env files, and do not rely on reversible obfuscation as protection.

Risk: Published safety literature is qualitative and not a substitute for structured safety signal analysis.

Mitigation: Use safety-focused literature output as background evidence only and verify conclusions against appropriate safety and regulatory sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-literature)
- [Publisher profile](https://clawhub.ai/user/medstatstar)
- [references/sop.md](references/sop.md)
- [references/search_menu.md](references/search_menu.md)
- [references/multi-db-search.md](references/multi-db-search.md)
- [references/openalex_key.md](references/openalex_key.md)
- [Homepage](https://github.com/medstatstar/ct-literature)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON, Markdown, Excel, and HTML report files produced by the skill's scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call public bibliographic APIs when execution is confirmed; reports are intended for reference and should be verified before regulatory use.]

## Skill Version(s):

0.5.3 (source: server evidence, frontmatter, changelog; released 2026-08-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
