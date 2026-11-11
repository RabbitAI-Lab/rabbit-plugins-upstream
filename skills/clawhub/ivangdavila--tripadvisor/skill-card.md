## Description:

Find and compare Tripadvisor hotels, restaurants, and attractions with official API workflows, URL-first navigation, and policy-safe data handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

External users and travel-planning agents use this skill to search Tripadvisor destinations, compare hotels, restaurants, and attractions, and produce ranked shortlists with source mode, tradeoffs, and unresolved uncertainties.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tripadvisor API keys can appear in URL command arguments or logs when using the documented curl workflows.

Mitigation: Keep shell tracing and verbose logging off, redact the key in request logs, and rotate or limit the API key if exposure is suspected.

Risk: Travel searches and lightweight filters are sent to Tripadvisor services during API or web workflows.

Mitigation: Use the skill only when sharing that travel context with Tripadvisor is acceptable, and avoid sending unnecessary sensitive personal details.

Risk: Broad activation on terms such as hotels or attractions can cause recurring preferences and shortlists to be stored locally.

Mitigation: Confirm activation and first-write behavior before creating files under ~/tripadvisor/, and keep stored preferences minimal.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/tripadvisor)
- [Skill Homepage](https://clawic.com/skills/tripadvisor)
- [Tripadvisor Location Search API](https://api.tripadvisor.com/api/partner/2.0/location/search)
- [Tripadvisor Location Details API](https://api.tripadvisor.com/api/partner/2.0/location/{id})
- [Tripadvisor Website](https://www.tripadvisor.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, ranked shortlists, rationale, source mode, and uncertainty notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local Tripadvisor preference, cache, session, request-log, shortlist, and archive files under ~/tripadvisor/ after user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
