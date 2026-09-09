## Description:

Turns a script, screenplay, or shot list into a storyboarded, shot-by-shot video workflow that breaks down scenes, generates shots, assembles them, and validates the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative developers use this skill to turn scripts or scene breakdowns into multi-shot animated video projects with storyboard, shot generation, assembly, and validation support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any files attached with --files are sent to the dLazy hosted API and media storage.

Mitigation: Use the skill only with content approved for dLazy processing, review attachments before sending them, and avoid uploading sensitive files unless that use is authorized.

Risk: Authentication can persist an API key in the local dLazy CLI configuration.

Mitigation: Use per-run DLAZY_API_KEY or npx when less local persistence is preferred, and rotate or revoke saved keys from the dLazy dashboard when needed.

Risk: The skill depends on the third-party @dlazy/cli npm package and dLazy hosted service availability.

Mitigation: Install the pinned @dlazy/cli@1.2.3 package declared by the release metadata and review the package or source link before execution in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or terminal text with CLI command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project ids, uploaded user files, and generated video project results returned by the dLazy service.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
