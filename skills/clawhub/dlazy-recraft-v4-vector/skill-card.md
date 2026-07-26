## Description: <br>
Text-to-vector model that outputs SVG results for logos, icons, and scalable design assets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, and external agents use this skill to invoke the dLazy Recraft V4 Vector model for generating vector-style design assets from text prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a third-party dLazy CLI and sends prompts, parameters, and explicitly referenced files to dLazy hosted services. <br>
Mitigation: Review the dLazy CLI and service terms before use, and avoid sending sensitive prompts or files unless approved for that service. <br>
Risk: Authentication stores a dLazy API key in local CLI configuration unless a per-invocation environment variable is used. <br>
Mitigation: Use organization-scoped keys, rotate or revoke keys when needed, and prefer npx @dlazy/cli@1.2.3 when avoiding a persistent global install. <br>


## Reference(s): <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files] <br>
**Output Format:** [Shell command output as JSON containing generated media result URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return asynchronous task IDs when --no-wait is used; generated URLs are hosted on files.dlazy.com.] <br>

## Skill Version(s): <br>
1.3.5 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
