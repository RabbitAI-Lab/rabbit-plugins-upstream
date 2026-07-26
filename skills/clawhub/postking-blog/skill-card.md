## Description: <br>
Create blog publications and generate, iterate on, and publish articles on PostKing, either hosted or pushed to WordPress, Medium, or Substack. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bitsandtea](https://clawhub.ai/user/bitsandtea) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams, content operators, and agents use this skill to create PostKing blog publications, generate and revise articles, and publish or schedule them to hosted blogs or connected WordPress, Medium, or Substack destinations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing and deletion actions can change live blog content. <br>
Mitigation: Review article IDs, status changes, and destinations before publishing, scheduling, pushing to external platforms, or deleting articles. <br>
Risk: External publishing can push content to connected WordPress, Medium, or Substack accounts. <br>
Mitigation: List publishing connections first and verify connection IDs before calling external publish actions. <br>
Risk: Async article generation may still be running when a follow-up action is requested. <br>
Mitigation: Poll job or article status until completion or failure before reviewing, editing, publishing, or deleting the generated article. <br>


## Reference(s): <br>
- [PostKing MCP endpoint](https://mcp.postking.app/mcp) <br>
- [PostKing Blog skill page](https://clawhub.ai/bitsandtea/skills/postking-blog) <br>
- [PostKing Blog icon](https://raw.githubusercontent.com/bitsandtea/postking-skills/main/assets/icons/postking-blog.svg) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, MCP tool calls, Shell commands, Text] <br>
**Output Format:** [Markdown guidance with MCP tool-call examples and CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an active PostKing brand; external publishing requires connected WordPress, Medium, or Substack accounts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
