## Description:

Detects whether image, video, or audio media is AI-generated, including visual deepfakes and likely generator model, with confidence scores for thresholding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content review teams use this skill to ask an agent to run dLazy detection on a single image, video, or audio file and interpret confidence scores for AI-generation, deepfake, and generator attribution checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local media can be uploaded to dLazy-hosted services for analysis.

Mitigation: Confirm each file is appropriate to share before analysis and avoid private, biometric, client, or regulated media unless that use is permitted.

Risk: The skill depends on an externally installed npm CLI and locally stored dLazy API key.

Mitigation: Review the @dlazy/cli package or source first, prefer npx or a pinned installation over a broad global install, and protect ~/.dlazy/config.json or use DLAZY_API_KEY per invocation.

Risk: AI-media detection scores may be incomplete, rate limited, or unsuitable as the sole basis for high-impact decisions.

Mitigation: Use confidence scores as decision support, verify important conclusions manually, and remember that text detection is not supported.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Analysis, JSON, Text]

**Output Format:** [JSON results with a brief human-readable text summary and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and exactly one media input flag; local files may be uploaded to dLazy media storage.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
