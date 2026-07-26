## Description: <br>
Turns a user's Google Scholar or academic paper search request into a confirmed Dataify Scraper API call. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare and submit Google Scholar searches through Dataify after reviewing the request parameters. It is suited for academic search workflows that need structured Dataify API request construction and raw response return. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit Google Scholar search parameters to Dataify using a user-provided token. <br>
Mitigation: Review the confirmation table before approving each API call and use only a Dataify token appropriate for these requests. <br>
Risk: Incorrect inferred parameters could produce an unintended academic search. <br>
Mitigation: Confirm or modify the displayed field values before allowing the skill to call the API. <br>


## Reference(s): <br>
- [Dataify Google Scholar API Reference](references/google_scholar_api.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, API calls, JSON, guidance] <br>
**Output Format:** [Markdown confirmation table followed by raw Dataify API response body] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before API calls and returns the API response without post-processing.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
