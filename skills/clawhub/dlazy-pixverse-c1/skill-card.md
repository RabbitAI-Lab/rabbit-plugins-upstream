## Description:

PixVerse C1 generates videos from text, image, first/last-frame, and reference-image inputs, with strengths in action, VFX, and high-motion scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate PixVerse C1 videos through the dLazy CLI from prompts and optional image or frame inputs. It helps the agent handle setup, authentication guidance, request options, and result handling for generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy hosted services for video generation.

Mitigation: Use the skill only for explicit PixVerse C1 requests and avoid sending sensitive prompts or media unless the user accepts dLazy processing.

Risk: Generated assets may be hosted by dLazy.

Mitigation: Treat returned asset URLs as third-party hosted outputs and download or share them only according to the user's data-handling requirements.

Risk: Using dlazy login can store an API key in local CLI configuration.

Mitigation: Prefer npx or per-invocation DLAZY_API_KEY when less local credential persistence is desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI results; optional generated media files when saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and selected media files are sent to dLazy hosted endpoints and generated assets may be hosted by dLazy.]

## Skill Version(s):

1.2.20 (source: server release evidence; artifact frontmatter states 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
