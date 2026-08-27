## Description:

Alibaba Bailian qwen3-tts text-to-speech for generating speech with curated system voices, dialect options, or a custom voice described in natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run dLazy's Qwen TTS command for text-to-speech generation, selecting a system voice or describing a custom voice and language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores or uses a dLazy API key for authenticated cloud requests.

Mitigation: Treat the key as a credential, prefer per-invocation environment use when appropriate, and rotate or revoke it from the dLazy dashboard if needed.

Risk: Prompts and generation parameters are sent to the dLazy hosted API.

Mitigation: Avoid submitting sensitive or regulated content unless the user has approved cloud processing under the applicable service terms.

Risk: Local file paths passed to media fields may be uploaded to dLazy media storage.

Mitigation: Pass only files intended for upload and review paths before invoking commands that include local assets.

Risk: A persistent global CLI install increases the local software footprint.

Mitigation: Use the pinned npx invocation when a temporary, non-global CLI execution is preferred.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response with generated asset URLs or async task metadata; optional local saved asset when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports dry-run, asynchronous task return, timeout control, and optional local saving.]

## Skill Version(s):

1.3.9 (source: release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
