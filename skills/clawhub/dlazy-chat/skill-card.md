## Description:

Chat with dLazy's project-scoped sandbox agent to run skills across multiple turns and continue existing projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy users chat with a hosted sandbox agent to run skills in a new project or continue multi-turn work in an existing one.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and project context are sent to dLazy services; files attached with --files are uploaded.

Mitigation: Use only when you intend to share that content with dLazy; review prompts and attachments before sending.

Risk: Login stores an API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY per run if you do not want a stored key, and protect any locally saved credentials.

Risk: Broad chat requests may activate the hosted agent unintentionally.

Mitigation: Use explicit dLazy-related prompts when invoking this skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI source listed in skill metadata (not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming text responses in the terminal; content depends on the selected skill and conversation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped, multi-turn responses]

## Skill Version(s):

1.2.33 (source: ClawHub release metadata; artifact frontmatter says 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
