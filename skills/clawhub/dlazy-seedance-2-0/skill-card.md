## Description:

Seedance 2.0 helps agents generate videos from text prompts, first/last-frame inputs, and multimodal image, video, or audio references through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's Seedance 2.0 video generation workflow from an agent, including text-to-video, first/last-frame, and multimodal reference generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image, video, or audio files are sent to dLazy for generation.

Mitigation: Review inputs before invocation and avoid sending sensitive or restricted media unless the user's dLazy account and data-handling requirements permit it.

Risk: Saved login stores a paid-service API key locally and may consume account credits.

Mitigation: Prefer DLAZY_API_KEY for per-run use on shared machines, or restrict permissions on ~/.dlazy/config.json and rotate or revoke the key from the dLazy dashboard when needed.

Risk: Security evidence says the inspected package does not enforce the restrictive config-file permissions claimed by the skill.

Mitigation: Do not rely on the saved config file for isolation; manually verify local file permissions or use an environment variable instead of persistent login.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI Source Link from Metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON responses containing generated asset URLs; optional downloaded media files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and selected image, video, or audio files are sent to dLazy endpoints; async runs may return a generateId for polling.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
