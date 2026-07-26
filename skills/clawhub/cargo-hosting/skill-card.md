## Description: <br>
Build, deploy, and manage Cargo Hosting apps and workers with the Cargo CLI - Vite SPAs served on *.cargo.app and serverless edge HTTP handlers, plus the deployments that ship and promote them. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cargo-ai](https://clawhub.ai/user/cargo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to scaffold, create, deploy, promote, inspect, and remove Cargo-hosted Vite apps, edge workers, and their deployments from an agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Promote or remove commands can change the live deployment or delete Cargo-hosted resources. <br>
Mitigation: Before running these commands, verify the Cargo account, workspace, resource UUID, and currently promoted deployment. <br>
Risk: Generated .env.local output can contain workspace and Cargo app configuration. <br>
Mitigation: Write environment output only to the intended local project and keep generated .env.local files out of source control. <br>
Risk: Deployment creation uploads the selected local source directory to Cargo's build service. <br>
Mitigation: Review the source path and ignore list before upload, and pass the package root rather than a built dist directory. <br>
Risk: A deployment build is asynchronous and is not live until a successful deployment is promoted. <br>
Mitigation: Poll the deployment until it reaches a terminal status, promote only a successful deployment, and verify the promoted deployment afterward. <br>


## Reference(s): <br>
- [Cargo Hosting skill page](https://clawhub.ai/cargo-ai/skills/cargo-hosting) <br>
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills) <br>
- [App examples](references/examples/apps.md) <br>
- [Worker examples](references/examples/workers.md) <br>
- [Deployment examples](references/examples/deployments.md) <br>
- [Hosting response shapes](references/response-shapes.md) <br>
- [Hosting troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands, JSON response examples, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide commands that scaffold local projects, upload source for hosted builds, promote deployments, remove resources, or print .env.local configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
