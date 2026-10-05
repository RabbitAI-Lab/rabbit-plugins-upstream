## Description:

Analyzes tomato and chili flower or fruit images and videos to estimate fruit-set rates and provide growing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Home growers and greenhouse operators use plant images or videos to assess flowering and fruit set, review analysis reports, and inform pollination or growing-condition adjustments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, or media URLs may be sent to external analysis services.

Mitigation: Use only media approved for remote processing and confirm the destination before use.

Risk: The skill may silently create or reuse an account identity, store tokens locally, and retrieve cloud report history.

Mitigation: Review account-linked storage and history behavior before installation; protect the local workspace and tokens.

Risk: Packaged code and documentation do not consistently match the plant-analysis description or release version.

Mitigation: Verify the installed version and test actual outputs before relying on analysis or growing guidance.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-flowering-fruit-set-rate-analysis-analysis)
- [Packaged API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown table of historical reports, with report links; JSON where available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be saved to a file.]

## Skill Version(s):

1.0.12 (source: ClawHub release; packaged skill lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
