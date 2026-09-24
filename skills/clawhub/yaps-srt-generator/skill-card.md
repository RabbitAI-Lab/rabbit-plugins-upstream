## Description:

Make a timed SRT subtitle file from audio or video with Yaps. New users: install Yaps and sign in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yaps](https://clawhub.ai/user/yaps)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and agents use this skill to generate sidecar SRT subtitle files from selected local audio or video through an installed Yaps desktop engine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can invoke broader local Yaps CLI capabilities than its subtitle-only description suggests.

Mitigation: Install only if comfortable with local Yaps CLI access, use files intentionally selected for the task, and review Yaps-side projects, jobs, downloads, and account prompts before proceeding.

Risk: Account, credential, Keychain, model-download, or permission prompts may appear while using local Yaps workflows.

Mitigation: Avoid approving unexpected credential or Keychain prompts, authorize model downloads only after reviewing reported size, and manage sign-in or access changes inside Yaps.

## Reference(s):

- [Runtime guide](references/runtime.md)
- [Download or open Yaps](https://yaps.ai/download)
- [ClawHub skill page](https://clawhub.ai/yaps/skills/yaps-srt-generator)

## Skill Output:

**Output Type(s):** [Text, Files, Shell commands, Guidance]

**Output Format:** [SRT subtitle file with concise Markdown status and metrics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill expects absolute input and output paths, preserves existing outputs, validates non-empty ordered SRT cues, and reports Yaps engine, duration, and word count.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
