## Description:

The jf-store-traffic skill helps agents deploy and operate a JF precise store foot-traffic workflow, including store creation, HA-5P-GM camera onboarding, traffic-area configuration, aggregate traffic queries, and visual HTML traffic reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jftech](https://clawhub.ai/user/jftech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, store operations teams, and deployment engineers use this skill to configure JF HA-5P-GM cameras for precise store traffic analytics and to query or report aggregate foot-traffic metrics.

### Deployment Geography for Use:

China mainland

## Known Risks and Mitigations:

Risk: The skill can use JF API credentials and camera access, including live camera imagery.

Mitigation: Use scoped credentials where possible, store them outside shared files, and grant access only in environments approved for camera operations.

Risk: The workflow includes commands that delete store or device resources.

Mitigation: Confirm exact store and device identifiers before delete operations and keep session state under review.

Risk: Generated HTML reports may contain sensitive traffic data and may load third-party chart code.

Mitigation: Handle reports as sensitive business documents and review or host chart dependencies according to local security policy.

Risk: Default or empty camera passwords can expose camera streams or device administration.

Mitigation: Set non-default camera passwords before deployment and avoid sharing camera credentials in prompts or generated files.

## Reference(s):

- [JF Precise Store Traffic OpenAPI Reference](references/api-reference.md)
- [ClawHub Skill Page](https://clawhub.ai/jftech/skills/jf-store-traffic)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, HTML reports, JSON]

**Output Format:** [Markdown guidance with shell commands, JSON configuration, tabular or JSON statistics, and generated HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports may contain inlined traffic data and browser-rendered charts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
