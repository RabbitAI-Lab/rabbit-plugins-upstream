## Description:

Using fixed cameras in multiple zones of a solo-living elder's home, the skill analyzes video streams for human activity and returns a long-term no-activity alert when no movement is detected within the configured window, defaulting to 12 hours.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, care-platform operators, and smart-home integrators use this skill to analyze fixed-camera video from solo-living elder homes or community elder-care settings, estimate inactivity duration, and produce structured alert results for human follow-up. The skill is an auxiliary monitoring aid and does not provide medical diagnosis or rescue instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home monitoring video and report metadata are highly sensitive and may be sent to remote services.

Mitigation: Use the skill only with informed consent from the monitored person or an authorized guardian, confirm the configured endpoints before deployment, and avoid visual monitoring in highly private areas when a less intrusive sensor can meet the need.

Risk: The skill silently manages persistent identity values and tokens.

Mitigation: Review local storage and token handling before installation, rotate credentials when moving environments, and limit access to machines that run the skill.

Risk: A no-activity alert can be wrong because camera coverage, lighting, file quality, or model output may be incomplete.

Mitigation: Treat alerts as prompts for human verification, not as medical conclusions or rescue instructions, and verify camera placement and supported input formats before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-long-term-immobility-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown or text containing structured JSON-style monitoring results, alert status, report links, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report export links and historical report listings returned from the configured remote service.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter declares 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
