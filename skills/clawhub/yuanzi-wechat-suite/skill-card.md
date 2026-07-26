## Description: <br>
Yuanzi Wechat Suite helps an agent run an end-to-end WeChat Official Account article workflow, including article extraction, prose drafting guidance, image generation, validation, and draft publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golikegod](https://clawhub.ai/user/golikegod) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operators, developers, and agents use this skill to prepare WeChat Official Account posts from source article review through prose checks, supporting images, and draft creation. It is most useful when a human will review credentials, generated content, and live WeChat publishing actions before release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can interact with a real WeChat Official Account and create live drafts or publishing actions. <br>
Mitigation: Use dry-run first and require human confirmation before any live draft or publish operation. <br>
Risk: WeChat API credentials and cached access tokens may be exposed if stored in local configuration or left behind after use. <br>
Mitigation: Store secrets in keyring, avoid plaintext config secrets, and delete token caches after publishing work is complete. <br>
Risk: Extractor and screenshot helpers may process untrusted URLs, paths, or HTML. <br>
Mitigation: Run the skill in a dedicated workspace and avoid untrusted inputs until those helpers are hardened. <br>
Risk: Generated content or transformed article material may be incorrect, outdated, or unsuitable for publication. <br>
Mitigation: Review extracted content, generated prose, images, and final WeChat drafts before release. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/golikegod/skills/yuanzi-wechat-suite) <br>
- [Publisher profile](https://clawhub.ai/user/golikegod) <br>
- [Quick reference](references/00-quick-reference.md) <br>
- [End-to-end workflow](references/06-end-to-end-workflow.md) <br>
- [WeChat article extractor README](scripts/extractor/README.md) <br>
- [WeChat image generator README](scripts/image-gen/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, generated HTML or image assets, extracted article data, and WeChat draft-publishing configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May interact with local files, WeChat URLs, generated images, and WeChat Official Account API credentials.] <br>

## Skill Version(s): <br>
2.1.4 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
