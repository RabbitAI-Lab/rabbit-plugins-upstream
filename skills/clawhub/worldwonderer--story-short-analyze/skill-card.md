## Description:

Analyzes popular short web fiction by extracting story core, structure, emotional arc, reversals, writing techniques, character function, resonance layers, and reusable patterns into local analysis artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and story-development agents use this skill to analyze legally held short fiction and produce reusable critique for later short-story drafting workflows. It is aimed at Chinese short web-fiction formats such as Fanqie short fiction, Zhihu Yanxuan-style stories, revenge, rebirth, melodrama, and social-family drama.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates local analysis files and stores a copy of the source text.

Mitigation: Run it only on texts the user is allowed to analyze, choose an appropriate output directory, and review the generated source backup and metadata before reuse.

Risk: Genre references include strong market and ideological assumptions that may bias critique.

Mitigation: Review the final analysis report when neutral literary criticism, classroom use, or editorial review is required.

Risk: Outputs are intended to feed later writing workflows and may carry forward mistakes from the analysis.

Mitigation: Check the markdown reports and JSON metadata before using them as inputs for downstream drafting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-short-analyze)
- [OpenClaw metadata source](https://github.com/worldwonderer/oh-story-claudecode)
- [Output contract](references/output-contract.md)
- [Output templates](references/output-templates.md)
- [Short fiction decomposition methodology](references/material-decomposition.md)
- [Quality checklist](references/quality-checklist.md)
- [AI-style self-check guide](references/anti-ai-writing.md)
- [Banned words and sentence patterns](references/banned-words.md)
- [Genre catalog](references/genre-catalog.md)
- [Genre core mechanics](references/genre-core-mechanics.md)
- [Genre readers](references/genre-readers.md)
- [Genre writing formulas](references/genre-writing-formulas.md)
- [Genre writing techniques](references/genre-writing-techniques.md)
- [Character basics](references/character-basics.md)
- [Character design methods](references/character-design-methods.md)
- [Character relations](references/character-relations.md)
- [Chapter hooks](references/hooks-chapter.md)
- [Paragraph hooks](references/hooks-paragraph.md)
- [Suspense hooks](references/hooks-suspense.md)
- [Deconstruction examples](references/deconstruction-examples.md)
- [Zhihu-style reference](references/zhihu-style.md)
- [Short web-fiction market reference](references/real-market-data.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, JSON, files, guidance]

**Output Format:** [Markdown reports and JSON metadata written to a local analysis directory]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a local source backup and staged outputs including analysis report, plot nodes, writing-technique notes, and metadata.]

## Skill Version(s):

1.1.14 (source: ClawHub release metadata; artifact frontmatter says 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
