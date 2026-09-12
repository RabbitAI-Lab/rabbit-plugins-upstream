## Description:

Transforms an OpenClaw agent into a personal brand authority engine that defines positioning, manages multi-platform presence, and supports authority building through strategic content, social proof, and networking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[georges91560](https://clawhub.ai/user/georges91560)

### License/Terms of Use:

MIT-0

## Use Case:

External entrepreneurs and operators use this skill to establish a personal brand around business, trading, and AI automation. It helps plan identity, platform presence, content cadence, social proof, and networking workflows across Twitter/X, LinkedIn, Instagram, YouTube, TikTok, and podcast channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use existing Telegram and social posting credentials for external notifications or automation when those credentials are present.

Mitigation: Review or disable automation before connecting social credentials, provide only the credentials needed for the intended workflow, and rotate or revoke credentials if behavior is unexpected.

Risk: The skill stores brand strategy, contacts, social proof, audit data, and learning/error logs in the workspace.

Mitigation: Run it only in workspaces approved for that information, review generated files before sharing them, and restrict read/write paths where the agent environment supports path controls.

Risk: Server security evidence notes that some sensitive write paths are under-declared.

Mitigation: Apply tighter path and network controls before deployment where supported, and review filesystem changes during initial runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/georges91560/skills/personal-brand-builder)
- [README](artifact/README.md)
- [Positioning Guide](artifact/positioning.md)
- [Brand Voice Guide](artifact/voice_guide.md)
- [Telegram Bot API](https://api.telegram.org)
- [Twitter/X API](https://api.twitter.com)
- [LinkedIn API](https://api.linkedin.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON configuration, CLI status text, and workspace files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write brand identity, platform configuration, content queues, network contacts, proof records, audit logs, and learning/error logs under the configured workspace paths.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
