## Description: <br>
Answer Research KB dialogue questions with team-overview-guided web search, external citations, optional reference attachments, and no QA persistence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[myd2002](https://clawhub.ai/user/myd2002) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Research KB users use this skill to answer web-search-enabled dialogue questions by combining team overview context with current external sources and citations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports an authenticated repository write helper that does not fit the skill's no-persistence claim. <br>
Mitigation: Install only with a read-only Gitea bot token, or remove the unused upsert_text write helper before granting repository credentials. <br>
Risk: The skill reads team KB overview and catalog content, previews supplied attachments, uses web search or fetch tools, and writes local result JSON. <br>
Mitigation: Review retrieved citations and avoid supplying sensitive attachments or repository credentials beyond the intended read-only KB query workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/myd2002/skills/kb-web-query) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON] <br>
**Output Format:** [JSON result file containing a Markdown answer with team-context and external-source citations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [QA persistence is disabled; answers should include verifiable external web sources when web search is used.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
