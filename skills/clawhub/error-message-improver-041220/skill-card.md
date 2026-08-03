## Description: <br>
Helps developers, support teams, and SaaS operators turn vague errors into clear messages that explain what failed, why it failed, and what to do next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and users use this skill to draft or improve error messages, troubleshooting workflows, checklists, and support-facing guidance. It is intended for work-productivity and debugging contexts where users need actionable failure explanations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording may route general debugging or support requests to this writing workflow when a more specific skill would fit better. <br>
Mitigation: Invoke the skill explicitly for error-message drafting and troubleshooting-copy work, and prefer a more specific technical skill for implementation or diagnosis tasks. <br>
Risk: Improved error text may still be misleading if the supplied failure context is incomplete or inaccurate. <br>
Mitigation: Review generated messages against actual product behavior and include the failure, likely cause, and user action before publishing. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/kyro-ma/skills/error-message-improver-041220) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [CryptoViz issue: Improve Loading, Empty and Error States](https://github.com/csxark/CryptoViz/issues/98) <br>
- [Kiali issue: OpenShift Impersonation for Multi-Cluster Auth](https://github.com/kiali/kiali/issues/10038) <br>
- [vg issue: No reference paths found](https://github.com/vgteam/vg/issues/4974) <br>
- [Apache tooling issue: Required resources down](https://github.com/apache/tooling-trusted-releases/issues/1395) <br>
- [SegmentFault: error-messages](https://segmentfault.com/t/error-messages) <br>
- [Hacker News: Hyprland 0.55 discussion](https://news.ycombinator.com/item?id=49002105) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown text with optional checklists, templates, code snippets, or workflow steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a short verification note, assumptions, limits, and follow-up work when useful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
