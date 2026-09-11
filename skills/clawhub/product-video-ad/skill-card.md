## Description:

Creates short product video ads by turning selling points into a storyboard, generating each shot, assembling clips, and adding timed subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and marketing teams use this skill to plan and generate 15-30 second product ad videos for paid social or commerce placements. It is most useful when a user has product selling points, reference images, and a target platform, and needs storyboard text plus generated video assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network fetching and provider endpoint overrides can expose credentials or internal network resources in unsafe configurations.

Mitigation: Use local files or trusted HTTPS image hosts, avoid custom ARK_BASE_URL unless you fully control it, and isolate provider credentials from unrelated projects.

Risk: Untrusted storyboard or brand files can influence prompts, reference image fetching, and generated output locations.

Mitigation: Review storyboard and brand files before execution, use a fresh output directory per run, and run dry-run planning before paid generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Video backend configuration](artifact/references/video-backends.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Code, Files, Guidance]

**Output Format:** [Markdown guidance with inline JSON and bash examples; generated runs can write MP4 clips, SRT subtitles, concat manifests, final video files, and JSON status output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run planning, provider selection, storyboard-driven multi-shot generation, optional brand constraints, ffmpeg assembly, and subtitle fallback behavior.]

## Skill Version(s):

1.0.6 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
