## Description:

文生图 Seedream 5.0 Pro generates professional-quality images through the dLazy Seedream 5.0 Pro CLI, with emphasis on fine detail, typography, and complex composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, marketers, and developers use this skill to generate commercial-quality images and brand assets through the dLazy Seedream 5.0 Pro CLI, optionally using reference images and saved output files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local media files are sent to dLazy API and media-storage endpoints for generation.

Mitigation: Avoid submitting unrelated private content, review file paths before invocation, and use the skill only with data appropriate for a cloud generation service.

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration or supplied through the environment.

Mitigation: Restrict access to the local configuration, avoid exposing environment secrets, and rotate or revoke the key if the config or runtime environment may have been exposed.

Risk: Installing the dLazy CLI globally can persist executable code in the user's environment.

Mitigation: Review the dLazy CLI package or source before installation and prefer npx or another isolated execution method when practical.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs or an asynchronous generateId; the --save option can download generated assets to a local path.]

## Skill Version(s):

1.2.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
