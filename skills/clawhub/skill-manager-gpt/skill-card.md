## Description:

[GPT only] Manage skills on ClawHub from ChatGPT Work/Codex: inspect and adapt public packages, publish GPT-specific skills with accurate metadata, and retrieve skills when requested. Requires GPT browser control; not an OpenClaw-native integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ciklopentan](https://clawhub.ai/user/ciklopentan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill in browser-capable ChatGPT Work or Codex environments to inspect, adapt, publish, and retrieve ClawHub skills while preserving accurate platform and licensing metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended for browser-capable GPT/Codex environments and may not run as an OpenClaw-native integration.

Mitigation: Use it only where browser control and equivalent skill-registry capabilities are available, and label unsupported platform behavior clearly.

Risk: Publishing a skill to ClawHub may expose unintended files or private data.

Mitigation: Review exactly which files will be uploaded, remove secrets and unnecessary local files, and publish only after explicit user confirmation.

Risk: ClawHub releases use MIT-0 licensing, which permits broad reuse and redistribution.

Mitigation: Confirm the licensing impact with the user before checking rights confirmation or submitting a release.

Risk: Implicit invocation and broad product routing may route the skill more widely than intended.

Mitigation: Consider narrowing manifest products or disabling implicit invocation when tighter routing is required.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/ciklopentan/skills/skill-manager-gpt)
- [OpenClaw ClawHub Documentation](https://docs.openclaw.ai/clawhub/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise text with optional code, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compatibility notes, publication checklists, file review findings, and safety guidance.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
