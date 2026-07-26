## Description: <br>
ContactOut helps agents use an OOMOL-connected ContactOut account to search people and companies, enrich profiles, verify emails, retrieve contact availability, and read usage stats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and sales or recruiting operators use this skill to run ContactOut people and company search, enrichment, email verification, contact availability checks, and account usage lookups through the OOMOL oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ContactOut actions may retrieve personal emails, phone availability, LinkedIn profile data, company enrichment data, and account usage stats. <br>
Mitigation: Run requests only when user-directed, review search and enrichment inputs before execution, and limit retrieved data to the user's stated task. <br>
Risk: Connector actions consume the user's connected ContactOut service and may affect billing, credits, or usage quotas. <br>
Mitigation: Use usage stats when relevant, watch for billing or credit errors, and confirm high-volume or broad searches before running them. <br>
Risk: Authentication or connection troubleshooting could expose unnecessary setup steps or connection flows. <br>
Mitigation: Use the existing OOMOL-connected account by default and fall back to setup or connection guidance only after an auth, scope, credential, or missing CLI failure. <br>


## Reference(s): <br>
- [ContactOut homepage](https://contactout.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, JSON, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields when actions run successfully.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
