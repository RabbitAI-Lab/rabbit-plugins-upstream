## Description:

Rewrites an Amazon US listing from a spec sheet, checks the title and bullet limits, and flags the claim words Amazon restricts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rapidworker1](https://clawhub.ai/user/rapidworker1)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon US sellers and brand managers use the skill to turn product specifications and keywords into listing copy, then check length and flag claims that need review before manual submission.

### Deployment Geography for Use:

United States (Amazon US marketplace)

## Known Risks and Mitigations:

Risk: Automated checks are limited and do not establish Amazon compliance; rewritten copy, category limits, and claims may need correction.

Mitigation: Manually review the copy, applicable category limits, and substantiation for claims before use; do not treat a clean report as proof of compliance.

Risk: The lint script replaces lint-report.md in its selected output folder, and the optional Windows app is unsigned.

Mitigation: Choose an output folder where replacing lint-report.md is acceptable. Treat the separate Windows app as a distinct trust decision and verify the download before running it.

## Reference(s):

- [Amazon US listing rules](references/amazon-listing-rules.md)
- [ClawHub release page](https://clawhub.ai/rapidworker1/skills/amazon-listing-optimizer)
- [Optional Windows app security information](https://github.com/rapidworker1/Multiple-AI-models-Toolkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration]

**Output Format:** [Amazon listing copy with a Markdown lint report; YAML product-spec input template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft title, five bullets, search terms, and claim flags; local checks do not upload or publish listings.]

## Skill Version(s):

1.0.6 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
