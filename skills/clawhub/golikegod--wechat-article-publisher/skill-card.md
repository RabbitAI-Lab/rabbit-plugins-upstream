## Description: <br>
Deprecated WeChat Official Account publishing skill that turns Markdown or HTML articles into styled WeChat drafts, uploads local images, prepares cover media, and can optionally submit drafts for publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golikegod](https://clawhub.ai/user/golikegod) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content operators use this skill to prepare WeChat Official Account drafts from Markdown or HTML, including image upload, cover handling, and optional publish submission. The release is deprecated and redirects users toward yuanzi-wechat-suite. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload article content and images to WeChat using account credentials. <br>
Mitigation: Run with --dry-run first and review the generated preview before allowing API uploads or publication. <br>
Risk: Immediate publication may occur when --publish is used after draft creation. <br>
Mitigation: Avoid --publish unless the draft has already been reviewed and the account is intended for live posting. <br>
Risk: Credential and token handling relies on local configuration, environment variables, keyring, and .token_cache.json. <br>
Mitigation: Prefer keyring or environment secrets, keep credentials out of config.json, and delete or protect .token_cache.json after use. <br>
Risk: Dependency installation is performed by a script using Python packages from requirements.txt. <br>
Mitigation: Install in an isolated virtual environment and review pinned dependency versions before running the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/golikegod/skills/wechat-article-publisher) <br>
- [Metadata homepage](https://github.com/victor-skills/wechat-article-publisher) <br>
- [Publisher profile](https://clawhub.ai/user/golikegod) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Files] <br>
**Output Format:** [Markdown guidance and shell commands; runtime script output is JSON and may create preview HTML files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Python dependencies and WeChat account credentials; dry-run mode avoids WeChat API calls and writes a local preview HTML file.] <br>

## Skill Version(s): <br>
2.1.2 (source: server release evidence; artifact frontmatter reports 2.1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
