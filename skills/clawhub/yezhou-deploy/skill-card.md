## Description:

Publish an HTML file, project directory, or ZIP package to 页舟 and update an existing project while preserving its share URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gebangfeng](https://clawhub.ai/user/gebangfeng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to publish or republish web pages, project directories, and ZIP packages to 页舟 while preserving the public share URL for existing works.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A tampered launch environment can set YEZHOU_BASE_URL so uploads and the saved 页舟 credential are sent to an untrusted endpoint.

Mitigation: Run the skill only when YEZHOU_BASE_URL is unset or explicitly set to a trusted endpoint, and review wrappers, CI jobs, and shell profiles before use.

Risk: The local .yezhou.json manifest can expose internal project identifiers if published with the project.

Mitigation: Treat .yezhou.json as project metadata and decide explicitly whether it should be tracked or ignored.

Risk: Updating the wrong remote work can replace an existing public project.

Mitigation: Use --site only when the user has identified the exact existing work by site ID or public URL.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gebangfeng/skills/yezhou-deploy)
- [Official Source](https://cnb.cool/gebangfeng/yezhou-deploy)
- [页舟 Service](https://yz.gbfeng.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise deployment guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the published or updated public URL printed by the bundled script.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
