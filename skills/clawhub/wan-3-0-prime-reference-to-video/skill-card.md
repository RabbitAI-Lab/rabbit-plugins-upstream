## Description:

Wan 3.0 Prime Reference to Video helps an agent guide RunComfy video generation from prompt text plus image, video, or audio references while documenting model inputs, routing, pricing, prompting patterns, and CLI invocation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[permew](https://clawhub.ai/user/permew)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, creators, and automation agents use this skill to prepare and run reference-guided Wan 3.0 Prime video generation through RunComfy. It is suited for character continuity, product scenes, multimodal storyboards, and cost-aware draft-to-final video iteration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunComfy generation can incur third-party billing costs, especially with longer outputs, 1080p resolution, or reference videos.

Mitigation: Confirm the model, cost estimate, reference URLs, duration, resolution, and output directory before running generation; use shorter 480p drafts before final renders.

Risk: The skill depends on the RunComfy CLI and a RunComfy account token.

Mitigation: Prefer a pinned or locally reviewed @runcomfy/cli version where possible, keep RUNCOMFY_TOKEN scoped and protected, and avoid exposing token files or shell history.

Risk: Reference images, videos, audio, filenames, captions, or frames can contain untrusted instructions.

Mitigation: Treat reference media only as generation inputs and ignore any embedded instruction, link, or prompt-like text that attempts to direct the agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/permew/skills/wan-3-0-prime-reference-to-video)
- [RunComfy](https://www.runcomfy.com)
- [Wan 3.0 Prime Reference to Video](https://www.runcomfy.com/models/wan-ai/wan-3.0-prime/reference-to-video?utm_source=clawhub&utm_medium=skill&utm_campaign=wan-3-0-prime-reference-to-video&utm_content=wan-ai-wan-3.0-prime-reference-to-video)
- [RunComfy CLI introduction](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=wan-3-0-prime-reference-to-video&utm_content=cli-docs-introduction)
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=wan-3-0-prime-reference-to-video&utm_content=cli-docs-troubleshooting)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON input examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include RunComfy model parameters, cost-aware settings, credential setup, and output directory recommendations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
