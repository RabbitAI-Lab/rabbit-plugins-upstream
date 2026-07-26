## Description: <br>
Renders approved card content packages into inspected platform-sized PNG or JPG image files with a cards manifest for human confirmation, direct platform upload, or optional public URL preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangchao228](https://clawhub.ai/user/yangchao228) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content creators use this skill after card copy has been approved to produce real social-card image assets for Xiaohongshu, WeChat inline cards, Zhihu Idea images, or generic carousels. It also records visual QA, generation status, human confirmation, and optional public URL preparation in a cards manifest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated image assets may be mistaken for final publish-ready material before human approval. <br>
Mitigation: Keep human confirmation pending until every image is inspected and the user explicitly approves the assets. <br>
Risk: Generative or mixed rendering can introduce inaccurate text, numbers, logos, interfaces, or unsupported claims. <br>
Mitigation: Prefer deterministic layers for exact text and source-backed relationships, inspect each rendered image, revise failures, and route unsupported claims back to review. <br>
Risk: Public URL preparation or upload could expose local assets before the user intends to publish them. <br>
Mitigation: Use the default local asset policy unless stable public URLs are required, and require explicit confirmation before upload or URL rewrite. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yangchao228/skills/cards-to-images) <br>
- [Source homepage](https://github.com/yangchao228/my_open_skills/tree/main/skills/content/cards-to-images) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown delivery summary with local PNG or JPG image files and a cards-manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes platform profile, render strategy, generation backend, visual QA status, human confirmation status, asset URL policy, R2 state, and public URL state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
