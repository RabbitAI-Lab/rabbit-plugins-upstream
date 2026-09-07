## Description:

Publish an HTML file, project directory, or ZIP package to 页舟 and update an existing project while preserving its share URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gebangfeng](https://clawhub.ai/user/gebangfeng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to publish or update HTML files, web project directories, or ZIP packages through 页舟 while preserving the public share URL for existing projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shell or CI environment that controls YEZHOU_BASE_URL could redirect credentials and project contents to a non-Yezhou server.

Mitigation: Review the shell and CI environment before use, especially YEZHOU_BASE_URL and YEZHOU_CONFIG_DIR, and only run the skill from projects intended for publication.

Risk: Publishing from the wrong project directory can expose unintended non-hidden files.

Mitigation: Run the skill only from the intended project root and confirm the project contents before deployment.

Risk: The generated .yezhou.json file can expose internal project identifiers if committed or published.

Mitigation: Treat .yezhou.json as project metadata and add it to .gitignore.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gebangfeng/skills/yezhou-deploy)
- [Server-resolved GitHub source](https://github.com/gebangfeng/yezhou-deploy)
- [Official source](https://cnb.cool/gebangfeng/yezhou-deploy)
- [页舟 deployment endpoint](https://yz.gbfeng.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and deployment status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a published or updated 页舟 URL and guidance for browser authorization or project metadata handling.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
