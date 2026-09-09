## Description:

Compare PEA, CTO (compte-titres) and assurance-vie net-of-tax outcomes for a French investor using Vestafolio's simulator API, after asking the simulator's questions (initial capital, monthly contribution, TMI, holding period, expected return, assurance-vie fees).

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to compare French PEA, CTO and assurance-vie investment-envelope outcomes after gathering the simulator inputs and getting consent to call Vestafolio's API.

### Deployment Geography for Use:

France

## Known Risks and Mitigations:

Risk: Investment assumptions are sent to Vestafolio's external API.

Mitigation: Explain the destination and exact fields first, get explicit user agreement, and send only simulator-relevant fields.

Risk: Financial and tax results can be sensitive to assumptions and changing rules.

Mitigation: Ground answers in the API result, state assumptions and limits, and avoid presenting the output as tax advice.

## Reference(s):

- [Vestafolio PEA vs CTO API](https://www.vestafolio.com/api/tools/v1/pea-vs-cto)
- [Vestafolio PEA vs CTO Simulator](https://www.vestafolio.com/simulateurs/pea-vs-cto)
- [ClawHub Skill Page](https://clawhub.ai/vestafolio/skills/vestafolio-pea-vs-cto)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or plain text with summarized simulator inputs, API-derived results, assumptions, warnings and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user agreement before sending simulator-relevant investment assumptions to Vestafolio's external API.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter reports 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
