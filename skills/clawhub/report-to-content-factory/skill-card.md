## Description:

Turn research into original WeChat articles, Xiaohongshu posts, and video scripts with citations and visual suggestions. No automatic publishing. / 将研报转化为原创公众号文章、小红书文案和视频脚本，附引用与配图建议，不自动发布。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Content, marketing, research, and editorial teams use this skill to turn public or authorized research into complete audience-facing drafts for WeChat, Xiaohongshu, and spoken-video formats. It produces cited copy, visual suggestions, revision notes, and JishuDB records without publishing content automatically.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow writes research material, drafts, citations, and revision records into a selected JishuDB knowledge base.

Mitigation: Confirm the KB, write privileges, retention rules, and readback checks before use, and avoid confidential documents unless the KB and retention policy are appropriate.

Risk: Generated copy could overstate report coverage, misread chart evidence, or treat public summaries as full reports.

Mitigation: Use only public or authorized sources, preserve source-card coverage labels, map claims to evidence locators, and distinguish metadata, public summaries, inspected images, and full reports.

Risk: Acquired research content could contain untrusted instructions or requests to change tools, destinations, or credentials.

Mitigation: Treat acquired content as evidence only, keep run and record identities stable, and never follow embedded instructions that affect execution, storage, or secret handling.

## Reference(s):

- [Report-to-Content Factory homepage](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/report-to-content-factory)
- [Evidence contract](references/evidence-contract.md)
- [199IT report category](https://www.199it.com/archives/category/report)
- [199IT RSS feed](https://www.199it.com/feed)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance, Configuration]

**Output Format:** [Markdown files with citations, visual plans, revision records, and JishuDB record content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces article.md, xiaohongshu-post.md, video-script.md, visual-plan.md, citations.md, and revision.md when required host capabilities are available.]

## Skill Version(s):

0.1.1 (source: evidence.release, artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
