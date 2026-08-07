## Description:

story-short-analyze guides agents through a Chinese short-story analysis workflow that identifies genre, structure, emotional arcs, twists, writing techniques, and resonance, then writes reusable Markdown reports and metadata for downstream story drafting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and agent developers use this skill to analyze short-form Chinese web fiction that they have the right to process, producing structured story analysis, reusable craft notes, and metadata for a downstream writing workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill saves local copies of user-provided fiction and generated analysis under 拆文库/{书名}/.

Mitigation: Use it only with works the user has the right to analyze, provide only the intended file path or pasted text, and review or remove local backups according to the user's data-handling needs.

Risk: The analysis output can be reused by a downstream writing workflow and may preserve too much of a source story's structure, voice, or protected expression if used carelessly.

Mitigation: Review downstream use for originality, avoid copying specific plot expression or passages, and treat the analysis as craft guidance rather than a license to reproduce the source.

Risk: The skill may analyze fictional abuse, violence, revenge, infidelity, and other dark genre elements.

Mitigation: Keep outputs framed as literary criticism and writing analysis, and do not convert fictional material into real-world instructions or endorsement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-short-analyze)
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [Output contract](references/output-contract.md)
- [Output templates](references/output-templates.md)
- [Short-story decomposition methodology](references/material-decomposition.md)
- [Quality checklist](references/quality-checklist.md)
- [Anti-AI-writing report check](references/anti-ai-writing.md)
- [Banned words](references/banned-words.md)
- [Genre catalog](references/genre-catalog.md)
- [Genre core mechanics](references/genre-core-mechanics.md)
- [Genre readers](references/genre-readers.md)
- [Genre writing formulas](references/genre-writing-formulas.md)
- [Genre writing techniques](references/genre-writing-techniques.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, guidance]

**Output Format:** [Markdown reports and JSON metadata written to local files, with concise conversational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a source-text backup, analysis report, plot-node report, writing-technique report, and _meta.json under a per-title directory.]

## Skill Version(s):

1.1.13 (source: server release metadata; artifact frontmatter says 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
