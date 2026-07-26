## Description: <br>
Triages tachograph infringements, identifies common patterns, and outputs what-to-check-next prompts and weekly review notes for UK tacho/WTD reviews. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kowl64](https://clawhub.ai/user/kowl64) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Transport managers and compliance reviewers use this skill to turn weekly UK tachograph and WTD infringement records into neutral triage notes, root-cause prompts, and follow-up actions. It is intended as a compliance review aid, not a final HR or legal decision tool. <br>

### Deployment Geography for Use: <br>
United Kingdom <br>

## Known Risks and Mitigations: <br>
Risk: Outputs could be mistaken for final compliance, employment, HR, or legal decisions. <br>
Mitigation: Review outputs under the organization's privacy, employment, and transport-compliance policies before acting. <br>
Risk: Incomplete tachograph, WTD, or RAG-history inputs can lead to misleading triage conclusions. <br>
Mitigation: Provide only authorized records and ask for missing driver lists, periods, data gaps, or prior RAG history before escalating follow-up actions. <br>
Risk: Driver infringement summaries may contain personal or sensitive operational information. <br>
Mitigation: Only process records the user is authorized to use and keep the generated notes limited to factual, neutral compliance follow-up. <br>


## Reference(s): <br>
- [Common infringement patterns](references/common-infringement-patterns.md) <br>
- [Weekly tacho and WTD compliance review pack template](assets/weekly-review-pack-template.md) <br>
- [What to check next playbook](assets/what-to-check-next-playbook.md) <br>
- [ClawHub skill page](https://clawhub.ai/kowl64/skills/tachograph-infringement-triage-root-cause-uk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown review notes and action summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces manager-facing weekly review packs and per-driver triage action summaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
