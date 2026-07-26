## Description: <br>
Qa Team Skills helps QA teams use a unified /qa entry point and eight standardized workflows to review requirements, design test cases, test agents, analyze defects, generate reports, manage QA work, and retain local testing memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
QA engineers, test managers, and developers use this skill to standardize AI-assisted testing work across requirement review, test-case design, agent testing, defect analysis, reporting, and team management. Teams can use its local memory workflow to reuse test cases, defect patterns, standards, and reports across product iterations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local memory can retain test cases, defect details, reports, standards, logs, screenshots, or other sensitive QA inputs. <br>
Mitigation: Use approved and redacted test data, avoid production credentials and customer personal data, confirm the memory location before use, and delete product memory directories when retention is no longer allowed. <br>
Risk: Generated test cases, reports, quality assessments, and root-cause analyses may be incomplete or misleading if accepted without review. <br>
Mitigation: Review P0 test cases, verify generated test data in the test environment, sample-check report data against source systems, and require second-person review for medium- or low-confidence root-cause analysis. <br>
Risk: Optional evaluation workflows can call an external LLM API when explicitly run with user-provided credentials. <br>
Mitigation: Run optional evaluation only in approved environments, use sanitized evaluation data, and keep API keys in environment variables rather than test content or reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-team-skills) <br>
- [Publisher profile](https://clawhub.ai/user/kokxi) <br>
- [README](README.md) <br>
- [User manual](docs/user-manual.md) <br>
- [Memory module](memory/README.md) <br>
- [Process integration guide](docs/process-integration.md) <br>
- [CI and quality validation](docs/ci-testing.md) <br>
- [skills.sh listing](https://skills.sh/Kokxi/qa-team-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance, configuration] <br>
**Output Format:** [Markdown and structured JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stateful workflows may persist test cases, defects, reports, and standards in local memory files.] <br>

## Skill Version(s): <br>
v1.5.4 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
