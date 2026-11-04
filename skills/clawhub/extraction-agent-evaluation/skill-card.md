## Description:

Design evidence-backed structured extraction workflows and evaluate field truth, grounding, record completeness and matching errors. Use for extraction schemas, agent evaluation and source-drift plans rather than source discovery or a whole dataset purchasing decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redrookai](https://clawhub.ai/user/redrookai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data teams use this skill to design structured extraction workflows and evaluate field accuracy, source grounding, record completeness, and matching errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A valid record or matching source pointer may be mistaken for proof that extracted facts are supported by the source.

Mitigation: Review source support for the correct entity and time separately, and use a stronger source check when the material requires it.

Risk: The helper may read evaluation files that should not be in its runtime scope.

Mitigation: Use it only with evaluation files intended for the agent, and configure access restrictions in the host environment.

## Reference(s):

- [Worked example: trials at facilities](artifact/references/example.md)
- [Practice: design the extraction and its test](artifact/references/practice.md)
- [Flat record scoring helper](artifact/scripts/score_flat_records.py)
- [ClawHub release](https://clawhub.ai/redrookai/skills/extraction-agent-evaluation)

## Skill Output:

**Output Type(s):** [Guidance, Code, JSON]

**Output Format:** [Markdown guidance, Python scoring helper, and JSON score report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The optional scorer handles a fixed flat-record schema; source-pointer consistency does not establish semantic support.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
