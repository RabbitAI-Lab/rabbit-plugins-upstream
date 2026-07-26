## Description: <br>
Audits a domain's authority, trust, and citation credibility by running a peer-relative 40-item CITE profile with evidence coverage and verified manipulation or penalty veto checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, SEO, and GEO practitioners use this skill to audit one domain against a locked peer cohort for citation-trust readiness. It helps identify evidence gaps, verified veto risks, CITE dimension results, and practical remediation steps before a rerun. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may rely on incomplete backlink, search, reputation, or authorized console evidence, which can leave CITE items Unknown and prevent a comparable total score. <br>
Mitigation: Require a locked peer cohort, dated evidence, explicit Unknown markings for missing qualified items, and preserve NOT_SCORED when required evidence or runtime support is unavailable. <br>
Risk: A saved audit artifact could persist sensitive or unnecessary evidence if written without clear authorization. <br>
Mitigation: Persist only after explicit user authorization, write only the permissioned v3 audit artifact, and validate the target path and artifact before saving. <br>


## Reference(s): <br>
- [Domain Authority Auditor on ClawHub](https://clawhub.ai/aaron-he-zhu/skills/domain-authority-auditor) <br>
- [Source Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Standalone Auditor Runtime](references/auditor-runtime.md) <br>
- [CITE Domain Authority Report Example](references/example-report.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with optional permissioned audit artifact and shell validation commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports status, verdict, score_state, CITE coverage, confidence, verified risks, unresolved Unknown items, remediation steps, and provenance appendix when requested.] <br>

## Skill Version(s): <br>
19.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
