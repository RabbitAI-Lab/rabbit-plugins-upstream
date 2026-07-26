## Description: <br>
Video replicate tool: extracts the first frame and audio from the source video, runs video understanding for a prompt, and returns a Seedance 2.0 replicate bundle (first frame + audio + video). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to invoke the dLazy video-replicate workflow from an agent, providing a source video and parameters to generate a Seedance 2.0 replicate bundle. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The dLazy CLI stores an API key locally, and that key may control paid credits or sensitive account access. <br>
Mitigation: Prefer per-invocation DLAZY_API_KEY where practical, rotate or revoke keys when needed, and verify that the local CLI config file is restricted to the current OS user after login. <br>
Risk: Local media paths supplied to the skill are uploaded to dLazy-hosted services for processing. <br>
Mitigation: Only pass media files intended for dLazy processing and review files for sensitive content before invocation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate) <br>
- [dLazy CLI Source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy Homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, API calls, JSON] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return generated media URLs or an asynchronous task identifier depending on CLI options.] <br>

## Skill Version(s): <br>
1.3.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
