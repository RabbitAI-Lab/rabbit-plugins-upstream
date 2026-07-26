## Description: <br>
Find the best public route to pan links, magnets, torrents, and public video URLs for movies, TV, anime, music, software, and books. Uses layered success-first retrieval, public HTML/RSS/no-API sources, and direct/actionable/clue result ranking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnbplus](https://clawhub.ai/user/mnbplus) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to search public no-API sources for pan links, magnets, torrents, and public video URLs, then receive ranked direct, actionable, or clue results for follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill queries public torrent, pan, search, and video sites and may return copyrighted or unsafe material. <br>
Mitigation: Use it only for lawful public resources, review returned links before opening or downloading them, and run first uses in a constrained environment. <br>
Risk: Public HTML/RSS sources can drift, throttle, block, or vary by region. <br>
Mitigation: Treat results as best effort, review warnings and source status, and rerun source probes when results look incomplete or stale. <br>
Risk: Bundled raw live-test HTML and JavaScript captures may contain untrusted third-party content. <br>
Mitigation: Do not open captured HTML or JavaScript directly in a browser; inspect them as text or in an isolated analysis environment. <br>
Risk: Some records are clue-only rather than final usable links, including current Dalipan token-only outputs. <br>
Mitigation: Distinguish direct, actionable, and clue records in the output, and require manual follow-up for clue-only results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnbplus/skills/resource-hunter) <br>
- [Source matrix](references/sources.md) <br>
- [Architecture](references/architecture.md) <br>
- [Usage notes](references/usage.md) <br>
- [Release notes 2.1.1](artifacts/RELEASE-NOTES-2.1.1.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-capable command output with search results, source status, warnings, and follow-up guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce quick text summaries or machine-consumable JSON; results may include direct, actionable, and clue-only records.] <br>

## Skill Version(s): <br>
2.1.1 (source: SKILL.md frontmatter, server release metadata, artifact metadata, and pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
