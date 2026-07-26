## Description: <br>
Monitor blogs and RSS/Atom feeds for updates using the blogwatcher CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to install and operate the blogwatcher CLI for tracking blog, RSS, and Atom feed updates from configured sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs the latest version of an external Go CLI, so the executed tool may change over time. <br>
Mitigation: Review the linked repository before installing and pin or audit the CLI version in controlled environments. <br>
Risk: Normal use contacts configured blog or feed URLs and stores local feed/read-state data. <br>
Mitigation: Use only approved feed sources and handle local state according to the user's data-retention requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/seanford/skills/blogwatcher) <br>
- [Blogwatcher GitHub repository](https://github.com/Hyaxia/blogwatcher) <br>
- [Blogwatcher Go install module](https://pkg.go.dev/github.com/Hyaxia/blogwatcher/cmd/blogwatcher) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and example CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the external blogwatcher CLI binary.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
