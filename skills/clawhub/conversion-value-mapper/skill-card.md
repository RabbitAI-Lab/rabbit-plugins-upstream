## Description: <br>
Defines and QAs a paid-ad conversion value model so value-based bidding can optimize toward profit, including net-value adjustment, proxy values for non-revenue actions, value-rule logic, and pre-launch reconciliation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams, agencies, and operators use this skill to define and check conversion values before launching or scaling tROAS, max-conversion-value, or similar value-based paid bidding. It helps map revenue to margin-adjusted value, derive proxy values for leads or calls, and identify value-integrity blockers before launch. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Use may involve business-sensitive revenue, margin, COGS, or lead-conversion data. <br>
Mitigation: Provide only data appropriate for agent processing and confirm any memory-save prompt before allowing results to persist across sessions. <br>
Risk: Incorrect value assumptions can lead paid bidding systems to optimize toward misleading conversion value. <br>
Mitigation: Review the margin inputs, proxy-value derivations, and value-vs-count reconciliation before using the resulting value model for launch decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/conversion-value-mapper) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown value-model spec and pre-launch value QA sheet] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include formulas, value-rule decisions, data-source labels, value-vs-count reconciliation findings, launch-readiness status, and optional memory handoff after user approval.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
