## Description: <br>
Creates, quality-checks, and publishes novels to FireSeed through HTTP API workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sanzhishuyuan](https://clawhub.ai/user/sanzhishuyuan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers and agent users use this skill to plan long-form fiction, generate chapters with built-in quality checks, publish chapters to FireSeed, and inspect or continue existing works. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish novels and chapters to FireSeed automatically on the user's behalf. <br>
Mitigation: Use it only when that publishing authority is intended, and review generated content before publication whenever possible. <br>
Risk: Authentication material could be exposed if passwords or tokens are shared casually or passed in URLs. <br>
Mitigation: Provide a scoped token through secure configuration, prefer Authorization headers, and avoid sharing passwords or URL token parameters in chat. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sanzhishuyuan/skills/fireseed-auto-novel-publish) <br>
- [Server-resolved GitHub provenance](https://github.com/sanzhishuyuan/fireseed-auto-novel-publish) <br>
- [FireSeed Platform](https://fireseed.online) <br>
- [Gitee mirror listed by artifact](https://gitee.com/topofthesky/ai-novel-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown prose with API request examples and structured progress summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update novels, chapters, covers, feedback events, task submissions, and FireSeed account state when authorized.] <br>

## Skill Version(s): <br>
2.3.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
