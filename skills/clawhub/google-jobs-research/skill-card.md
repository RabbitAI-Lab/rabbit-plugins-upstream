## Description:

Searches Google's public careers site (careers.google.com) via the Crawlora API and pulls single job postings by id, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search current public Google Careers postings by role or location and retrieve normalized details for a specific numeric job id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included helper can call arbitrary Crawlora API paths beyond the documented Google Jobs endpoints.

Mitigation: Prefer the documented /google-jobs/search and /google-jobs/job paths, keep the Crawlora key in the environment, and review or restrict the helper before allowing broad agent use.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/google-jobs-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON API output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for live Crawlora API calls.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
