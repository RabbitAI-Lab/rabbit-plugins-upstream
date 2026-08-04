## Description: <br>
Deploy small, non-sensitive static sites to temporary Cloudflare Workers previews. Use when an intended user explicitly accepts Cloudflare terms and needs a short-lived workers.dev URL with a privately delivered Claim URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wei840222](https://clawhub.ai/user/wei840222) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to deploy small, non-sensitive static sites to short-lived Cloudflare Workers preview URLs after confirming the intended user accepts Cloudflare terms. It also guides private handling of the Claim URL needed to keep or manage the temporary account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: All regular files under the selected static directory can be embedded in a public Cloudflare Workers preview. <br>
Mitigation: Review the static directory before deployment and use the skill only for small, non-sensitive static sites. <br>
Risk: The Claim URL can transfer control of the temporary Cloudflare account if exposed. <br>
Mitigation: Write the Claim URL only to a new private local file and deliver it only to the intended user. <br>
Risk: Deployment to Cloudflare requires user acceptance of Cloudflare terms and privacy policy. <br>
Mitigation: Stop before provisioning unless the intended user explicitly accepts the terms and the command includes the terms-acceptance flag. <br>


## Reference(s): <br>
- [Cloudflare Temporary Preview Reference](references/cloudflare-api.md) <br>
- [Cloudflare Workers Temporary Accounts](https://developers.cloudflare.com/workers/platform/claim-deployments/) <br>
- [Cloudflare Workers Multipart Upload Metadata](https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/) <br>
- [Cloudflare Workers Limits](https://developers.cloudflare.com/workers/platform/limits/) <br>
- [ClawHub Skill Page](https://clawhub.ai/wei840222/skills/cloudflare-drop) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a public workers.dev Live URL and writes the Claim URL to a caller-selected private local file.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
