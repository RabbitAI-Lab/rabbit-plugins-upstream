## Description: <br>
Deprecated WeChat article extraction skill that helps agents parse WeChat Official Account article URLs or supplied HTML into article metadata, account details, content HTML, cover URLs, and error status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golikegod](https://clawhub.ai/user/golikegod) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent users use this skill to extract structured metadata and article content from WeChat Official Account links or previously fetched HTML. The release is deprecated and points users to the maintained yuanzi-wechat-suite replacement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is deprecated and no longer maintained. <br>
Mitigation: Prefer the maintained yuanzi-wechat-suite replacement before installing or running this skill. <br>
Risk: The security review reports dynamic JavaScript execution from fetched or user-provided HTML. <br>
Mitigation: Run only in an isolated workspace and avoid feeding arbitrary HTML unless the parser has been reviewed and hardened. <br>
Risk: The security review reports insecure or debug helper scripts. <br>
Mitigation: Avoid running bundled helper scripts and remove or review them before operational use. <br>
Risk: The security review recommends updating abandoned dependencies. <br>
Mitigation: Review and update dependencies before using this skill in a maintained workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/golikegod/skills/wechat-article-extractor-skill) <br>
- [Publisher profile](https://clawhub.ai/user/golikegod) <br>
- [Artifact README](artifact/README.md) <br>
- [Node.js](https://nodejs.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript examples and structured extraction results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Extraction results include success or error status plus fields such as title, author, account metadata, publish time, content HTML, cover URL, and source links.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
