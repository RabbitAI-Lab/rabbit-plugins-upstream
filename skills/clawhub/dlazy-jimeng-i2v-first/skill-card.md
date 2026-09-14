## Description:

Generate dynamic videos based on a single first frame image and prompts using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy Jimeng image-to-video service from an agent workflow, providing a first-frame image and prompt to generate a hosted video result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI and dLazy cloud service, which can send prompts, parameters, and selected media files to api.dlazy.com and files.dlazy.com.

Mitigation: Install only after accepting that data flow, prefer npx or another isolated run method, and pass only the specific media needed for generation.

Risk: The skill requires a dLazy API key stored locally or supplied through the DLAZY_API_KEY environment variable.

Mitigation: Protect the API key, use per-invocation credentials where practical, and rotate or revoke the key if exposure is suspected.

Risk: The evidence notes flag and output-format inconsistencies in the documentation.

Mitigation: Check dlazy jimeng-i2v-first -h before use and confirm the required flags before submitting generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return a hosted media URL, save a generated asset locally, or return an asynchronous generation ID for polling.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
