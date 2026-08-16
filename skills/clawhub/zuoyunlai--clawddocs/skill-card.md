## Description:

Clawdbot documentation expert with decision tree navigation, search scripts, doc fetching, version tracking, and configuration snippets for Clawdbot features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to find Clawdbot documentation, troubleshoot setup and provider issues, retrieve relevant docs, and adapt common configuration snippets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide agents to consult external Clawdbot documentation that can change over time.

Mitigation: Cite the source documentation URL and verify current docs before applying operational guidance.

Risk: Configuration examples include provider token placeholders.

Mitigation: Use environment variables or secret stores for real tokens and avoid placing secrets in prompts, logs, or shared config examples.

Risk: Bundled shell helpers support documentation search, fetching, cache checks, and change tracking.

Mitigation: Review commands before execution and run them in an appropriate workspace with normal least-privilege controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/clawddocs)
- [Clawdbot documentation](https://docs.clawd.bot/)
- [Common configuration snippets](snippets/common-configs.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cite Clawdbot documentation URLs and summarize search or fetch results from bundled helper scripts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
