## Description: <br>
Dlazy Short Video helps agents run dLazy's short-video template to create finished 15-25 second vertical MP4s for TikTok, YouTube Shorts, Instagram Reels, Douyin, and similar social formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, marketers, and agent users use this skill to start or continue dLazy short-video projects from prompts and optional reference files. It is intended for social short-form video generation, while conversion-focused product ads are directed to a different skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, options, and attached files are sent to dLazy API and media storage services. <br>
Mitigation: Review data sensitivity before use and avoid submitting confidential prompts or media unless that SaaS transfer is approved. <br>
Risk: A dLazy organization API key may be stored in the local CLI configuration. <br>
Mitigation: Use the environment variable option for one-off sessions when appropriate, keep local config permissions restricted, and rotate or revoke keys from the dLazy dashboard when needed. <br>
Risk: Broad auto-routing terms such as reels may trigger short-video generation when the user intent is ambiguous. <br>
Mitigation: Confirm the user wants short-video generation before invoking the skill for broad or ambiguous requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline bash command examples; dLazy project responses may include references to generated vertical MP4 files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a dLazy API key; prompts, options, and attached files are sent to dLazy services when the CLI is invoked.] <br>

## Skill Version(s): <br>
1.2.6 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
