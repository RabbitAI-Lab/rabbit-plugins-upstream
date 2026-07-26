## Description: <br>
Classifies agent tasks into four risk tiers and maps each tier to verification guidance before work proceeds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent orchestrators use this skill to classify code and configuration tasks by risk, choose verification gates, and decide which tasks can safely run in parallel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses heuristic file-pattern guidance, so unusual tasks may be under-classified if their risk is not visible from paths or file counts. <br>
Mitigation: Escalate uncertain, security-sensitive, data-affecting, irreversible, or production-impacting tasks and apply the higher-tier verification gates. <br>
Risk: The artifact references companion checkpoint skills for deeper review that are not included in this package. <br>
Mitigation: When a referenced checkpoint skill is unavailable, use an equivalent human or lead-agent review before completing RED or CRITICAL tasks. <br>
Risk: Broad safety and verification triggers may cause the skill to appear in contexts where a full risk review is unnecessary. <br>
Mitigation: Use it when risk-tier guidance is desired, and treat documentation-only or purely exploratory work according to the exclusions in the artifact. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-risk-classification) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [Readiness Levels](artifact/modules/readiness-levels.md) <br>
- [Heuristic Classifier](artifact/modules/heuristic-classifier.md) <br>
- [Tier Definitions](artifact/modules/tier-definitions.md) <br>
- [Verification Gates](artifact/modules/verification-gates.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with risk-tier labels, decision rules, and verification gate instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces advisory classifications only; it does not execute code or access external services.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
