## Description:

Measures finished videos, images, and audio for timed defects with supporting evidence, then ranks takes by their findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media creators use the skill to review finished AI-made videos, images, and audio, inspect measured defects, and rank alternate takes before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports a suspicious verdict because installation examples use an unpinned installer and scripts require undeclared network and environment capabilities; it found no clear malicious intent.

Mitigation: Before installation, verify the installer and skill revision from trusted sources, then check whether network and environment access fit the runtime.

Risk: The security scan was partial because some referenced paths were missing, so its evidence is incomplete.

Mitigation: Treat the scan as incomplete and review the skill and its referenced paths before relying on it.

Risk: Benchmark claims may be unreliable if their timestamps or evaluation context are not valid.

Mitigation: Do not rely on benchmark claims without checking their timestamp validity and test context.

## Reference(s):

- [Media Judge project page](https://github.com/vargHQ/skills/tree/main/media-judge)
- [Check definitions and thresholds](artifact/references/checks.md)
- [Visual review guidance](artifact/references/eyes.md)
- [Ranking protocol](artifact/references/ranking.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [Markdown verdict and ranking report, JSON measurement facts, and timestamped evidence images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports measured checks, review prompts, and ranked takes with evidence; findings require human review.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
