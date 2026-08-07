## Description: <br>
Creates additional macOS WeChat application copies so an agent can guide a user through running multiple WeChat instances with separate logins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhaobod1](https://clawhub.ai/user/zhaobod1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and macOS users use this skill when they need agent guidance for creating WeChat2.app, WeChat3.app, and similar local copies that can be opened alongside the original WeChat app. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify and ad-hoc-sign WeChat app copies under /Applications. <br>
Mitigation: Review the script before running it and use it only when the user accepts Gatekeeper, update, and support implications for modified app copies. <br>
Risk: Existing WeChat2.app, WeChat3.app, or similar copies may be deleted, including root-owned copies after an administrator prompt. <br>
Mitigation: Back up or manually inspect existing copies before execution and confirm any administrator password prompt is expected. <br>
Risk: The created copies share the original WeChat data directory, so chat history is not isolated between app copies. <br>
Mitigation: Tell users that the copies are for simultaneous login convenience, not data separation, unless they separately configure isolated containers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhaobod1/skills/huo15-multi-wechat) <br>
- [README](artifact/README.md) <br>
- [Changelog](artifact/docs/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides macOS-specific steps for copying, modifying, ad-hoc signing, registering, and opening WeChat app copies.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter, changelog, and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
