## Description: <br>
Minsky Moment helps agents diagnose whether prolonged financial stability is hiding leverage-driven fragility by classifying debt structure, trigger stress, and collapse cascades. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External analysts, developers, and agent users use this skill to examine leveraged companies, sectors, markets, or credit cycles for Minsky-style fragility and produce a structured fragility diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Financial-risk analysis may influence real investment, lending, or counterparty decisions. <br>
Mitigation: Verify financial claims, debt-service data, and current market facts independently before applying the diagnosis to decisions. <br>
Risk: The skill can produce an overconfident diagnosis when cash-flow, debt-service, or rollover data is missing. <br>
Mitigation: Follow the skill's stop rule by naming the data gap instead of forcing a debt-stage classification. <br>
Risk: Users may mistake structural fragility analysis for a prediction of when a collapse will occur. <br>
Mitigation: State that the diagnosis identifies fragility and trigger mechanisms, not market timing. <br>


## Reference(s): <br>
- [Primary Sources](references/sources.md) <br>
- [Method in Action: US Subprime Mortgage Market (2003-2008)](examples/us-subprime-mortgage-market-2003-2008.md) <br>
- [Method in Action: The AI Capex Financing Loop (2023-2026)](examples/ai-capex-circular-financing-2023-2026.md) <br>
- [Hyman P. Minsky, The Financial Instability Hypothesis](https://www.levyinstitute.org/pubs/wp74.pdf) <br>
- [Financial Crisis Inquiry Report](https://www.govinfo.gov/content/pkg/GPO-FCIC/pdf/GPO-FCIC.pdf) <br>
- [NVIDIA Investor Relations](https://investor.nvidia.com) <br>
- [U.S. Bureau of Industry and Security](https://www.bis.doc.gov) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown diagnostic report with structured fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires current debt-service, rollover, lending-standard, and market-stress evidence for reliable diagnosis.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
