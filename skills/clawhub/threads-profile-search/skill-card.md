## Description: <br>
Discovers Threads user accounts by keyword, extracting profile data including username, display name, verification status, biography, and follower count. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to find Threads accounts by keyword and optionally enrich matching profiles with public profile metadata such as biography and follower counts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use an active Threads browser session when calling the profile API. <br>
Mitigation: Run it only in the intended browser session and review whether the session context is appropriate before collecting profile details. <br>
Risk: Profile metadata collection may be inappropriate for sensitive, non-consensual, or policy-restricted scraping workflows. <br>
Mitigation: Use it only for compliant profile discovery tasks and avoid collecting or reusing data in ways that violate user expectations or platform rules. <br>
Risk: Threads may rate-limit profile enrichment requests. <br>
Mitigation: Test small batches first, add delays between enrichment calls, and resume from saved results after failures. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/threads-profile-search) <br>
- [Publisher profile](https://clawhub.ai/user/browseract-cli) <br>
- [Threads profile search](https://www.threads.com/search/?q={keyword}&type=profiles) <br>
- [Threads profile detail endpoint](https://www.threads.com/api/v1/users/web_profile_info/?username=) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON profile records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Profile search is limited to approximately 16 unauthenticated results per keyword; enrichment calls should be spaced to reduce rate limiting.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
