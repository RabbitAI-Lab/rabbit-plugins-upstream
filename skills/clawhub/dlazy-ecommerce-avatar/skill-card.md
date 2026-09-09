## Description:

Ecommerce livestream avatar / AI spokesperson for product selling videos, with production base-portrait recipes and a script-to-TTS-to-avatar-to-B-roll workflow for product selling videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agents use this skill to plan and run a repeatable digital-human product video workflow for TikTok Shop, Douyin, Amazon, Shopee, and brand-store selling. It guides base portrait selection, script segmentation, TTS, avatar driving, B-roll generation, and assembly decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a third-party CLI and may send product images, generated avatar assets, audio, and prompts to dLazy services.

Mitigation: Install in a non-privileged environment, avoid sudo, limit the dLazy API key, and review what media and prompts are submitted before execution.

Risk: Paid generation calls can consume credits when parameters, prompt lengths, or media duration are wrong.

Mitigation: Use the documented dry-run option, segment scripts and audio within model limits, and validate model-specific size and duration flags before submitting paid requests.

Risk: Generated avatar sales content can create misleading product claims, false authority cues, or platform disclosure issues.

Mitigation: Review claims and visuals before publication, avoid prohibited absolute or medical-effect claims unless properly substantiated, verify any credentials or labels, and apply required AI-generated content disclosures.

Risk: The main avatar-driving path depends on a static-image-plus-audio model and produces media specs that may differ from B-roll clips.

Mitigation: Validate base portraits for driveability, keep fallback lipsync paths available when the primary model is unavailable, and re-encode assembled clips to a common resolution, frame rate, sample rate, and channel layout.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-avatar)
- [dLazy homepage](https://dlazy.com)
- [Skill overview](SKILL.md)
- [Full production pipeline](pipeline.md)
- [Base portrait recipes](recipes.md)
- [Troubleshooting and compliance guidance](troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include prompt constraints, model-specific limits, dry-run checks, cost notes, and media assembly steps.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
