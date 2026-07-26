## Description: <br>
Image replicate tool that analyzes a source image's visuals, composition, colors, lighting, and style, builds a replicate prompt, and uses Seedream 4.5 to generate a new image in the same style. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to invoke the dLazy CLI for image replication workflows, including sending reference images to a hosted generation service and receiving generated image output URLs or async task identifiers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a third-party dLazy CLI and hosted cloud service with a required API key. <br>
Mitigation: Confirm the user is comfortable using the third-party service, prefer per-invocation DLAZY_API_KEY when local key persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed. <br>
Risk: User-supplied media may be uploaded to dLazy storage and generated outputs are hosted by dLazy. <br>
Mitigation: Avoid submitting sensitive or restricted media unless the user has approved that cloud upload and hosted output handling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include hosted image URLs or an async generateId for polling.] <br>

## Skill Version(s): <br>
1.3.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
