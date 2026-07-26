## Description: <br>
Paste a URL and use the dLazy hosted URL-to-video workflow to create a promo, ad, or product demo video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn a webpage or landing-page URL into a video by invoking the dLazy website-to-video CLI workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, URLs, and explicitly attached files are sent to dLazy's hosted service, and login stores a local dLazy API key. <br>
Mitigation: Review the data being submitted before use, prefer npx when avoiding a persistent global install, and rotate or revoke the API key from the dLazy dashboard when needed. <br>


## Reference(s): <br>
- [Dlazy Url To Video on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video) <br>
- [dLazy CLI GitHub repository](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Terminal text with shell commands and streamed agent responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference project ids for continuing multi-turn video generation sessions.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
