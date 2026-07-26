## Description: <br>
Dlazy Webtoon Adapter helps agents adapt web novel material into Chinese-language webtoon plot breakdowns, episode tags, and per-episode scripts, with optional dLazy CLI-backed image generation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agents use this skill to turn web novel source text into structured webtoon adaptation outputs in Chinese, including plot breakdowns, episode tagging, revision handling, and script drafts. When image generation is requested, it guides the agent through single-step dLazy CLI commands after user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The dLazy CLI stores an API key in local configuration or accepts it through an environment variable. <br>
Mitigation: Use a dedicated dLazy organization key, keep local configuration access-limited, and rotate or revoke the key from the dLazy dashboard when access changes. <br>
Risk: Prompts and referenced local media may be sent to dLazy API and file services during generation. <br>
Mitigation: Avoid sending sensitive source material or private media unless the user has approved that disclosure and accepts dLazy processing. <br>
Risk: The skill asks agents to install or run @dlazy/cli@1.2.3 through npm or npx. <br>
Mitigation: Review the npm package and CLI source before use, and prefer npx for one-off runs when a persistent global install is unnecessary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown and structured Chinese prose with optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are conversation-bound; generation commands require user confirmation and use @dlazy/cli@1.2.3.] <br>

## Skill Version(s): <br>
1.3.5 (source: evidence release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
