## Description:

Analyzes child bedroom night audio/video for bedtime unrest, fear-of-dark behavior, nightmare wakeups, and out-of-bed safety events, then returns structured soothing recommendations and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and developers of smart nursery devices use this skill to process guardian-authorized bedroom audio/video or URLs for behavior-event detection, soothing-action suggestions, and historical report lookup. It is not a medical diagnostic tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child bedroom media or URLs may be uploaded to a cloud service.

Mitigation: Use only with parent or guardian consent, confirm provider retention and deletion controls, and avoid inputs that include unnecessary bystanders or sensitive content.

Risk: Silent backend identity binding and local token persistence can make report access and credential scope opaque.

Mitigation: Install only where local credential storage, account scoping, and deletion processes are acceptable; avoid use on shared machines unless credentials are isolated.

Risk: Historical cloud reports may expose child sleep, bedroom, or caregiving data.

Mitigation: Limit report access to authorized caregivers, review cloud sharing settings, and delete reports that are no longer needed.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-bedtime-soothing-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown report text with optional JSON/detail output, report links, and historical-report tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write an output file when requested; historical report queries are retrieved from the cloud service.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
