## Description:

Use this skill when the user wants to analyze, design, optimize, recreate-in-spirit, or batch-produce thumbnails/covers for Bilibili, YouTube, Xiaohongshu, Douyin, WeChat Channels, public-account articles, courses, AI tools, knowledge IP, or product content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tobewin](https://clawhub.ai/user/tobewin)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, course teams, product teams, and agents use this skill to turn titles, platform targets, reference covers, portraits, and campaign goals into thumbnail strategy, no-text image prompts, post-production layout guidance, batch briefs, and quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portrait and reference-image workflows can generate detailed likeness and style-direction prompts.

Mitigation: Use user-authorized portraits and references, review likeness and style use carefully, and follow the skill boundary against identifying real people or copying protected designs.

Risk: Helper scripts read user-directed files and write generated reports or briefs.

Mitigation: Run scripts only against intended local inputs and review generated Markdown or JSON before sharing or publishing.

Risk: Cover strategy advice could be mistaken for guaranteed performance improvement.

Mitigation: Treat outputs as strategy, prompt, layout, and QC guidance; the artifact states that it does not promise viral results or predict click-through rate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tobewin/skills/covercraft-skill)
- [Server-resolved source repository](https://github.com/ToBeWin/covercraft-skill)
- [Artifact README](artifact/README.md)
- [Output contract](artifact/templates/output_contract.md)
- [Quality report](artifact/QUALITY_REPORT.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, JSON, shell commands, and structured guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local helper scripts can produce batch cover briefs, prompt packs, and technical QC reports from user-directed files.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
