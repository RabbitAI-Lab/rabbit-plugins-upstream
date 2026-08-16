## Description:

Generates speech, music, sound effects, and cloned-voice audio by selecting an appropriate dLazy CLI audio model for the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to route audio-generation requests to dLazy CLI models for text-to-speech, music, sound effects, dialogue, and voice-cloning workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: dLazy generation can use paid credits.

Mitigation: Confirm account balance and expected cost before running generation commands.

Risk: Prompts and selected media files are sent to dLazy hosted services.

Mitigation: Avoid submitting confidential, regulated, or unapproved media unless the user's policy permits use of the dLazy service.

Risk: API keys may be persisted in local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable or npx invocation when users do not want a global install or stored key.

Risk: Voice-cloning commands can upload voice samples and generate cloned voices.

Mitigation: Use only voice samples where the user has rights and consent for cloning and downstream use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON CLI output references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media outputs are returned by the dLazy CLI as hosted URLs on files.dlazy.com.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter says 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
