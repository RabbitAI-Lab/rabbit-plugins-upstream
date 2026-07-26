## Description: <br>
Apply the substitution principle to position a compound or keyword-plus-modifier domain within the current asking-price market. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abtdomain](https://clawhub.ai/user/abtdomain) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and domain-market analysts use this skill to build a substitution-based Comparative Market Analysis for compound or keyword-plus-modifier domains using currently verified for-sale listings. It supports competitive listing-positioning context for buying or selling, while excluding official appraisals, investment advice, historical-sale calibration, and fixed-target buyer valuation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Domain listing data can be stale, unavailable, or unverifiable, which can make a CMA misleading. <br>
Mitigation: Verify retained comparables against original marketplace pages where possible, record observation dates, and report insufficient current comparable market when the minimum verified-comparable threshold is not met. <br>
Risk: The workflow may be mistaken for an official appraisal, completed-sale estimate, or investment recommendation. <br>
Mitigation: Keep the analysis framed as current asking-price market positioning, include the compliance statement, and avoid buy, sell, or offer-acceptance recommendations. <br>
Risk: Fetching target domains or marketplace pages can expose the agent to unsafe or irrelevant sites. <br>
Mitigation: Run safety checks before fetching target domains, do not fetch domains flagged as malicious, and stop when the target is an active business, brand-dependent case, or otherwise out of scope. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/abtdomain/skills/domain-cma-valuation) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown report with structured tables, source trails, observation dates, limitations, and a compliance statement] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires current listing verification and at least three verified tier-1 or tier-2 comparables before producing a primary listing-positioning range.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
