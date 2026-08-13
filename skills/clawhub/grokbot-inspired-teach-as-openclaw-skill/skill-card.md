## Description:

Record a screen demonstration and turn it into a reusable, parameterized OpenClaw SKILL.md.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aldow3n-a11y](https://clawhub.ai/user/aldow3n-a11y)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Developers and OpenClaw users use this skill to record a local workflow demonstration, extract frames and optional narration, and produce a reusable draft SKILL.md with parameterized steps and safety boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill records local screen demonstrations and may capture sensitive workflow details.

Mitigation: Avoid demonstrating secrets or private account details, and install only if you are comfortable recording your screen locally.

Risk: Optional browser-history access can expose visited URLs.

Mitigation: Decline browser-history access unless it is needed.

Risk: Generated SKILL.md files are persistent draft instructions that may omit decision rules or failure handling.

Mitigation: Review the generated draft skill before relying on it, deploying it, or scheduling it.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/aldow3n-a11y/grokbot-inspired-teach-as-openclaw-skill)
- [ClawHub release page](https://clawhub.ai/aldow3n-a11y/skills/grokbot-inspired-teach-as-openclaw-skill)
- [AgentSkills specification](https://agentskills.io)
- [OpenClaw skill schema reference](references/skill-schema.md)
- [Teach principles](references/teach-principles.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown skill file plus concise text report and shell command invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated skills are drafts; recordings and extracted frames are intended to be deleted after use.]

## Skill Version(s):

0.1.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
