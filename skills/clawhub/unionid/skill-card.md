## Description:

Queries JD.com payment PINs, login PINs, and basic account information associated with a WeChat unionid.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuoxiangpang](https://clawhub.ai/user/zhuoxiangpang)

### License/Terms of Use:

MIT-0

## Use Case:

Support, fraud, compliance, or account operations teams use this skill to look up JD.com account identifiers and basic account details linked to a supplied WeChat unionid, subject to approved authorization and data-access controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive account-linkage data and full account details without built-in safeguards.

Mitigation: Run it only inside approved support, fraud, or compliance workflows with authorization checks, query logging, masking, and field minimization.

Risk: A supplied WeChat unionid can lead to retrieval of linked JD.com payment PINs, login PINs, and account fields.

Mitigation: Require a legitimate case or workflow authorization before lookup and return only the minimum fields needed for the approved task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhuoxiangpang/skills/unionid)
- [Publisher profile](https://clawhub.ai/user/zhuoxiangpang)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown guidance describing account lookup steps and returned account information]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a WeChat unionid input and authorized access to the referenced account data tables.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
