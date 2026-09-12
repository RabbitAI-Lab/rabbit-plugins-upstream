## Description:

Help a user find, judge, apply for and rehearse for jobs across discover, assess, apply, and interview modes, producing career reports and application materials without fabricating experience or predicting interview or offer probability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

External job seekers use this skill to search for roles, assess postings, tailor CVs or resumes, prepare cover or motivation letters, and rehearse interviews. It is designed for local-first career workflows where outputs must remain grounded in the user's real profile, answers, and sourced job evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live discovery and AnySearch configuration can expose users to untrusted job-site content, browser automation behavior, or an untrusted API endpoint.

Mitigation: Review setup before installing, use a pinned or verified installer, and set ANYSEARCH_API_BASE_URL only for endpoints you trust.

Risk: Browser-based discovery may interact with a logged-in everyday browser session.

Mitigation: Let the user handle site logins, verification challenges, and browser consent; avoid granting browser access for sources that are not needed.

Risk: Candidate profiles and application records are stored locally for reuse.

Mitigation: Use a user-scoped environment, keep local profile folders access-controlled, and remove retained workspaces when they are no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dong845/skills/job-hunt)
- [README_EN.md](README_EN.md)
- [REFERENCE.md](REFERENCE.md)
- [Agent setup](references/agent-setup.md)
- [Discovery sources](references/discovery-sources.md)
- [Source policy](references/source-policy.md)
- [Browser fallback](references/browser-fallback.md)
- [Evaluation guide](evals/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and application documents, structured YAML/JSON work records, Word documents, PDFs, and shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can generate tailored CVs, optional cover or motivation letters, fit assessments, shortlists, interview briefs, mock transcripts, debriefs, and local delivery folders.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
