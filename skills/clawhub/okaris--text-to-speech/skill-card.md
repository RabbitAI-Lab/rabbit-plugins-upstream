## Description:

Convert text to natural speech with inference.sh CLI models for voiceovers, audiobooks, podcasts, accessibility, video narration, IVR, and voice assistants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okaris](https://clawhub.ai/user/okaris)

### License/Terms of Use:


## Use Case:

Developers and content creators use this skill to generate inference.sh CLI commands and configuration examples for text-to-speech, voice cloning, multi-speaker dialogue, podcast generation, and expressive speech workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes a mutable remote installer command.

Mitigation: Use a manually downloaded, version-pinned CLI binary and verify it against published checksums before installation.

Risk: Related skill installation examples use unpinned npx commands.

Mitigation: Pin versions and review the package source before running installation commands.

Risk: Text submitted for speech generation may be processed by a remote service.

Mitigation: Do not submit secrets, regulated data, or confidential scripts unless that remote transfer is approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/okaris/skills/text-to-speech)
- [inference.sh Running Apps Documentation](https://inference.sh/docs/apps/running)
- [inference.sh Apps Overview](https://inference.sh/docs/apps/overview)
- [inference.sh CLI Checksums](https://dist.inference.sh/cli/checksums.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON input examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include inference.sh app IDs, CLI commands, and sample JSON payloads.]

## Skill Version(s):

0.1.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
