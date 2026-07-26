## Description: <br>
Design To Code helps agents convert Figma links, UI screenshots, TRAE design outputs, sketches, or written design specs into runnable local application code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jainwong](https://clawhub.ai/user/jainwong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and product builders use this skill to turn design inputs into responsive web or full-stack application projects with scaffolded code, assets, configuration, and run instructions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated full-stack code can include authentication, payment, upload, logging, or webhook paths that need project-specific security review. <br>
Mitigation: Review secrets handling, access control, payment and webhook verification, upload restrictions, and logging before using generated code in a real project. <br>
Risk: The skill may suggest installing dependencies or running scaffold commands for a generated application. <br>
Mitigation: Run generated commands in a development environment, inspect dependencies and configuration changes, and test the app before deployment. <br>
Risk: Design inputs such as Figma links, screenshots, or AI-provider prompts may contain proprietary information. <br>
Mitigation: Confirm access permissions and data-sharing rules before providing private designs or connecting external provider accounts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jainwong/skills/design-to-code) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, source files, configuration files, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include frontend or full-stack scaffolds, README instructions, .env.example templates, database schemas, API routes, and responsive UI validation notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
