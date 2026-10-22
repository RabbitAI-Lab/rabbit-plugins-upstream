## Description:

Collect what is new in AI over the last 24 hours across X, Hugging Face, GitHub, and sitemaps, deduplicated into a report of names that are starting to surge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuyansen](https://clawhub.ai/user/zhuyansen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and market researchers use this skill to create a daily report of emerging AI models, products, and repositories to inform keyword research. It gathers signals from configured X accounts, Hugging Face, GitHub, and sitemaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on separately downloaded radar code.

Mitigation: Review the code and pin a known revision before running it.

Risk: Configured sources and API use can incur charges, and X monitoring requires an AIsa key or CLI login.

Mitigation: Check enabled sources and expected costs before running, and use an AIsa key with spending limits.

Risk: Reports and snapshots remain on the local machine.

Mitigation: Protect local report and snapshot files according to their contents.

## Reference(s):

- [ClawHub ai-listening release](https://clawhub.ai/zhuyansen/skills/ai-listening)
- [new-term-radar project](https://github.com/zhuyansen/new-term-radar)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Markdown report and JSON data file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A first run may only build snapshots and produce limited results.]

## Skill Version(s):

0.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
