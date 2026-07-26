## Description: <br>
Classifies product features into Kano categories so product teams can prune waste and choose an MDP-focused launch scope. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[monikazapisekstudio](https://clawhub.ai/user/monikazapisekstudio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers, designers, founders, and product engineers use this skill to triage concrete feature backlogs, classify features with the Kano model, and decide what to keep, kill, defer, or research before launch. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is intentionally opinionated and may push back during general backlog or MVP discussions where neutral product-planning help is expected. <br>
Mitigation: Invoke it explicitly for Kano analysis, feature pruning, or MDP-vs-MVP scope decisions, and override or ignore its stance when a neutral planning discussion is needed. <br>
Risk: Feature classifications can be misleading when the user lacks concrete feature names, target segment, product stage, constraints, or validation evidence. <br>
Mitigation: Require those inputs before classification, mark unsupported judgments as low confidence or Questionable, and recommend lightweight validation before committing to build. <br>
Risk: Market-access prerequisites such as SOC2, HIPAA, GDPR, PCI-DSS, FedRAMP, data residency, or SSO can be misread as user-facing Kano features. <br>
Mitigation: Keep prerequisites in a separate launch-gate track and apply Kano only to user-facing feature behavior or UI elements. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/monikazapisekstudio/skills/kano-model-strategist) <br>
- [README](README.md) <br>
- [Evaluation Evidence](EVIDENCE.md) <br>
- [Attribution](ATTRIBUTION.md) <br>
- [Kano Classification Reference](references/kano-classification.md) <br>
- [Kano vs MDP vs MVP Decision Logic](references/kano-vs-mdpmvp.md) <br>
- [Experience Rot Checklist](references/experience-rot-checklist.md) <br>
- [CEO Pushback Scripts](references/ceo-pushback-scripts.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown backlog table with concise decision sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Limits backlog tables to 15 rows, uses T-shirt sizing for effort estimates, and requires concrete feature names, target segment, product stage, and constraints.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
