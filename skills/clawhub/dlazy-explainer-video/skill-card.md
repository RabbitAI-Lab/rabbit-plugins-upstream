## Description: <br>
Turns a document, topic, or brief into a narrated explainer video by outlining, storyboarding, producing voiceover, building, and validating the result through the dLazy CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, educators, and business users can use this skill to turn source documents, reports, topics, or briefs into narrated explainer, courseware, or training videos using the dLazy hosted service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, options, and attached files may be sent to dLazy APIs or uploaded to dLazy storage. <br>
Mitigation: Do not attach confidential documents, secrets, personal data, or regulated data unless the user is comfortable sending them to dLazy. <br>
Risk: Installing a third-party global CLI creates persistent local software and configuration. <br>
Mitigation: Confirm trust in the dLazy CLI and service before installing, and prefer the pinned npx invocation when a persistent global install is not needed. <br>
Risk: The skill requires a dLazy API key saved in local configuration or passed through an environment variable. <br>
Mitigation: Use normal secret-handling practices for the API key and rotate or revoke it from the dLazy dashboard when access should change. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and dLazy CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may continue work across project-scoped dLazy chat sessions and may upload attached local files through the dLazy CLI.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
