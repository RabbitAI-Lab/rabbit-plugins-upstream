## Description:

Clinical Trial Chief Advisor helps agents answer clinical-trial methodology, design, compliance, regulatory, safety, operations, QC, and tone questions, while routing real-data, literature, safety-signal, registry, and sample-size needs to sibling clinical-trial skills when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical-trial practitioners, clinicians, nurses, medical students, and agent developers use this skill to get structured clinical-trial guidance, regulatory-methodology support, and routing to companion skills for live registry, safety, literature, and sample-size work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Middle and complex clinical-trial questions and draft answers may be sent to the author's Coze endpoint by default.

Mitigation: Do not enter confidential sponsor data, unpublished protocol details, subject information, credentials, trade secrets, or other restricted content; review or remove auto-approved outbound endpoints before deployment.

Risk: Outbound behavior has weak runtime control according to the authoritative security summary.

Mitigation: Install only where the organization accepts the Coze refinement flow, and prefer local-only handling for simple questions when outbound sharing is not acceptable.

Risk: The bundled shared token is an operational public credential, not a private secret.

Mitigation: Treat the bundled token as public infrastructure for this skill and do not replace it with private credentials unless the deployment owner has reviewed the code and endpoint behavior.

Risk: Optional memory or QA logging can retain sensitive clinical-trial content if enabled.

Mitigation: Keep QA logging disabled unless explicitly needed, review local storage settings, and avoid storing sensitive or regulated content in logs or memory.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/medstatstar/skills/ct-advisor)
- [Project Homepage](https://github.com/medstatstar/ct-advisor)
- [Answer Workflow Steps](references/steps.md)
- [External Search Sites by Workflow](references/search-sites.md)
- [Atomic Task Units](references/units.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text guidance, sometimes with inline commands, routed-skill handoff details, citations, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Simple questions can be answered locally; middle and complex questions may use an author-hosted Coze endpoint for refinement.]

## Skill Version(s):

0.9.53 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
