## Description: <br>
Installs the yxer CLI, syncs the formal yixiaoer skill, initializes API-key configuration, and runs environment checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yixiaoer888](https://clawhub.ai/user/yixiaoer888) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to bootstrap the yxer command-line workflow before switching to the formal yixiaoer skill for publishing, account, upload, or analytics tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs an external CLI package globally, which can persist configuration and affect the host environment. <br>
Mitigation: Install only in trusted environments and only if the user trusts the @yixiaoermail/cli package. <br>
Risk: The configuration flow may involve entering an API key, which can expose secrets in shared terminals or logs. <br>
Mitigation: Avoid pasting production API keys into shared terminals or logs; use an interactive prompt or secret-store method if yxer supports one. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yixiaoer888/skills/yixiaoer-publish) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with shell command blocks and concise configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js, npm, npx, the external @yixiaoermail/cli package, and a valid API key for configuration.] <br>

## Skill Version(s): <br>
1.6.5 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
