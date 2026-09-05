## Description:

Inspect a real public website and design a runnable Dataify-based scraper when no suitable prebuilt scraper exists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect public websites, route common platforms to prebuilt Dataify skills, and generate a bounded starter scraper with validation artifacts for requested fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target URLs and retrieved public HTML are sent to Dataify services and saved in the selected output directory.

Mitigation: Use the skill only for public targets where that transfer is acceptable, and review or clean generated output directories before sharing them.

Risk: The workflow uses a Dataify API token to call external services.

Mitigation: Use a scoped token, keep it in the environment instead of chat or project files, and never print or persist the token.

Risk: Generated scraper code may be incomplete or too target-specific for broad reuse.

Mitigation: Review the generated code and validation files, require non-empty samples and at least 90 percent requested-field completeness, and treat unsupported fields as needing selector refinement.

## Reference(s):

- [Prebuilt routing](references/prebuilt-routing.md)
- [Dataify documentation](https://doc.dataify.com)
- [Dataify support](https://www.dataify.com/)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-scraper-builder)

## Skill Output:

**Output Type(s):** [Analysis, Code, Files, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance with shell commands and generated JSON, HTML, and Python files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artifacts may include scraper_spec.json, site_profile.json, validation.json, sample_output.json, sample.html, and generated_scraper.py.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
