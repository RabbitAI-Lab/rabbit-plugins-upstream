## Description: <br>
Analyzes pet grooming images or videos through server-side APIs to assess coat matting, shed-hair volume, grooming effectiveness, and hairball risk, with optional history lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet-care users and developers use this skill to submit pet grooming media and receive structured grooming-effectiveness, matting, shed-hair, and hairball-risk results for care guidance. The outputs are for pet-care reference and are not a medical diagnosis or treatment plan. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet images, videos, URLs, generated identity values, and report history may be handled by lifeemergence.com services. <br>
Mitigation: Use the skill only where cloud processing and account-linked history are acceptable, and avoid submitting sensitive media unless retention and deletion expectations are clear. <br>
Risk: The skill may silently create or reuse a local identity and store account tokens locally. <br>
Mitigation: Run it in an isolated workspace or account, review local state before and after use, and prefer releases that document token storage, revocation, and deletion. <br>
Risk: The server-side analysis is a pet-care aid and may not be reliable enough for medical decisions. <br>
Mitigation: Treat results as grooming guidance only and consult a veterinary professional for health concerns, severe matting, abnormal shedding, or suspected hairball complications. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-grooming-effectiveness-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown text with embedded JSON-style structured analysis and report links; optional file output when --output is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a server-generated report export URL and historical report JSON when listing prior reports.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
