## Description: <br>
Tongyi Wanxiang 2.7 video model for text-to-video, first/last-frame-to-video, and reference-to-video generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to invoke the dLazy hosted Wan2.7 video model from prompts and optional reference images, video, audio, or first and last frames. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local media may be uploaded to dLazy storage, and the security summary warns that uploads can occur even when using dry-run. <br>
Mitigation: Avoid passing private local files unless upload is acceptable, and use `npx @dlazy/cli@1.2.3` for ad hoc runs when possible. <br>
Risk: The skill uses a dLazy API key, and the security guidance warns that local CLI key storage may not enforce the restrictive permissions claimed by the artifact. <br>
Mitigation: Prefer `DLAZY_API_KEY` per invocation in sensitive environments, or manually restrict permissions on `~/.dlazy/config.json` and rotate keys when needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7) <br>
- [Publisher Profile](https://clawhub.ai/user/dlazyai) <br>
- [dLazy CLI Source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy Homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The wrapped CLI returns hosted media URLs for completed jobs or async task identifiers when no-wait mode is used.] <br>

## Skill Version(s): <br>
1.3.4 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
