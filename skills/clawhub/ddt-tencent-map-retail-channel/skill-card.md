## Description:

Analyzes retail channel structure, city coverage, competitor differences, and market opportunities from Tencent Map address text using DDT published store snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts and business users use this skill to evaluate published retail brand footprints, category mix, city coverage, nearby stores, and competitor differences from brand names, map address text, coordinates, or public store IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Retail brands, addresses, coordinates, or store IDs may be shared with the DDT service during analysis.

Mitigation: Confirm the user trusts the DDT service for the requested analysis and only submit inputs needed for the retail-channel task.

Risk: The DDT API key could be exposed if pasted into chat, files, logs, or version control.

Mitigation: Keep the API key in environment variables only and never include the real key in generated output.

Risk: Coverage gaps, truncated previews, or snapshot timing could lead to overstated retail conclusions.

Mitigation: Check API coverage, data version, and truncation fields; label unavailable data as not covered and avoid inferring openings, closures, or complete market lists.

Risk: Using the skill outside its retail scope could produce misleading channel or competitor analysis.

Mitigation: Stop non-retail requests and direct the user to the appropriate industry-specific skill or workflow.

## Reference(s):

- [DDT Claw Homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub Skill Page](https://clawhub.ai/horacetu/skills/ddt-tencent-map-retail-channel)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown narrative with concise metrics, coverage notes, and optional curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DDT_API_KEY; uses published retail snapshots and limited public store previews.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
