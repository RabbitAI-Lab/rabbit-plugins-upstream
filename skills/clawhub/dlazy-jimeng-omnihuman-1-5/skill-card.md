## Description:

Helps generate digital-human broadcast videos from a portrait image and audio or text using Jimeng OmniHuman 1.5 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request digital-human presenter videos from a portrait and audio or a text prompt through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy, and generated outputs are hosted there.

Mitigation: Only submit media with permission to use the hosted service; check privacy requirements before uploading.

Risk: Authentication can save an API key in the user's local configuration.

Mitigation: Protect the key, use per-invocation credentials when preferred, and rotate or revoke it if exposed.

Risk: Using the third-party CLI requires running an npm package.

Mitigation: Review the package and source before authenticating; use the documented npx option to avoid a global installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return hosted media URLs or an asynchronous task ID; a save option downloads the result locally.]

## Skill Version(s):

1.3.29 (source: server-resolved ClawHub release; artifact frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
