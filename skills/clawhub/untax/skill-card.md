## Description:

Use Untax for source-backed property assessment research, relevant taxpayer questions, public VA office or form lookup, and explicitly requested private review PDFs, requirements or test checkout workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

Property owners and taxpayers use Untax to research property assessments and tax relief, find public VA offices or forms, and request private veteran review drafts or sandbox checkout workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private VA information could be shared without the user's intended consent.

Mitigation: Review requested account permissions and share VA information only for the selected review when the user explicitly chooses to use it.

Risk: An unsigned veteran review PDF could be mistaken for an official filing or eligibility decision.

Mitigation: Describe generated PDFs as unsigned drafts that are not filed and do not establish eligibility or guarantee county acceptance.

Risk: A sandbox checkout could be mistaken for a real payment or county filing.

Mitigation: Identify sandbox checkout as a test workflow and do not describe it as a live charge, real savings, or completed filing.

## Reference(s):

- [Untax integrations and setup](https://untax.io/integrations/0.4.1)
- [Untax MCP service](https://untax.io/mcp)
- [Untax](https://untax.io)
- [GISDB integration guide](https://gisdb.io/integrations/0.4.1#quick-start)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text, PDF files]

**Output Format:** [Conversational research summaries and guidance; unsigned PDF review drafts when explicitly requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research and drafts depend on available service data, permissions, and user consent.]

## Skill Version(s):

0.4.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
