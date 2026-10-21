## Description:

Collects recorded calls each morning, turns them into go-to-market log entries, and proposes recurring insights as reviewable repository updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, revenue operations, and engineering teams use this skill to capture call transcripts, draft structured call notes, and propose evidence-backed go-to-market context changes through pull requests for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted transcript text may influence a coding agent that can propose repository changes.

Mitigation: Treat transcript content as data, review generated changes before merging, and restrict repository credentials.

Risk: Recorder credentials or workspace secrets could leak into commits or pull request descriptions.

Mitigation: Limit workspace environment access and scan changes and pull request text for secrets before publishing.

Risk: An unverified recorder adapter may miss calls or capture the wrong data in a scheduled run.

Mitigation: Test the selected adapter with real calls in dry-run mode and review the deployment plan before enabling the schedule.

## Reference(s):

- [Call Capture on ClawHub](https://clawhub.ai/cargo-ai/skills/call-capture)
- [Project homepage (release metadata)](https://github.com/getcargohq/gtm-skills)
- [Recorder integration reference](references/recorder-apis.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown call logs and context proposals, with setup guidance and a pull request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposed changes require human review and merge.]

## Skill Version(s):

0.1.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
