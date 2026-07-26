## Description: <br>
Automates security news collection, Korean security blog post generation with GLM-4.7, draft publication to Notion, and approved deployment to GitHub Pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rebugui](https://clawhub.ai/user/rebugui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content operators use this skill to collect security news, generate draft blog posts, publish drafts to Notion, and deploy approved posts to a GitHub Pages-backed blog. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically publish to Notion or GitHub and mutate a local blog repository. <br>
Mitigation: Use a dedicated blog repository, scoped credentials, verified BLOG_REPO_PATH or BLOG_LOCAL_PATH values, and manual review or dry-run checks before any git push or public deployment. <br>
Risk: Broad cron or background service use could publish or deploy content before the workflow is fully validated. <br>
Mitigation: Avoid unattended scheduling until the pipeline has been tested end to end with the intended repository, Notion database, and approval workflow. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/rebugui/auto-sec-blogger-repo) <br>
- [Architecture reference](references/architecture.md) <br>
- [GLM API documentation](https://open.bigmodel.cn/dev/api) <br>
- [Notion API documentation](https://developers.notion.com/) <br>
- [Jekyll documentation](https://jekyllrb.com/docs/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, Python code snippets, shell commands, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create blog post files, Notion drafts, Git commits, and deployment-triggering pushes when configured with credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
