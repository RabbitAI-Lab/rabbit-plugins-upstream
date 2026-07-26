## Description: <br>
Helps QA reviewers find AI-generated test-case blind spots across sequencing, concurrency, resource contention, state accumulation, data consistency, and third-party integration, then produce supplemental test cases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and test reviewers use this skill after AI-generated test cases have been reviewed to identify missing coverage and generate traceable supplemental cases for known AI blindspot categories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad coverage prompts and add a fixed six-category review structure when a lighter answer would be enough. <br>
Mitigation: Use it for post-review blindspot analysis or explicit omission checks, and keep the response scoped to categories relevant to the user's request. <br>
Risk: Supplemental test cases may not be directly executable without product-specific requirements, environments, or constraints. <br>
Mitigation: Have QA reviewers validate generated cases against the requirements, system behavior, and available test environment before adding them to a test suite. <br>


## Reference(s): <br>
- [Six Blindspot Details](references/blindspot-details.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-ai-blindspot-compensation) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown report with tables and traceable supplemental test-case entries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supplemental cases are expected to include blindspot IDs and related requirement or original test-case IDs when available.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
