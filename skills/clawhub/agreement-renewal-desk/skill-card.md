## Description:

Prepares obligation schedules from supplied agreement text and adds their entries to a local renewal schedule.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Legal and account operations staff use the skill to derive dated obligations from supplied agreement sections and optionally append them to a local renewal schedule.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downstream runs append renewal rows to a local CSV in the chosen output directory.

Mitigation: Use a dedicated writable output directory; avoid shared or production folders unless the append is intended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/agreement-renewal-desk)

## Skill Output:

**Output Type(s):** [Structured data, Files]

**Output Format:** [JSON obligation schedule or schedule receipt; downstream also appends a local CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upstream is read-only; downstream writes under the selected output directory.]

## Skill Version(s):

3.0.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
