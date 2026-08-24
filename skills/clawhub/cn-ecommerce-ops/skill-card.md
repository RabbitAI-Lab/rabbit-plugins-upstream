## Description:

cn-ecommerce-ops helps agents support China-focused e-commerce operations with product scoring, pricing and profit calculation, advertising ROI analysis, conversion-funnel diagnosis, copy compliance checks, and current-data command planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[g305595965](https://clawhub.ai/user/g305595965)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to make operational decisions for Chinese e-commerce stores, including product selection, pricing, paid-ad planning, store diagnostics, listing content, live-commerce workflows, and advertising-law copy review.

### Deployment Geography for Use:

Global, for China-focused e-commerce workflows where the user is authorized to access the relevant platform and business data.

## Known Risks and Mitigations:

Risk: The skill may ask the agent to look up current e-commerce data or use user-provided business inputs.

Mitigation: Use only accounts, platform pages, and business data that the user is authorized to access, and confirm important values against merchant backends before relying on the result.

Risk: The skill may read user-selected local text or JSON files for analysis.

Mitigation: Provide only intended files and avoid secrets or unrelated personal data in the inputs.

Risk: Generated live.py command plans can be influenced by inaccurate or untrusted input JSON.

Mitigation: Review generated command plans and missing-field notes before execution, especially when the source JSON was supplied by an untrusted party.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/g305595965/skills/cn-ecommerce-ops)
- [Server-resolved GitHub provenance](https://github.com/g305595965/cn-ecommerce-ops)
- [Platform Playbook](references/platform-playbook.md)
- [Product Selection Framework](references/product-selection.md)
- [Listing and Content Guide](references/listing-and-content.md)
- [Operations and Risk Playbook](references/operations-playbook.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional JSON output and shell-command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Python scripts use standard library only and support --json output; live.py can generate command plans from user-provided JSON data.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
