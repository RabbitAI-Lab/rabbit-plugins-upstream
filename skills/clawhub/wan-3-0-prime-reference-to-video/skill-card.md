## Description:

Wan 3.0 Prime Reference to Video helps agents generate RunComfy video clips from prompts plus reference images, videos, or audio while preserving subject, product, or location consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[permew](https://clawhub.ai/user/permew)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent operators use this skill to prepare RunComfy CLI calls for reference-guided Wan 3.0 Prime video generation, including media inputs, resolution, duration, aspect ratio, and cost-aware routing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunComfy generation is billed, and 1080p outputs or reference-video inputs can increase cost.

Mitigation: Review prompts and estimated costs before running; use short 480p drafts before final high-resolution generation.

Risk: Reference media may include content the user is not authorized to process.

Mitigation: Use only reference image, video, and audio URLs the user supplied or explicitly approved.

Risk: The skill depends on RunComfy CLI credentials and outbound network access.

Mitigation: Install the CLI only when RunComfy access is intended, keep tokens in the supported RunComfy configuration or RUNCOMFY_TOKEN environment variable, and avoid exposing tokens in prompts or command output.

Risk: Generated media downloads can create local files and consume disk space.

Mitigation: Choose an explicit output directory and review generated files after each run.

## Reference(s):

- [RunComfy Wan 3.0 Prime Reference to Video](https://www.runcomfy.com/models/wan-ai/wan-3.0-prime/reference-to-video?utm_source=clawhub&utm_medium=skill&utm_campaign=wan-3-0-prime-reference-to-video&utm_content=wan-ai-wan-3.0-prime-reference-to-video)
- [RunComfy CLI introduction](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=wan-3-0-prime-reference-to-video&utm_content=cli-docs-introduction)
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=wan-3-0-prime-reference-to-video&utm_content=cli-docs-troubleshooting)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides RunComfy CLI invocation and local configuration; generated video files are produced by the external RunComfy service.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
