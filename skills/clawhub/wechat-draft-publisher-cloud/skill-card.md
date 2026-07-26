## Description: <br>
Publishes existing Markdown articles and cover images to the WeChat Official Account draft box through a user-configured WeChat Cloud relay, with dry-run as the default and real publishing gated by an explicit flag. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shinchen6](https://clawhub.ai/user/shinchen6) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and content automation operators use this skill to convert prepared Markdown content into WeChat-compatible HTML, upload referenced images through a trusted relay, and create or delete WeChat Official Account drafts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Draft article content, cover images, and local article images are sent through a configured relay when real publishing is enabled. <br>
Mitigation: Use dry-run first, use only a relay you operate or trust, require HTTPS, keep the relay key private, and avoid confidential drafts unless relay hosting and logs are secured. <br>
Risk: Real publishing and draft deletion create external side effects in the WeChat Official Account draft box. <br>
Mitigation: Keep the default dry-run behavior for validation and require the explicit --real flag before publishing or deleting drafts. <br>
Risk: Referenced local image paths are uploaded during real publishing. <br>
Mitigation: Review article image references before running with --real. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shinchen6/skills/wechat-draft-publisher-cloud) <br>
- [Skill homepage](https://github.com/shinchen6/wechat-draft-publisher-skill) <br>
- [WeChat draft relay project](https://github.com/shinchen6/wechat-draft-relay) <br>
- [README](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; runtime writes JSON result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default dry-run; --real is required for network publishing or draft deletion.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
