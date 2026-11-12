## Description:

Monitor blogs and RSS/Atom feeds for updates using the blogwatcher CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent help install and run blogwatcher for monitoring blogs and RSS/Atom feeds, scanning for updates, listing articles, and marking items read.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Go install path uses @latest, so the installed third-party CLI can change between installs.

Mitigation: Pin the Go module to a reviewed version or inspect the upstream repository before installation.

Risk: The installed CLI runs with the user's normal account permissions.

Mitigation: Review the CLI behavior and run it in an appropriate user environment before relying on its output.

## Reference(s):

- [Blogwatcher skill page](https://clawhub.ai/seanford/skills/blogwatcher)
- [Blogwatcher homepage](https://github.com/Hyaxia/blogwatcher)
- [ClawHub publisher profile](https://clawhub.ai/user/seanford)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces CLI usage guidance for blogwatcher; no API credentials were detected in the evidence.]

## Skill Version(s):

1.0.0 (source: release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
