## Description: <br>
Gov Procurement Analyst helps suppliers, procurement agents, and purchasing teams analyze Chinese government procurement opportunities, bid decisions, compliance risks, contracts, policies, and bid-document drafting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Suppliers, bid teams, procurement agents, and purchasing units use this skill to find public procurement notices, match opportunities to an enterprise profile, assess bid viability, draft bid materials, and review compliance or contract risks. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist sensitive company profile data, qualifications, historical projects, and generated bid materials on the local machine. <br>
Mitigation: Use explicit invocation, avoid sensitive certificates unless local-only processing is confirmed, and review how to list, delete, or disable stored profiles, archives, and material libraries. <br>
Risk: Broad triggers, timed pushes, and update actions may produce or deliver procurement analysis outside the user's intended scope. <br>
Mitigation: Confirm the target project, company, and delivery channel before relying on reports, and disable scheduled pushes or update actions when they are not needed. <br>
Risk: Bid, contract, policy, and complaint guidance may be incomplete or unsuitable for a specific procurement matter. <br>
Mitigation: Have qualified procurement, legal, or finance reviewers check generated reports and filing materials before submission. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/gov-procurement-analyst) <br>
- [Procurement platforms and compliance guide](references/procurement-platforms.md) <br>
- [Anti-scraping best practices](references/anti-scraping-best-practices.md) <br>
- [Enterprise profiling and matching algorithm](references/enterprise-profiling.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown-style reports and guidance with optional JSON files from helper scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist local enterprise profiles, bid archives, material libraries, generated bid documents, and script output files.] <br>

## Skill Version(s): <br>
4.7.0 (source: frontmatter, release evidence, README version history) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
