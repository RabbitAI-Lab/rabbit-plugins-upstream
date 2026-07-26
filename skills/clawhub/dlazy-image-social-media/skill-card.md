## Description: <br>
A structured skill for multi-platform social-media content creation across Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and related channels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and agent users use this skill to plan and produce platform-specific social-media image concepts, in-image text, captions, and dLazy CLI generation commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, parameters, and selected media files may be sent to dLazy cloud endpoints during generation. <br>
Mitigation: Use the skill only with content approved for dLazy's cloud services and avoid submitting sensitive media unless that transfer is acceptable. <br>
Risk: The dLazy CLI requires an API key that can be stored in the local user configuration. <br>
Mitigation: Prefer the DLAZY_API_KEY environment variable for per-session credentials, and rotate or revoke keys from the dLazy dashboard when needed. <br>
Risk: Global installation of the pinned npm CLI changes the local agent environment. <br>
Mitigation: Review the pinned @dlazy/cli package source before installation or use the documented npx invocation to avoid a long-lived global install. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media) <br>
- [dLazy CLI Source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy Homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with structured planning, platform checks, caption copy, inline shell commands, and generated image URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before each image generation command and uses a pinned dLazy CLI package.] <br>

## Skill Version(s): <br>
1.3.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
