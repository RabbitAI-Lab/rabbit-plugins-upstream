## Description: <br>
Audit any website for AI search visibility (GEO / AEO) by fetching public site surfaces, running a weighted readiness checklist, and returning a scored gap report with concrete fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[supersky0820](https://clawhub.ai/user/supersky0820) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External site owners, marketers, and SEO practitioners use this skill to assess whether a public website is crawlable, parseable, and ready to be quoted by AI answer engines. It reports AI readiness gaps and fixes while distinguishing readiness from live AI citation status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches public pages from domains the user asks it to audit. <br>
Mitigation: Run it only against public websites the user is authorized to assess, and avoid supplying private or credentialed URLs. <br>
Risk: A static readiness score may be mistaken for proof that AI engines currently cite the site. <br>
Mitigation: State that the report measures AI readiness, not live AI citation status, and keep live citation status in the not-measurable section. <br>
Risk: Fetch failures or unavailable signals could lead to misleading conclusions if treated as failures. <br>
Mitigation: Mark unmeasurable checks as not measurable and exclude them from the score, preserving traceability to fetched bytes. <br>
Risk: Reports may include TriRank service links from the skill's explanatory material. <br>
Mitigation: Keep those links contextual and do not present them as required for completing the static audit. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/supersky0820/trirank-skills/tree/main/skills/trirank-geo-audit) <br>
- [ClawHub skill page](https://clawhub.ai/supersky0820/skills/trirank-geo-audit) <br>
- [TriRank AI visibility benchmark](https://trirankai.com/data/ai-visibility-benchmark) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown scored audit report with gaps, warnings, passing checks, and not-measurable disclosures] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses fetched public webpage evidence; live AI citation status is excluded from the score.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
