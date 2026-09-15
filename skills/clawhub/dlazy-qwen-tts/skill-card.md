## Description:

Alibaba Bailian qwen3-tts text-to-speech that lets agents choose curated system voices, including dialects, or design a custom voice from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate text-to-speech audio through the dLazy CLI using Alibaba Bailian qwen3-tts voices. It supports both selecting a preset voice and describing a custom voice in natural language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, API credentials, and explicitly supplied files through the dLazy CLI and hosted service.

Mitigation: Review dLazy service handling requirements before use, avoid sending sensitive inputs unless approved, and use organization-scoped API keys that can be rotated or revoked.

Risk: Installing a global third-party CLI introduces supply-chain exposure.

Mitigation: Prefer pinned on-demand execution with npx or another contained execution method when possible, and review the referenced @dlazy/cli package/source before installation.

Risk: The artifact output-format example describes image results even though this is a text-to-speech skill.

Mitigation: Treat output-format documentation cautiously until corrected, and verify returned MIME types and downloaded files before downstream use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result metadata for generated audio assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy API authentication; generated asset URLs are hosted by the dLazy service.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
