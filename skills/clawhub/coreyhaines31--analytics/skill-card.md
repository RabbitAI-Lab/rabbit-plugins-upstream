## Description: <br>
Helps users set up, improve, audit, and troubleshoot analytics tracking and measurement across tools such as GA4, Google Tag Manager, Mixpanel, Segment, and UTM-based campaign tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyhaines31](https://clawhub.ai/user/coreyhaines31) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, product, analytics, and engineering teams use this skill to define tracking plans, event taxonomies, UTM conventions, GA4/GTM implementations, and validation steps for measurement workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Analytics and advertising tags may be copied into production before valid consent rules are applied. <br>
Mitigation: Review consent requirements before implementation and configure GA4, GTM, pixels, and other third-party tags to fire only under the privacy rules that apply to the users. <br>
Risk: Tracking examples may encourage collection of PII, raw identifiers, or unnecessary user properties if copied without review. <br>
Mitigation: Audit event properties before deployment, avoid PII and raw user identifiers, and use pseudonymous identifiers where user-level tracking is required. <br>
Risk: Analytics guidance can produce misleading business metrics if event definitions, trigger conditions, or duplicate tags are not validated. <br>
Mitigation: Validate events with GA4 DebugView, GTM Preview mode, browser tools, and backend source-of-truth comparisons before relying on the data for decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coreyhaines31/skills/analytics) <br>
- [Publisher profile](https://clawhub.ai/user/coreyhaines31) <br>
- [Event Library Reference](references/event-library.md) <br>
- [GA4 Implementation Reference](references/ga4-implementation.md) <br>
- [Google Tag Manager Implementation Reference](references/gtm-implementation.md) <br>
- [Google Analytics recommended events](https://support.google.com/analytics/answer/9267735) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown with tables, checklists, and inline JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces tracking plans, event naming guidance, UTM conventions, debugging steps, and analytics implementation snippets; it does not generate executable files by itself.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; source frontmatter metadata reports 2.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
