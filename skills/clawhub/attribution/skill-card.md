## Description: <br>
Helps users figure out which marketing drives conversions and revenue, choose or interpret attribution models, reconcile conflicting numbers across tools, and plan first-party attribution when they control the site or app. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyhaines31](https://clawhub.ai/user/coreyhaines31) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams, founders, analysts, and developers use this skill to choose defensible attribution approaches, interpret conflicting conversion and revenue numbers, and decide when to instrument first-party attribution. It supports both non-engineering attribution readouts and implementation guidance for joining marketing touches to conversions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Attribution guidance can involve privacy-sensitive analytics identifiers and conversion metadata shared with third-party tools. <br>
Mitigation: Confirm privacy notices, consent setup, vendor contracts, and retention rules before production use. <br>
Risk: First-party attribution implementations may accidentally expose emails or stable user IDs in URLs or webhook logs. <br>
Mitigation: Use fail-closed safeguards, avoid sending emails or stable user IDs in URLs, validate webhook inputs, and test webhook validation before production use. <br>


## Reference(s): <br>
- [Attribution Models](references/attribution-models.md) <br>
- [Attribution by Business Type](references/by-business-type.md) <br>
- [First-Party Attribution](references/first-party-tracking.md) <br>
- [Measurement Paradigms](references/measurement-paradigms.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/coreyhaines31/skills/attribution) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance, configuration] <br>
**Output Format:** [Markdown attribution readouts, recommendations, implementation guidance, and occasional code or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tables, confidence levels, source-of-truth recommendations, model comparisons, and privacy or implementation guardrails.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
