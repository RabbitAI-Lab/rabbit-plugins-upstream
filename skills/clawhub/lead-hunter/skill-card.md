## Description: <br>
Automated lead generation and enrichment for AI agents that helps find prospects, enrich contact and company data, score leads, and prepare CRM-ready outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[galacticpuffin](https://clawhub.ai/user/galacticpuffin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and sales operators use this skill to configure lead discovery, enrichment, scoring, CRM export, and outreach-trigger workflows for B2B prospecting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can handle personal lead data through enrichment, email discovery, CRM export, and webhook workflows. <br>
Mitigation: Minimize collected fields, store lead files securely, define retention and deletion rules, and avoid sending full lead records to untrusted destinations. <br>
Risk: The skill references scraping, email probing, and discovery sources that may be restricted by platform terms or compliance obligations. <br>
Mitigation: Use only lawful, consent-aware sources, avoid scraping where terms do not allow it, and gate any high-risk collection method behind explicit review. <br>
Risk: Outreach triggers can move from lead scoring into automated contact workflows. <br>
Mitigation: Disable or require approval for automated outreach until the workflow, consent basis, suppression lists, and sender controls have been reviewed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/galacticpuffin/skills/lead-hunter) <br>
- [Publisher Profile](https://clawhub.ai/user/galacticpuffin) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, shell commands] <br>
**Output Format:** [Markdown with YAML and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces lead discovery, enrichment, scoring, export, webhook, and CRM integration guidance for an agent.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
