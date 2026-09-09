## Description:

Analyzes fixed-camera shelter video or image input to report visual behavior observations associated with acute stress reactions, including stupor, tremor, unresponsiveness, and hypervigilance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Emergency-response operators, command-center staff, and authorized psychological rescue teams use this skill to analyze emergency shelter footage, produce behavior-observation alerts, and guide human review and Psychological First Aid follow-up. The skill is an operational aid and does not provide clinical diagnoses or medication guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles highly sensitive emergency shelter footage and report history.

Mitigation: Deploy only in an authorized emergency-response environment, document remote processing, and limit use to approved rescue and command-center workflows.

Risk: The release defaults to insecure HTTP endpoints.

Mitigation: Change the release configuration to HTTPS production endpoints before installation or execution.

Risk: The skill silently creates identities and caches tokens.

Mitigation: Replace plaintext token caching with a managed secret store or short-lived in-memory credentials.

Risk: Historical report queries may expose sensitive incident records.

Mitigation: Disable history queries unless they are explicitly required and authorized for the deployment.

## Reference(s):

- [API interface documentation](artifact/references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-trauma-stress-behavior-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with structured JSON-like analysis, crisis alert details, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write the generated report text to a local output file when an output path is supplied.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
