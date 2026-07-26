## Description: <br>
Convert static character images into vivid action videos with Jimeng Dream Actor. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to invoke the dLazy CLI for Jimeng Dream Actor image-to-video generation from prompts and image or video references. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected media files are sent to the dLazy hosted API and media storage for generation. <br>
Mitigation: Use only prompts and media approved for third-party processing, review dLazy service terms, and avoid sending sensitive or restricted content. <br>
Risk: The skill requires a dLazy API key and may consume billable credits. <br>
Mitigation: Prefer scoped organization keys, rotate or revoke keys from the dLazy dashboard when no longer needed, and use dry-run or balance checks before costly runs. <br>
Risk: A globally installed CLI persists on the local system. <br>
Mitigation: Use the pinned npx invocation for occasional use and review the CLI source before persistent installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [JSON response with generated media URLs or async task status, plus concise guidance for authentication, balance, and execution errors.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May upload selected prompts and media files to dLazy endpoints and may use billable API credits.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
