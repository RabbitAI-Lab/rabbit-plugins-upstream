## Description: <br>
Generate realistic digital human broadcast videos from portrait images and audio/text using Jimeng OmniHuman 1.5. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent users use this skill to generate digital human broadcast videos through the dLazy hosted Jimeng OmniHuman 1.5 API from supplied portrait images and audio or text prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The pinned CLI may upload selected local media, including during dry-run behavior identified by the security evidence. <br>
Mitigation: Avoid dry-run with sensitive local images or audio unless the behavior is fixed or confirmed acceptable. <br>
Risk: Saved API keys may not have the permission hardening claimed by the skill documentation. <br>
Mitigation: Prefer DLAZY_API_KEY per invocation or manually restrict permissions on ~/.dlazy/config.json when saving a key. <br>
Risk: Persistent global CLI installation increases exposure to package and update risks. <br>
Mitigation: Prefer npx for one-off use when a persistent global CLI is not required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5) <br>
- [dLazy homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with bash examples and JSON CLI result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI responses may include generated media URLs or an async task identifier for later polling.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
