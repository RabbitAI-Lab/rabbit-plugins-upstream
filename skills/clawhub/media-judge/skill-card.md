## Description:

Measures finished AI-made videos, images, and audio for defects, then produces evidence-backed reports and ranks takes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and agents use the skill to review finished media, investigate measured defects with visual evidence, and compare or rank multiple takes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports undeclared network and environment capabilities and unpinned installation examples; its analysis is partial and does not establish malicious intent.

Mitigation: Explain and bound network and environment permissions, and pin and verify the CLI and skill revision before installation.

Risk: The security guidance flags the overwrite example and benchmark limitation for review.

Mitigation: Review the overwrite example before running it and account for the stated benchmark limitation when interpreting results.

## Reference(s):

- [Project homepage](https://github.com/vargHQ/skills/tree/main/media-judge)
- [Checks and thresholds](references/checks.md)
- [Visual review guidance](references/eyes.md)
- [Ranking protocol](references/ranking.md)
- [Judging an AI video without bias](https://varg.ai/how-to/judge-an-ai-video-without-bias)

## Skill Output:

**Output Type(s):** [Analysis, Markdown reports, JSON measurements, Evidence images, Ranked takes]

**Output Format:** [Markdown verdicts, JSON measurements, contact sheets, and evidence frames]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports cover selected checks; some findings require visual review.]

## Skill Version(s):

1.0.7 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
