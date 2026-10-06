## Description:

Plans a translation setting and builds a local translation job entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Localization teams use this skill to select a translation setting from a request and record a local translation job entry using that setting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input may expose unrelated private file contents if pointed at the wrong JSON file.

Mitigation: Provide only the intended localization request JSON as input.

Risk: The downstream operation writes a job artifact to the selected local output directory.

Mitigation: Choose a dedicated writable output folder and review the resulting artifact.

## Reference(s):

- [Localization Job Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/localization-job-desk)

## Skill Output:

**Output Type(s):** [Configuration, Files]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a translation setting or recorded job entry; the downstream operation also writes a local JSON artifact and reports its effect.]

## Skill Version(s):

3.0.0 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
