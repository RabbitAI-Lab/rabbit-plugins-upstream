## Description:

Analyzes retail chain expansion opportunities, candidate-address competition, and rollout sequencing from Amap-copied place text using published DDT store snapshots, without claiming any official Amap affiliation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External retail expansion, site-selection, and operations users use this skill to screen published retail brands, evaluate opportunity cities, compare candidate addresses, and produce focused field-verification checklists. The skill is intended for snapshot-based screening rather than definitive investment, lease, or opening decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends retail brand names, copied addresses, or coordinates to the disclosed DDT service.

Mitigation: Use only data you are comfortable sharing with that service and avoid submitting confidential site plans, secrets, or unrelated personal data.

Risk: The workflow requires a DDT API key for authenticated requests.

Mitigation: Configure the key only in a controlled runtime, do not paste it into chat, and keep it out of logs, skill files, and version control.

Risk: Outputs are based on published retail snapshot data and limited previews, so they may be incomplete or stale for final business decisions.

Mitigation: Treat results as screening evidence, check coverage and data-version notes, and verify candidate locations through field or business review before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-amap-retail-expansion)
- [DDT Claw API homepage](https://gotoshop-ai.com/ddtclaw/)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown with concise recommendations, key metrics, coverage notes, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses published retail data snapshots; may include limited public store previews only when the user provides coordinates or a public store ID.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
