## Description:

Generates a Heluo Lishu cultural life-reading by collecting birth details, computing natal and later-life hexagrams, arranging major luck cycles and yearly readings, and presenting the result as Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leahlu0124-creator](https://clawhub.ai/user/leahlu0124-creator)

### License/Terms of Use:

MIT-0

## Use Case:

External users interested in Heluo Lishu or Chinese divination use this skill as a cultural-reference assistant to produce a Markdown life-reading from birth details and to explain specific years on request. Agents use its bundled scripts and reference data to calculate hexagrams, major luck periods, yearly frames, and source-based readings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for personal birth details and birthplace.

Mitigation: Collect only the details needed for the reading, avoid sharing them outside the session, and do not retain them unless the user explicitly requests it.

Risk: Users may over-rely on a fortune-reading output for important life decisions.

Mitigation: Present outputs as entertainment or cultural reference and avoid framing them as professional medical, legal, financial, or life-planning advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/leahlu0124-creator/skills/heluo-lifetime)
- [Publisher profile](https://clawhub.ai/user/leahlu0124-creator)
- [Heluo lifetime skill instructions](artifact/SKILL.md)
- [Heluo natal hexagram algorithm](artifact/references/heluo-algorithm.md)
- [Major luck and yearly algorithm](artifact/references/dayun-liunian.md)
- [Earlier-to-later hexagram transformation](artifact/references/xiantian-houtian.md)
- [Raw source line index](artifact/references/raw-index.md)
- [Juan 4 index data](artifact/references/juan4_index.json)
- [Yao text reference data](artifact/references/yaoci.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown life-reading with quoted source passages; scripts may emit JSON or plain text calculation results for the agent to incorporate.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided birth details and bundled local reference data; evidence reports no hidden network, credential, persistence, or privileged behavior.]

## Skill Version(s):

1.1.1 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
