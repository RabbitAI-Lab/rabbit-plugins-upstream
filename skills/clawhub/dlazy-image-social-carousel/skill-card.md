## Description: <br>
A structured workflow skill dedicated to social-media carousel design using a decide-intent-first, single-confirmation, cover-first flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and content teams use this skill to plan and generate social-media carousel image sets with a confirmed direction, cover-first review, and consistent remaining slides. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and provided media can be sent to dLazy API and file services. <br>
Mitigation: Avoid submitting sensitive material unless approved for the service and review organizational data-handling requirements before use. <br>
Risk: The dLazy API key may be stored in a local CLI configuration file. <br>
Mitigation: Use the DLAZY_API_KEY environment variable for non-persistent use, and rotate or revoke keys when access changes. <br>
Risk: The workflow depends on a third-party CLI and hosted API. <br>
Mitigation: Review the dLazy CLI source or package before installation and use the pinned CLI version identified by the release evidence. <br>


## Reference(s): <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with confirmation tables, phase status, CLI commands, and generated image URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires dLazy CLI authentication; prompts and supplied media may be sent to dLazy API and file services.] <br>

## Skill Version(s): <br>
1.3.6 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
