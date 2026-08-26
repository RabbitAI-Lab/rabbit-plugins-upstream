## Description:

Weekly viral-topic library for AI video creators. Collects public trend signals from TikTok / Reels / Shorts, extracts non-copyright structure (hook, pacing, visual keywords, camera), maps a generator-ready prompt pack, and grades topics. Use when the user says generate this week's topic library, run the topic library, weekly content production, or viral teardown plus prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fsn021920-prog](https://clawhub.ai/user/fsn021920-prog)

### License/Terms of Use:

Creative Commons Attribution-ShareAlike 4.0 International

## Use Case:

External creators and developers use this skill to research current public short-video trend signals, turn non-copyright structures into text-to-video prompt packs, and export a weekly topic library for AI video production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated trend briefs or prompts could accidentally reuse protected IP, real-person likenesses, captions, audio, trademarks, or misleading viral-performance claims.

Mitigation: Review outputs before public use; keep only non-copyright structure, drop protected IP or real-person likenesses, avoid copied captions/audio, preserve platform AI labels, and treat grades as editorial filters.

Risk: The skill asks an agent to search the public web and write local Markdown and JSON files.

Mitigation: Install only when public-web research and local file creation are expected, and review generated files for copyright, likeness, trademark, and AI-label compliance before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fsn021920-prog/skills/weekly-topic-library-generator)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance, Files]

**Output Format:** [Markdown and JSON files with topic teardown, prompt packs, grades, risk flags, and suggested generators]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes weekly-topic-library-[Year]W[WeekNumber].md and weekly-topic-library-[Year]W[WeekNumber].json in the working directory after the user confirms the library.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata; artifact README lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
