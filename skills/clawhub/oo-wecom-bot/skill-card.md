## Description:

WeCom Bot helps an agent read, create, update, and delete WeCom Bot data through OOMOL's oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and employees use this skill to operate WeCom Bot through a connected OOMOL account, including messaging, schedules, meetings, todos, documents, online sheets, smart sheets, and smart pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes installer commands for the oo CLI.

Mitigation: Install only after manually reviewing or verifying the installer source, and avoid running setup commands unless the CLI is missing.

Risk: Some WeCom changes may not be clearly tagged before execution.

Mitigation: Require explicit user confirmation before changing todos, sheets, messages, meetings, documents, or dynamically discovered tools.

Risk: The connected WeCom account may have broad permissions.

Mitigation: Deploy only with an OOMOL-connected account whose permissions match the intended WeCom workspace tasks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-wecom-bot)
- [WeCom Bot Homepage](https://work.weixin.qq.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses and WeCom document or smart-page content as Markdown.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
