## Description:

Installs and checks free language models for WorkBuddy and Claude Code, with optional model switching, image support, and availability monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and WorkBuddy or Claude Code users can set up free model options, check whether they still work, and monitor availability and tool support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation or model switching can change persistent WorkBuddy and Claude Code settings.

Mitigation: Review changes first using --dry-run where available, and back up model settings and Claude profiles before installing or switching.

Risk: Requests to free third-party model gateways can expose sensitive prompts, code, or images.

Mitigation: Avoid submitting secrets, private code, regulated data, or sensitive images to these services.

Risk: Failed proxy requests may retain prompt content locally.

Mitigation: If prompt retention is unacceptable, disable failed-request dumps with CCPROXY_DUMP_FAILED=0.

## Reference(s):

- [Free LLM Installer on ClawHub](https://clawhub.ai/oracis/skills/free-llm-installer)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce model verification and availability reports.]

## Skill Version(s):

1.1.5 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
