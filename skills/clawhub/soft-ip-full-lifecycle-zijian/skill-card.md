## Description: <br>
Software IP self-assessment skill for Chinese software copyright applications, delivering an AI-guided compliance review after clawtip payment verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and software teams use this skill to assess readiness for Chinese software copyright registration. It checks material completeness, source-code documentation, user manuals, rights attribution, and registration risks, then provides issue lists, risk ratings, and remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes a local order file containing the user's question and payment-related fields. <br>
Mitigation: Keep the initial question minimal when it could include source code, applicant details, or confidential business information, and remove old order files when local retention is no longer needed. <br>
Risk: The workflow depends on payment verification before the AI assessment is delivered. <br>
Mitigation: Confirm clawtip is installed and payment credentials are valid before relying on the service output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/soft-ip-full-lifecycle-zijian) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown-style compliance assessment with command output fields for order creation and payment verification] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language user-facing review; requires clawtip payment verification before assessment.] <br>

## Skill Version(s): <br>
3.1.44 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
