## Description: <br>
Builds platform-specific publish packages and verifies titles, summaries, captions, tags, image readiness, public URLs, human confirmation, and release blockers for reviewed content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangchao228](https://clawhub.ai/user/yangchao228) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content teams, writers, and publishing agents use this skill to prepare preflight publish packages and final release checks for WeChat, Zhihu, Zhihu Idea, Xiaohongshu, blog, or multi-platform drafts after content review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A publish package could imply content is ready when required facts, platform bodies, images, public URLs, or permissions are incomplete. <br>
Mitigation: Keep explicit blockers and use blocked or needs_review until all required artifacts and checks are complete. <br>
Risk: Card images or public assets could be treated as publish-ready without real files, manifest checks, visual QA, or human confirmation. <br>
Mitigation: Verify manifest paths, image counts, dimensions, order, per-image visual QA, and recorded human confirmation before marking ready_to_publish. <br>
Risk: Public artifacts could expose private paths, credentials, internal notes, or account details. <br>
Mitigation: Review generated publishing materials before any external upload or post and remove private details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yangchao228/skills/wenchang-publish-check) <br>
- [Project homepage](https://github.com/yangchao228/my_open_skills/tree/main/skills/content/wenchang-publish-check) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown publish package with structured status fields and content_state update guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not generate images, upload files, or publish externally; final mode requires human confirmation before ready_to_publish.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
