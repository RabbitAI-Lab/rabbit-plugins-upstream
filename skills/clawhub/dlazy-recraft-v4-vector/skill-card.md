## Description:

Text-to-vector model that outputs SVG results for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative tool users invoke this skill to generate vector-style image assets through the dLazy CLI using text prompts and optional aspect-ratio controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any files explicitly passed to the CLI may be sent to dLazy cloud endpoints.

Mitigation: Avoid submitting private or sensitive files unless the user is comfortable uploading them to the dLazy service.

Risk: Authentication stores a dLazy API key in local CLI configuration when using dlazy login or dlazy auth set.

Mitigation: Use normal key hygiene, rotate or revoke keys from the dLazy dashboard when needed, and prefer per-invocation environment variables where local persistence is undesirable.

Risk: A global CLI installation persists the third-party tool on the system.

Mitigation: Use npx @dlazy/cli@1.2.3 for on-demand execution when a persistent global install is not preferred.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted generated asset URLs; the --save option can download the generated output to a local path.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
