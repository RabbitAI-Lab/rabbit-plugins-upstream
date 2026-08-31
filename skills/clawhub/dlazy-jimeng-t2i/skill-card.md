## Description:

文生图 即梦 Jimeng T2I helps agents generate high-quality images from text prompts using the dLazy Jimeng text-to-image CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit text prompts, optional reference images, and size settings to Jimeng through dLazy and receive generated image results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends prompt text and explicitly supplied media files to an external paid SaaS API.

Mitigation: Avoid submitting private prompts or local files unless external processing and upload to dLazy are intended.

Risk: Authentication setup can store a dLazy API key in the local CLI configuration.

Mitigation: Use the documented device login or API-key setup only on trusted systems, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global CLI installation persists the dLazy binary on the system.

Mitigation: Use the documented npx invocation when a non-persistent install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image results are returned as JSON containing hosted image URLs, and may be downloaded to a user-specified local path.]

## Skill Version(s):

1.3.10 (source: evidence.release.version; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
