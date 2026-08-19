## Description:

Soul Archive is a local-first digital personality persistence and agentic memory skill that extracts, stores, recalls, and reports persona and workflow patterns as plaintext JSON for use by local AI agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dqsjqian](https://clawhub.ai/user/dqsjqian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use this skill to maintain a local personal profile and long-term agent memory that can be recalled as prompts, summaries, warnings, reports, or configuration for future sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can build and reuse a sensitive plaintext personal profile that local agents can read.

Mitigation: Review config.json before use, disable auto_extract, auto_reflect, and auto_context_inject when manual control is preferred, and avoid storing health, finance, intimate, or other highly sensitive details.

Risk: Persona prompts can enable an AI agent to imitate the user.

Mitigation: Use the skill only for intended personal workflows, review generated prompts and reports, and preserve the documented requirement to disclose AI role-play when directly asked.

Risk: Generated reports or synced archives can expose local personal data beyond the intended machine.

Mitigation: Keep archives out of public repositories, apply the documented gitignore guidance for highly sensitive folders, and open generated reports only in environments where any external script exposure is acceptable.

## Reference(s):

- [Soul Archive on ClawHub](https://clawhub.ai/dqsjqian/skills/soul-archive)
- [Privacy](PRIVACY.md)
- [Multi-device sync and backup](docs/multi-device-sync.md)
- [Extraction prompts](references/extraction_prompts.md)
- [Claude Skills documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/getting-started)
- [Agent Guild](https://github.com/dqsjqian/agent-guild)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML, Shell commands, Configuration, Guidance]

**Output Format:** [CLI text, Markdown, JSON files and summaries, generated HTML reports, and prompt-ready persona context]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores user and agent memory locally as plaintext JSON under the configured soul data directory.]

## Skill Version(s):

3.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
