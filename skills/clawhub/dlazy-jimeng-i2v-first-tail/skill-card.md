## Description:

Generate coherent transition videos using Jimeng first-and-tail-frame models from a prompt plus first-frame and last-frame images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to invoke the dLazy CLI for Jimeng first-tail-frame video generation, optionally returning async task IDs or saving generated media locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media paths supplied to the command are sent to dLazy hosted services for generation.

Mitigation: Confirm the user is comfortable sending the requested media to dLazy before execution, and avoid confidential or regulated content unless approved for that service.

Risk: Using dlazy login or dlazy auth set can store a revocable API key in the local dLazy configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for one-off runs when persistent credential storage is not desired, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: A global install persists the dLazy CLI binary on the system.

Mitigation: Use the pinned npx invocation when users prefer not to keep a global CLI installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result objects containing generated media URLs or async task IDs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs from files.dlazy.com or save the generated asset to a local path when requested.]

## Skill Version(s):

1.3.10 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
