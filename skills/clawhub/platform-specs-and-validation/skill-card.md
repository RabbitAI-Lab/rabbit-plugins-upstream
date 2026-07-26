## Description: <br>
Platform Specs And Validation helps agents prepare multi-platform WoopSocial posts by mapping per-platform required fields, enforcing media and content constraints, and running the validate-before-publish loop before atomic creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and social-media teams use this skill to make fan-out posts publish-ready across connected WoopSocial accounts. It helps map required platform fields, resolve account-specific values, check media rules, and validate errors before publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incorrect target accounts, privacy settings, or disclosure declarations could result in unintended or misleading public posts. <br>
Mitigation: Have the person responsible for the post review target accounts, privacy choices, made-for-kids status, and branded-content declarations before publishing. <br>
Risk: Platform enums, limits, and account-specific options can change and make previously valid guidance stale. <br>
Mitigation: Resolve account-specific values from platform-inputs and run POST /posts/validate before creation; re-check the live WoopSocial spec when platform behavior may have changed. <br>
Risk: A multi-platform fan-out post can fail atomically when one target violates required fields or media rules. <br>
Mitigation: Validate every target together, fix all blocking errors, and use contentOverride or separate posts when one content item cannot satisfy every platform. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/social-media-skills/skills/platform-specs-and-validation) <br>
- [Scope, distinctions + connections](references/scope-and-connections.md) <br>
- [The CHECK framework](references/the-check-framework.md) <br>
- [Validation reference + two worked examples](references/validation-reference-and-recipes.md) <br>
- [WoopSocial publish spec](references/woopsocial-publish-spec.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with endpoint, field, and validation references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes CHECK-framework validation steps, per-platform field mappings, media constraints, and warnings for human-reviewed privacy and disclosure decisions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
