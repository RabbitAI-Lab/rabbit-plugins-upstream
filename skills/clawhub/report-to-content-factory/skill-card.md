## Description:

Turns industry-report evidence into original WeChat articles, Xiaohongshu posts, and short-video scripts with citations and visual suggestions, retaining evidence and revisions in JishuDB.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and marketing teams use this skill to turn authorized industry research into evidence-backed, platform-specific drafts and traceable citations. JishuDB setup and approved retention of source evidence and revisions are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: JishuDB setup and retention of source materials, drafts, and revisions require user approval.

Mitigation: Review the release, installation paths, endpoint, client configuration, publisher details, and retention scope before approving setup or source transfer.

Risk: Windows installation has an explicitly unsigned-installer posture.

Mitigation: Review and explicitly approve the Windows installer transaction before execution.

Risk: Research-derived content can misstate findings or reuse material without adequate attribution.

Mitigation: Review claims against retained evidence and citations, and respect source access and reuse rights before publication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bowen-aijishu/skills/report-to-content-factory)
- [Skill homepage listed in metadata](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/report-to-content-factory)
- [Report discovery and evidence contract](references/evidence-contract.md)
- [Bundled JishuDB setup guide](references/jishudb-setup/setup.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown drafts, citations, revision notes, and optional visual plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces requested article, post, or spoken-video script drafts; does not publish content or generate finished covers.]

## Skill Version(s):

0.1.8 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
