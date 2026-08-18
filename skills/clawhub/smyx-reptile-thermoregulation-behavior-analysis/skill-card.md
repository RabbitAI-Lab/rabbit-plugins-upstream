## Description:

Analyzes reptile enclosure video or video URLs to report basking, hiding, cool-zone dwell time, zone transitions, activity rhythm, and thermal-preference warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, breeders, and smart vivarium operators use this skill to assess whether reptiles are using basking, hiding, and cool zones in expected patterns. Agents can use it to run analysis, retrieve historical reports, and return structured observations, non-diagnostic welfare guidance, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded reptile videos or video URLs are processed by a remote service.

Mitigation: Use only media that is approved for remote processing and review the configured service endpoints before running the skill.

Risk: The skill uses an internal identity automatically and may store account tokens locally.

Mitigation: Review identity handling and local token storage before installation, especially in shared workspaces.

Risk: The package configuration may point to development or private service addresses.

Mitigation: Confirm endpoint configuration matches the intended deployment environment before use.

Risk: Behavior analysis could be mistaken for veterinary diagnosis or device-control authority.

Mitigation: Keep outputs limited to behavior observations and non-diagnostic guidance; require user confirmation for any environment changes and refer serious concerns to a qualified reptile veterinarian.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-thermoregulation-behavior-analysis)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured reports with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, thermal preference labels, alert levels, recommended actions, and disclaimers; analysis depends on remote service responses.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
