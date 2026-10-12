## Description:

Analyzes videos of an older person's hand at rest for tremor frequency and amplitude and provides a screening report for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Family caregivers and care providers use recorded hand-at-rest video to screen for possible tremor, review past reports, and decide when to seek clinical assessment. Results are not a diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Health-related videos or URLs are sent to external lifeemergence.com services.

Mitigation: Obtain consent from everyone affected before use and restrict sharing of recordings and report links.

Risk: Persistent local identity and token records, including a shared default identity, may expose report history across users.

Mitigation: Avoid shared workspaces unless per-user identity isolation is enforced; restrict access to stored records and history.

Risk: A tremor screening result could be mistaken for a medical diagnosis.

Mitigation: Treat results as screening guidance and seek professional neurological assessment for concerning findings.

## Reference(s):

- [Skill listing](https://clawhub.ai/18072937735/skills/smyx-elderly-hand-tremor-detection-analysis)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured report or JSON; history may include report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save a report to a local file on request.]

## Skill Version(s):

1.0.13 (source: ClawHub release; bundled SKILL.md states 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
