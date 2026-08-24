## Description:

Normalize the final JSON output of a single-session CTR product-card click diagnosis. Use after the diagnosis draft is complete and before replying, whenever the report must contain exactly the agreed query, clicked item, unclicked items, five fixed dimensions, structured suggestions, and limitations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rawven](https://clawhub.ai/user/rawven)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill as the final formatting and validation step for single-session CTR product-card click diagnosis reports before returning the normalized JSON response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill echoes normalized CTR session and report content to stdout as the final answer.

Mitigation: Provide only the CTR session and draft report content intended for release, and review the normalized JSON before sharing it externally.

Risk: The normalizer validates report structure but does not verify the factual correctness of the diagnosis.

Mitigation: Complete comparison and image-fact collection before running the skill, and treat any unknown dimensions or dropped suggestions as cues to fix the draft.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/Rawven/ctr-json-normalizer)
- [ClawHub skill page](https://clawhub.ai/rawven/skills/ctr-json-normalizer)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Minified JSON emitted to stdout, or an error JSON object for invalid drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normalizes candidate item coverage, dimension order, allowed status values, suggestion shape, and limitations without inventing factual claims.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
