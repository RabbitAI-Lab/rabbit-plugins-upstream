## Description:

Screens public FDA FAERS adverse-event reports for drug-event safety signals using PRR, ROR, IC, and EBGM, with optional FDA label and China pharmacovigilance bulletin corroboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Pharmacovigilance, clinical-trial, medical, statistical, and regulatory users can use this skill to screen public FAERS reports for potential drug-event signals, compare safety profiles, and produce auditable report artifacts for expert review. It is a screening aid only and does not establish causality or support medication, clinical, or regulatory decisions without qualified review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Under-disclosed home-directory persistence may occur through the ~/.workbuddy/AGENTS.md logging instruction.

Mitigation: Remove or disable that logging instruction before use, and review the installed AGENTS.md behavior before allowing the skill to run.

Risk: The skill performs public FAERS/openFDA queries and writes local report artifacts.

Mitigation: Use a dedicated output directory and confirm detailed retrieval only when those local artifacts are expected.

Risk: openFDA API keys could be mishandled if pasted into chat or bundled with the skill.

Mitigation: Provide keys only through local configuration such as an environment variable, and do not paste keys into conversations.

Risk: Exported case-level reports may contain sensitive public-report details.

Mitigation: Treat generated case-level outputs as sensitive and restrict sharing to qualified reviewers.

Risk: The evidence security guidance calls for updating the requests dependency.

Mitigation: Review and update the requests package before deployment in a managed environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-safety)
- [Publisher profile](https://clawhub.ai/user/medstatstar)
- [Project homepage](https://github.com/medstatstar/ct-safety)
- [openFDA drug event API](https://api.fda.gov/drug/event.json)
- [openFDA API key registration](https://open.fda.gov/api/register/)
- [Methods](references/methods.md)
- [Fetch Pipeline and FAERS API Field Reference](references/fetch_pipeline.md)
- [Evidence Hierarchy and Claim Boundaries for FAERS Output](references/evidence-hierarchy.md)
- [openFDA API Key](references/openfda_api_key.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands; generated reports may be HTML, XLSX, JSON, or Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Core report artifacts are written to the user-selected output directory; optional detailed FAERS retrieval requires explicit confirmation.]

## Skill Version(s):

0.1.36 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
