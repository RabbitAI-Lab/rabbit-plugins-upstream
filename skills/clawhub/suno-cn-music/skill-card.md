## Description:

Suno.cn AI music assistant for agents that helps users create songs from prompts or lyrics, generate lyrics, cover or extend reference audio, create instrumental music and BGM, separate vocals or stems, edit audio, convert WAV/MIDI/sheet-music outputs, and query works or credits through web authorization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adcgg](https://clawhub.ai/user/adcgg)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to connect an agent to Suno.cn music generation and audio-processing workflows, including prompt-to-song creation, lyrics generation, reference-audio cover or extension, vocal and stem separation, audio editing, and account or credit checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send credentials and uploaded files to a service endpoint controlled through environment configuration.

Mitigation: Install only from a trusted publisher and avoid setting SUNO_CN_MCP_URL or SUNO_CN_CONFIG_DIR unless using a trusted test setup.

Risk: Some operations consume Suno.cn account credits.

Mitigation: Review account balance and credit-consuming actions before confirming retries or purchases.

Risk: Generated music and transformed audio may have rights, suitability, or quality constraints outside the skill package.

Mitigation: Review outputs and Suno.cn terms before publishing or using generated works commercially.

Risk: The skill stores local authorization state for web-based access.

Mitigation: Use auth logout or Suno.cn authorization management to revoke access when finished.

## Reference(s):

- [Suno.cn homepage](https://www.suno.cn)
- [Suno.cn MCP REST API](references/api.md)
- [ClawHub skill page](https://clawhub.ai/adcgg/skills/suno-cn-music)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON helper responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated audio, MIDI, WAV, PDF, authorization, purchase, task-status, and account links from Suno.cn service responses.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter/helper version: 2.3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
