## Description: <br>
Publish web content to Cloudflare Pages with account and project selection, new project creation, and deployment of HTML or static asset directories using Cloudflare API token authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drodecker](https://clawhub.ai/user/drodecker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to publish generated or existing static web content to Cloudflare Pages, including selecting accounts and projects, creating a new project, and returning deployment results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish or update live Cloudflare Pages sites. <br>
Mitigation: Confirm the Cloudflare account, project, branch, and production intent before deployment. <br>
Risk: Cloudflare API tokens grant deployment authority. <br>
Mitigation: Use a least-privilege Pages token and validate that it is intended for the selected account and project. <br>
Risk: The skill is scoped to static content, not server-side logic or complex build pipelines. <br>
Mitigation: Use a dedicated Worker, Functions, or build workflow for dynamic behavior or custom build requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drodecker/skills/clawflare) <br>
- [Server-resolved GitHub import provenance](https://github.com/drodecker/clawflare.publish/tree/main/skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured deployment results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Deployment responses should surface the live URL, deployment ID, and status when available.] <br>

## Skill Version(s): <br>
0.1.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
