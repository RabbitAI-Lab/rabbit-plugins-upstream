## Description:

Manage Sonatype Nexus Repository 3 from the command line: list repositories, search components and assets, list components in a repository, upload files to raw hosted repositories, download assets, and delete components.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weiguang1017](https://clawhub.ai/user/weiguang1017)

### License/Terms of Use:

MIT

## Use Case:

Developers and DevOps engineers use this skill to browse and operate Sonatype Nexus Repository Manager 3 repositories, including artifact discovery, raw asset publishing, downloads, and component cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Download commands can send Nexus credentials to a URL outside the intended Nexus host.

Mitigation: Run download commands only when the URL is clearly on the expected Nexus host, and review the URL before execution.

Risk: Deleting a component is irreversible and has no built-in confirmation step.

Mitigation: Require explicit human approval outside the tool and confirm the component ID with search or list output before deletion.

Risk: Overprivileged Nexus credentials increase blast radius if commands are misused.

Mitigation: Use a least-privilege Nexus token and grant read, add, or delete permissions only for the repositories and tasks required.

Risk: The requests dependency should stay current to avoid known dependency vulnerabilities.

Mitigation: Pin requests to a current safe version when installing the skill in a managed environment.

## Reference(s):

- [Source repository](https://github.com/weiguang1017/nexus-repository-skill)
- [ClawHub skill page](https://clawhub.ai/weiguang1017/skills/nexus-repository-skill)
- [Agent instructions](SKILL.md)
- [README](README.md)
- [Detailed Chinese manual](使用手册.md)
- [RestartX support](https://service.restartx.top/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands; CLI commands print JSON to stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3.8+, requests, Nexus connection credentials, and a Sonatype Nexus Repository Manager 3.0+ target.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
