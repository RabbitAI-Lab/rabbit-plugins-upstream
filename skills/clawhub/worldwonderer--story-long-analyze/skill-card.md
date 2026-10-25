## Description:

分析长篇网络小说的开篇、逐章情节、因果与时间线、节奏、角色情感、设定和文风，并支持复用已有成果与断点续跑。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Authors and writing teams use this skill to analyze a supplied long-form novel, produce chapter-level and cross-chapter reports, and identify reusable storytelling techniques without copying the source work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads the selected novel and project files and writes analysis outputs in the book workspace, with optional inspiration-library and topic-decision updates.

Mitigation: Confirm the selected book workspace and review the files that may be updated before running the analysis.

Risk: Reruns and chapter-index maintenance may move old outputs or call for removal of generated summaries and caches.

Mitigation: Check the target directory and preserve any outputs you need before rerunning or rebuilding the index.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/story-long-analyze)
- [Project link supplied in skill metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Opening-chapter analysis](references/stage1-golden-chapters.md)
- [Plot and pacing analysis](references/stage3-plot-rhythm.md)
- [Report structure](references/stage5-report.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Text, Guidance]

**Output Format:** [Chinese-language Markdown reports and chapter notes, with a CSV chapter index]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a progress record and optional inspiration-library outputs for resumable analysis.]

## Skill Version(s):

1.1.31 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
