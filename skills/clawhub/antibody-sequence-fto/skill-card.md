## Description:

Screens antibody and other biosequence patent similarity and claim relevance to support early FTO risk checks before formal legal analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

R&D, IP, and patent-search teams use this skill to screen antibody heavy-chain and light-chain protein sequences against patent sequence and target-landscape evidence. It produces a preliminary FTO risk report with source-linked findings for follow-up review by patent counsel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted antibody sequences may be confidential research or commercial data.

Mitigation: Use the skill only with approved tools and providers for the relevant confidentiality requirements.

Risk: The generated FTO report is preliminary and may not fully resolve claim-scope or jurisdiction-specific patent risk.

Mitigation: Have patent counsel review relevant claims and source-linked evidence before making FTO or launch decisions.

Risk: Sequence identity, claimed status, patent numbers, or claims could be misleading if generated without returned tool evidence.

Mitigation: Require source-linked findings and explicitly state when search tools return no supporting result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/antibody-sequence-fto)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Structured HTML report with source-linked tables, risk summaries, and prioritized recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report sections cover sequence information, HC and LC comparison results, patent landscape, risk assessment, action recommendations, and PatSnap source links.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
