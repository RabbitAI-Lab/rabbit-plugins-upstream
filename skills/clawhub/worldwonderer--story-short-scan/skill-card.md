## Description:

短篇网文扫榜。分析知乎盐言、七猫、黑岩、点众等平台热门短篇数据，捕捉风口题材。触发方式：/story-short-scan、/短篇扫榜、「短篇什么火」「知乎故事排行」。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers use this skill to review short fiction listings and author-provided rankings, compare themes and reader-facing emotional hooks, and develop topic ideas suited to a selected platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious with medium confidence; it reports behavior outside the stated trend-scanning purpose, and only 7 of 11 components were fully inspected.

Mitigation: Review the complete scanner findings and the components that were not fully analyzed; defer installation until the reported mismatch is understood.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/story-short-scan)
- [GitHub URL listed in OpenClaw metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Manual rank input guide](artifact/references/manual-rank-input.md)
- [Dianzhong platform guide](artifact/references/platform-dianzhong.md)
- [Heiyan platform guide](artifact/references/platform-heiyan.md)
- [Historical market data](artifact/references/real-market-data.md)
- [Topic matching and handoff guide](artifact/references/topic-match.md)
- [Dianzhong short fiction listings](https://www.ishugui.com/browse)
- [Dianzhong female fiction listings](https://www.ishugui.com/browse/on3)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, Guidance]

**Output Format:** [Markdown reports and saved rank-data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Platform-dependent analysis; reports identify sample date, coverage, confidence, and a suggested rescan date. Rankings and interactions indicate attention, not story quality.]

## Skill Version(s):

1.1.25 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
