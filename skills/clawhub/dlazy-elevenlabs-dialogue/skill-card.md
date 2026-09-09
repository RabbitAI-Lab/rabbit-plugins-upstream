## Description:

ElevenLabs eleven_v3 multi-voice dialogue generates a single conversation audio render from dialogue lines with per-line voice assignment, language, stability, and seed controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate multi-speaker dialogue audio for character scenes, podcasts, and short skits through the dLazy CLI and ElevenLabs eleven_v3.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, selected local media files, and generated outputs are handled by dLazy's hosted service.

Mitigation: Review data before submission, avoid sensitive content unless approved for that service, and account for generated output URLs hosted on files.dlazy.com.

Risk: The dLazy API key can be stored in the local CLI config.

Mitigation: Use OS-user-restricted config storage or per-invocation environment variables as appropriate, and rotate or revoke organization keys when access changes.

Risk: The skill invokes a pinned third-party CLI package.

Mitigation: Prefer the on-demand `npx @dlazy/cli@1.2.3` path in sensitive environments and review the referenced CLI package before global installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, Files, Guidance]

**Output Format:** [Markdown command guidance and JSON result metadata with generated asset URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports a pinned dLazy CLI invocation, optional dry-run, async generation, timeout control, and saving the generated asset to a local path.]

## Skill Version(s):

1.3.14 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
