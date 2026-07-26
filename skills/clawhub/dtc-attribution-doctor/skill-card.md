## Description: <br>
Diagnoses ROAS declines and attribution gaps for DTC storefronts by comparing Convbox first-party attribution data with platform-reported metrics and producing quantified recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lcolton](https://clawhub.ai/user/lcolton) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketing operators, founders, and analysts use this skill to investigate DTC growth, ROAS, attribution, creative, conversion, budget, and profit questions using aggregated Convbox data. It returns diagnostic findings, reports, and next-step recommendations while leaving campaign, budget, bid, and storefront changes to human execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires agent access to Convbox aggregated store and ad-performance data through CONVBOX_API_KEY. <br>
Mitigation: Install only in agent environments authorized to access that store data, keep the key in secure environment configuration, and do not expose it in prompts, logs, or shared files. <br>
Risk: Saved store context in memory.md may contain business profile, benchmarks, and preferences. <br>
Mitigation: Review stored context and avoid sharing the same agent profile with unauthorized users. <br>
Risk: Budget, bid, campaign, and storefront recommendations can affect business performance if applied blindly. <br>
Mitigation: Treat outputs as analysis and proposals that require human review and execution in the relevant platforms. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lcolton/skills/dtc-roas-doctor) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/lcolton) <br>
- [Clawdis homepage](https://github.com/RTOAI/convbox-diagclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports and diagnostic guidance, with optional shell commands for configuration health checks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses CONVBOX_API_KEY to access aggregated Convbox store and ad-performance data; recommendations require human review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
